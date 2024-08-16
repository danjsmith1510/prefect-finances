import json
from prefect import flow
import datetime as dt
import pytz
from tasks.bigquery import load_sports_extract_table, run_sports_merge_extracts
from tasks.nbastats import get_active_players_nba, get_box_scores, get_schedule, get_teams_nba

league_id = '00'
start_date = dt.date(year=2024, month=5, day=1)
end_date   = dt.date(year=2024, month=6, day=30)
# end_date   = dt.date(year=2024, month=9, day=20)
# start_date= dt.datetime.today().astimezone(tz) - dt.timedelta(days=daysBeforeToGet)
# end_date = dt.datetime.today().astimezone(tz) + dt.timedelta(days=daysAheadToGet)


@flow(log_prints=True)
def sports_base_workflow():

    tz = pytz.timezone('Australia/Sydney')
    timestamp = dt.datetime.now(tz).isoformat()

    nba_teams = get_teams_nba()
    print(f"Got {len(nba_teams)} nba teams")
    load_sports_extract_table('teams', json.dumps(nba_teams), timestamp)

    active_nba_players = get_active_players_nba()
    print(f"Got {len(active_nba_players)} active nba players")
    load_sports_extract_table('players', json.dumps(active_nba_players), timestamp)

    nba_game_list = get_schedule(start_date, end_date, league_id)
    print(f"Got {len(nba_game_list)} nba games")
    load_sports_extract_table('schedule', json.dumps(nba_game_list), timestamp)

    nba_boxscore_list = get_box_scores(nba_game_list, league_id)
    print(f"Got {len(nba_boxscore_list)} nba boxscores")
    load_sports_extract_table('boxscore', json.dumps(nba_boxscore_list), timestamp)

    run_merge = run_sports_merge_extracts()
    print (run_merge)

if __name__ == "__main__":
    sports_base_workflow()