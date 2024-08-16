import time
import datetime as dt
from prefect import task
from prefect_gcp.bigquery import GcpCredentials
from nba_api.stats.endpoints import scoreboardv2, boxscoretraditionalv3
from nba_api.stats.static import players as pl
from nba_api.stats.static.teams import get_teams

# @task(retries=2)
# def get_active_players_wnba():
#     """Get all active players for wnba"""
#     active_players_wnba =  pl.get_wnba_active_players()
#     active_players_wnba_dict = [dict(active_player_wnba, **{'league_id':'10'}) for active_player_wnba in active_players_wnba]
#     return active_players_wnba_dict

@task(retries=2)
def get_active_players_nba():
    """Get all active players for nba"""
    active_players_nba =  pl.get_active_players()
    active_players_nba_dict = [dict(active_player_nba, **{'league_id':'00'}) for active_player_nba in active_players_nba]
    return active_players_nba_dict

@task(retries=2)
def get_teams_nba():
    """Get all nba teams"""
    nba_teams =  get_teams()
    nba_teams_dict = [dict(nba_team, **{'league_id':'10'}) for nba_team in nba_teams]
    return nba_teams_dict

@task(retries=2)
def get_schedule(start_date, end_date, leagueid):
    """Get all nba or wnba games"""
    game_list=[]
    current_date = start_date
    while current_date <= end_date:
        day_scoreboard = scoreboardv2.ScoreboardV2(game_date=current_date.strftime('%Y-%m-%d'), league_id=leagueid, timeout=100) 
        game_list_dict = day_scoreboard.get_normalized_dict()['GameHeader']
        print (current_date.strftime('%Y-%m-%d') + ': ' + str(len(game_list_dict)))
        if (len(game_list_dict) > 0):
            for game in game_list_dict:
                game['league_id'] = leagueid
                game_list.append(game)
        time.sleep(2.5)
        current_date += dt.timedelta(days=1)
    return game_list

@task(retries=2)
def get_box_scores(game_list, league_id):
    """Get all nba or wnba boxscores"""
    box_score_list = []
    for game in game_list:
        status = game['GAME_STATUS_TEXT']
        if (status == 'Final'):
            try:
                box_score_raw = boxscoretraditionalv3.BoxScoreTraditionalV3(game_id=game['GAME_ID'])
                box_score = box_score_raw.get_dict()['boxScoreTraditional']
                box_score['league_id'] = league_id
                box_score_list.append(box_score)
                time.sleep(2.5)
            except AttributeError:
                continue 
    return box_score_list