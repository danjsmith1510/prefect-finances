from prefect_gcp.bigquery import GcpCredentials
from nba_api.stats.endpoints import scoreboardv2, boxscoretraditionalv3
from finance_database import load_sports_extract_table
import json, time, pytz, datetime as dt

gcp_credentials = GcpCredentials.load("gcp-credentials-home-dashboard")
tz = pytz.timezone('Australia/Sydney')
timestamp = dt.datetime.now(tz).isoformat()
start_date = dt.date(year=2023, month=10, day=24)
end_date   = dt.date(year=2023, month=10,  day=25)
# start_date_raw = dt.datetime.today().astimezone(tz) - dt.timedelta(days=3)
# start_date = start_date_raw.strftime('%Y-%m-%d')
# end_date = dt.datetime.today().astimezone(tz).strftime('%Y-%m-%d')

box_score_list = []
current_date = start_date
while current_date <= end_date:
    print (current_date)
    day_scoreboard = scoreboardv2.ScoreboardV2(game_date=current_date.strftime('%Y-%m-%d')) 
    game_list_dict = day_scoreboard.get_normalized_dict()['GameHeader']
    game_ids = [o['GAME_ID'] for o in game_list_dict]
    for game_id in game_ids:
        box_score_raw = boxscoretraditionalv3.BoxScoreTraditionalV3(game_id=game_id)
        box_score = box_score_raw.get_dict()['boxScoreTraditional']
        box_score_list.append(box_score)
        time.sleep(1.75)
    current_date += dt.timedelta(days=1)
load_sports_extract_table('boxscore', json.dumps(box_score_list), timestamp)