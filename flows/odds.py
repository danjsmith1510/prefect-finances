import datetime
from prefect import task
import time, requests
from datetime import timezone 

oddsapi_apikey = 'eb6cc7067fa1a52dcdc14efb7a6c6eda'
oddsapi_url_get_events = 'https://api.the-odds-api.com/v4/sports/basketball_nba/events?apiKey=' + oddsapi_apikey
oddsapi_url_get_event_markets = 'https://api.the-odds-api.com/v4/sports/basketball_nba/events/'
oddsapi_regions = 'au,us,us2'
oddsapi_markets = 'player_points,player_rebounds,player_assists,player_threes,player_points_alternate,player_rebounds_alternate,player_assists_alternate,player_threes_alternate,player_points_rebounds_assists,player_points_rebounds_assists_alternate,player_steals,player_blocks'


now_utc = datetime.datetime.now(timezone.utc).isoformat()

@task(retries=2)
def get_nba_playerprop_odds():
    """Get all nba events from odds api"""
    oddsList = []
    response = requests.get(oddsapi_url_get_events)
    events = response.json()
    time.sleep(2)
    for event in events:
        timeDiff = datetime.datetime.fromisoformat(event['commence_time']) - datetime.datetime.fromisoformat(now_utc)
        if (timeDiff.total_seconds()//3600) < 26: #change to 26 day before season
            print(f"{event['id']} - {event['away_team']} @ {event['home_team']} - {event['commence_time']} is {str(timeDiff.total_seconds()//3600)} hours away --> fetching player props")
            markets_url = oddsapi_url_get_event_markets + event['id'] + '/odds?apiKey=' + oddsapi_apikey + '&regions=' + oddsapi_regions + '&markets=' + oddsapi_markets
            markets = requests.get(markets_url)
            print(f"{event['id']} - {event['away_team']} @ {event['home_team']} - {event['commence_time']} --> got player props from {str(len(markets.json()))} bookies")
            oddsList.append(markets.json())
        else:
            print(f"{event['id']} - {event['away_team']} @ {event['home_team']} - {event['commence_time']} is {str(timeDiff.total_seconds()//3600)} hours away --> not fetching player props")
        time.sleep(1.5)
    return (oddsList)