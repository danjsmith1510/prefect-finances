# # import json
# # import time
# # from nba_api.stats.endpoints import scoreboardv2, boxscoretraditionalv3
# from nba_api.stats.endpoints import playerindex
# # from nba_api.stats.static.teams import get_nba_teams
# # import pytz
# import datetime
# # from bigquery import load_sports_extract_table

# # leagueid = '10'
# # # leagueId_list = [['10', 'wnba'], ['00', 'nba']]
# # daysAheadToGet = 25
# # daysBeforeToGet = 14

# # game_list = []
# # box_score_list = []

# # tz = pytz.timezone('Australia/Sydney')
# # timestamp = dt.datetime.now(tz).isoformat()
# # # start_date= dt.datetime.today().astimezone(tz) - dt.timedelta(days=daysBeforeToGet)
# # # end_date = dt.datetime.today().astimezone(tz) + dt.timedelta(days=daysAheadToGet)
# # start_date = dt.date(year=2024, month=5, day=14)
# # end_date   = dt.date(year=2024, month=9, day=16)
# # print (start_date.strftime('%Y-%m-%d') + ' --> ' + end_date.strftime('%Y-%m-%d'))

# # current_date = start_date
# # while current_date <= end_date:
# #     day_scoreboard = scoreboardv2.ScoreboardV2(
# #         game_date=current_date.strftime('%Y-%m-%d'), 
# #         league_id=leagueid, 
# #         timeout=100
# #     ) 
# #     game_list_dict = day_scoreboard.get_normalized_dict()['GameHeader']
# #     print (current_date.strftime('%Y-%m-%d') + ': ' + str(len(game_list_dict)))
# #     if (len(game_list_dict) > 0):
# #         for game in game_list_dict:
# #             game['leagueid'] = leagueid
# #             # game['gamedate'] = current_date.strftime('%Y-%m-%d')
# #             game_list.append(game)
# #             game_id = game['GAME_ID']
# #             print (game)
# #             # try:
# #             #     box_score_raw = boxscoretraditionalv3.BoxScoreTraditionalV3(game_id=game_id)
# #             #     box_score = box_score_raw.get_dict()['boxScoreTraditional']
# #             #     box_score['gamedate'] = current_date.strftime('%Y-%m-%d')
# #             #     box_score['leagueid'] = leagueid
# #             #     box_score_list.append(box_score)
# #             time.sleep(4)
# #             # except AttributeError:
# #             #     continue
# #     current_date += dt.timedelta(days=1)
# # print (len(game_list))
# # # load_sports_extract_table('schedule', json.dumps(game_list), timestamp)
# # # load_sports_extract_table('boxscore', json.dumps(box_score_list), timestamp)


# # # playerIndex = playerindex.PlayerIndex(league_id=leagueid)
# # # player_dict = playerIndex.get_normalized_dict()['PlayerIndex']
# # # print (player_dict[0])
# # # print (playerIndex.get_normalized_dict()['PlayerIndex'][0])

# # # wnba_teams = get_wnba_teams()
# # # print (wnba_teams[0])

# # nba_teams = get_nba_teams()

# from nba_api.stats.endpoints.playerindex import PlayerIndex

# playerIndex = PlayerIndex(league_id='00')
# player_dict = playerIndex.get_normalized_dict()['PlayerIndex']
# print (len(player_dict))
# print (player_dict[0])

# import pytz
# tz = pytz.timezone('US/Eastern')
# from datetime import datetime
# x = datetime.today().astimezone(tz).strftime('%Y-%m-%d')
# print (x)

# import datetime
# # print (datetime.datetime.fromisoformat('2023-10-24 15:55:44+00:00', datetime.datetime.fromisoformat('2023-10-24 23:30:00+00:00')
# timeDiff = datetime.datetime.fromisoformat('2024-01-16 02:30:00+00:00') - datetime.datetime.fromisoformat('2023-10-24 15:55:44+00:00')
# print (timeDiff)
# print (timeDiff.total_seconds()//3600)

# from nba_api.stats.endpoints import BoxScoreAdvancedV2, scoreboardv2

# day_scoreboard = scoreboardv2.ScoreboardV2(game_date='2023-10-24', league_id='00', timeout=100) 
# game_list_dict = day_scoreboard.get_normalized_dict()['GameHeader']
# for game in game_list_dict:
#     box_score_raw = BoxScoreAdvancedV2(game_id=game['GAME_ID'])
#     box_score = box_score_raw.get_normalized_dict()['TeamStats']
#     print(box_score)
# box_score = box_score_raw.get_dict()['boxScoreTraditional']

# import requests, time, datetime
# from datetime import timezone 

