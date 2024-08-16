# import json
# import time
# from nba_api.stats.endpoints import scoreboardv2, boxscoretraditionalv3
# from nba_api.stats.endpoints import playerindex
from nba_api.stats.static.teams import get_nba_teams
# import pytz
# import datetime as dt
# from bigquery import load_sports_extract_table

# leagueid = '10'
# # leagueId_list = [['10', 'wnba'], ['00', 'nba']]
# daysAheadToGet = 25
# daysBeforeToGet = 14

# game_list = []
# box_score_list = []

# tz = pytz.timezone('Australia/Sydney')
# timestamp = dt.datetime.now(tz).isoformat()
# # start_date= dt.datetime.today().astimezone(tz) - dt.timedelta(days=daysBeforeToGet)
# # end_date = dt.datetime.today().astimezone(tz) + dt.timedelta(days=daysAheadToGet)
# start_date = dt.date(year=2024, month=5, day=14)
# end_date   = dt.date(year=2024, month=9, day=16)
# print (start_date.strftime('%Y-%m-%d') + ' --> ' + end_date.strftime('%Y-%m-%d'))

# current_date = start_date
# while current_date <= end_date:
#     day_scoreboard = scoreboardv2.ScoreboardV2(
#         game_date=current_date.strftime('%Y-%m-%d'), 
#         league_id=leagueid, 
#         timeout=100
#     ) 
#     game_list_dict = day_scoreboard.get_normalized_dict()['GameHeader']
#     print (current_date.strftime('%Y-%m-%d') + ': ' + str(len(game_list_dict)))
#     if (len(game_list_dict) > 0):
#         for game in game_list_dict:
#             game['leagueid'] = leagueid
#             # game['gamedate'] = current_date.strftime('%Y-%m-%d')
#             game_list.append(game)
#             game_id = game['GAME_ID']
#             print (game)
#             # try:
#             #     box_score_raw = boxscoretraditionalv3.BoxScoreTraditionalV3(game_id=game_id)
#             #     box_score = box_score_raw.get_dict()['boxScoreTraditional']
#             #     box_score['gamedate'] = current_date.strftime('%Y-%m-%d')
#             #     box_score['leagueid'] = leagueid
#             #     box_score_list.append(box_score)
#             time.sleep(4)
#             # except AttributeError:
#             #     continue
#     current_date += dt.timedelta(days=1)
# print (len(game_list))
# # load_sports_extract_table('schedule', json.dumps(game_list), timestamp)
# # load_sports_extract_table('boxscore', json.dumps(box_score_list), timestamp)


# # playerIndex = playerindex.PlayerIndex(league_id=leagueid)
# # player_dict = playerIndex.get_normalized_dict()['PlayerIndex']
# # print (player_dict[0])
# # print (playerIndex.get_normalized_dict()['PlayerIndex'][0])

# # wnba_teams = get_wnba_teams()
# # print (wnba_teams[0])

nba_teams = get_nba_teams()

