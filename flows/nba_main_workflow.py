from prefect import flow
import json, pytz, datetime as dt, time
from bigquery import load_sports_extract_table, run_sports_merge_main_extracts
from nba import get_player_box_scores, get_team_box_scores, get_players, get_schedule

league_id = '00'
local_tz = pytz.timezone('Australia/Sydney')
et_tz = pytz.timezone('US/Eastern')
today_et = dt.datetime.today().astimezone(et_tz).date()

schedule_start_date = today_et
schedule_end_date = dt.date(year=2025, month=4, day=16)
boxscore_start_date = today_et - dt.timedelta(days=2)
boxscore_end_date = today_et

@flow(log_prints=True)
def nba_main_workflow():

    print(f"Schedule Start Date: {schedule_start_date.strftime('%Y-%m-%d')}")
    print(f"Schedule End Date: {schedule_end_date.strftime('%Y-%m-%d')}")
    print(f"Boxscore Start Date: {boxscore_start_date.strftime('%Y-%m-%d')}")
    print(f"Boxscore End Date: {boxscore_end_date.strftime('%Y-%m-%d')}")

    timestamp = dt.datetime.now(local_tz).isoformat()

    nba_players = get_players()
    print(f"Got {len(nba_players)} nba players")
    load_sports_extract_table('players', json.dumps(nba_players), timestamp)

    nba_schedule = get_schedule(schedule_start_date, schedule_end_date, league_id)
    print(f"Got {len(nba_schedule)} nba games")
    load_sports_extract_table('schedule', json.dumps(nba_schedule), timestamp)

    nba_get_boxscore_list = get_schedule(boxscore_start_date, boxscore_end_date, league_id)
    print(f"Got {len(nba_get_boxscore_list)} box scores to fetch")

    nba_player_boxscore_list = get_player_box_scores(nba_get_boxscore_list, league_id)
    print(f"Got {len(nba_player_boxscore_list)} nba player boxscores")
    load_sports_extract_table('boxscore', json.dumps(nba_player_boxscore_list), timestamp)

    nba_team_boxscore_list = get_team_box_scores(nba_get_boxscore_list, league_id)
    print(f"Got {len(nba_team_boxscore_list)} nba team boxscores")
    load_sports_extract_table('boxscoreteam', json.dumps(nba_team_boxscore_list), timestamp)

    run_merge = run_sports_merge_main_extracts(boxscore_start_date)
    print (run_merge)

if __name__ == "__main__":
    nba_main_workflow()