# oddsapi_apikey = 'eb6cc7067fa1a52dcdc14efb7a6c6eda'
# oddsapi_url_get_events = 'https://api.the-odds-api.com/v4/sports/basketball_nba/events?apiKey=' + oddsapi_apikey
# oddsapi_url_get_event_markets = 'https://api.the-odds-api.com/v4/sports/basketball_nba/events/'
# oddsapi_regions = 'au,us,us2'
# oddsapi_markets = 'player_points,player_rebounds,player_assists,player_threes,player_points_alternate,player_rebounds_alternate,player_assists_alternate,player_threes_alternate'

# now_utc = datetime.datetime.now(timezone.utc).isoformat()

# oddsList = []
# response = requests.get(oddsapi_url_get_events)
# events = response.json()
# time.sleep(1)
# for event in events:
#     timeDiff = datetime.datetime.fromisoformat(event['commence_time']) - datetime.datetime.fromisoformat(now_utc)
#     if (timeDiff.total_seconds()//3600) < 130:
#         print (event)
#         print(f"{event['id']} - {event['away_team']} @ {event['home_team']} - {event['commence_time']} is {str(timeDiff.total_seconds()//3600)} hours away --> fetching player props")
#         markets_url = oddsapi_url_get_event_markets + event['id'] + '/odds?apiKey=' + oddsapi_apikey + '&regions=' + oddsapi_regions + '&markets=' + oddsapi_markets
#         print (markets_url)
#         markets = requests.get(markets_url)
#         oddsList.append(markets.json())
#     time.sleep(1)
# print (oddsList)

import requests, time
jira_headers = {
    "accept": "application/json",
    "authorization": "Basic ZGFuaWVsanNtaXRoMTUxMEBnbWFpbC5jb206QVRBVFQzeEZmR0YwVDdYbE1LVXpmMUpKM21BU2R3cnhsT0ZWaDFPeXdaZmFqZzFnbE5RcmNZSUl3Wjc2SjJvWnUza1g4ZjU1MmFkOWZyczVFTFI1cWdfN2psamRUTUI3M2FxWjZSUnZmZnlUeFpod3RWLU1BampheFRmenhnZ0owVkJmQjNOSTFqeUExVVFMWmZxV2N3aWRzdkNOQkxzWDJKNDdzWmxKZlFiTTlub1lPMUFqOGs0PUJBNkQxNjhE"
}
jira_url_stories = 'https://ernie2022.atlassian.net/rest/api/2/search?jql=type=Story&maxResults=100'
jira_url_epics = 'https://ernie2022.atlassian.net/rest/api/2/search?jql=type=Epic&maxResults=100'

def processJiraStories(stories):
    tasks = []
    for element in stories['issues']:
        estimated_cost = element['fields']['customfield_10060']
        if 'parent' in element['fields']:
            parent_epic = element['fields']['parent']['fields']['summary']
            if estimated_cost is not None:
                task = {
                    'ID': int(element['id']), 
                    'Project': parent_epic,
                    'TrackProgress': 1,
                    'Description': element['fields']['summary'],
                    'Priority': 0,
                    'Effort': 0,
                    'Estimate': element['fields']['customfield_10060'],
                    'PercentComplete': element['fields']['customfield_10061'],
                    'Expected': element['fields']['customfield_10062'],
                    'RemainingEstimate': element['fields']['customfield_10063']
                }  
            tasks.append(task)
    return tasks

alltasks = []
response = requests.get(jira_url_stories, headers=jira_headers)
time.sleep(2)
storyCount = response.json()['total']
startAtCounter = 0
while (startAtCounter < storyCount):
    response = requests.get(jira_url_stories + '&startAt=' + str(startAtCounter), headers=jira_headers)
    alltasks.extend(processJiraStories(response.json()))
    print (len(alltasks))
    print (alltasks[-1])
    startAtCounter = startAtCounter + 100
    time.sleep(2)

# for element in stories['issues']:
#     estimated_cost = element['fields']['customfield_10060']
#     if 'parent' in element['fields']:
#         parent_epic = element['fields']['parent']['fields']['summary']
#         if estimated_cost is not None:
#             task = {
#                 'ID': int(element['id']), 
#                 'Project': parent_epic,
#                 'TrackProgress': 1,
#                 'Description': element['fields']['summary'],
#                 'Priority': 0,
#                 'Effort': 0,
#                 'Estimate': element['fields']['customfield_10060'],
#                 'PercentComplete': element['fields']['customfield_10061'],
#                 'Expected': element['fields']['customfield_10062'],
#                 'RemainingEstimate': element['fields']['customfield_10063']
#             }  
#             tasks.append(task)