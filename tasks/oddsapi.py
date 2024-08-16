import json
import datetime as dt
import pytz
from bigquery import load_sports_extract_table
tz = pytz.timezone('Australia/Sydney')
timestamp = dt.datetime.now(tz).isoformat()

input_file = open ('tasks/sample.json', 'r')
json_array = json.load(input_file)
odds_dict = [dict(event, **{'leagueid':'00'}) for event in json_array]
load_sports_extract_table('playerprops', json.dumps(json_array), timestamp)