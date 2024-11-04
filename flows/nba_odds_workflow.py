import time
from prefect import flow
import json, pytz, datetime as dt
from bigquery import load_sports_extract_table, run_sports_merge_odds_extracts
from odds import get_nba_playerprop_odds

local_tz = pytz.timezone('Australia/Sydney')

@flow(log_prints=True)
def nba_odds_workflow():

    timestamp = dt.datetime.now(local_tz).isoformat()
    nba_playerprop_odds = get_nba_playerprop_odds()
    load_sports_extract_table('playerprops', json.dumps(nba_playerprop_odds), timestamp)
    run_sports_merge_odds_extracts()
    time.sleep(1)

if __name__ == "__main__":
    nba_odds_workflow()