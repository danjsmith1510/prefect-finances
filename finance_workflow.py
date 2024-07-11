import json
from prefect import flow
import datetime as dt
import pytz
from tasks.finance_database import load_extract_table, run_merge_extracts
from tasks.pocketsmith import get_pocketsmith_accounts, get_pocketsmith_categories, get_pocketsmith_transactions
from tasks.jira import get_jira_stories

tz = pytz.timezone('Australia/Sydney')
timestamp = dt.datetime.now(tz).isoformat()
start_date_raw = dt.datetime.today().astimezone(tz) - dt.timedelta(days=7)
start_date = start_date_raw.strftime('%Y-%m-%d')
end_date = dt.datetime.today().astimezone(tz).strftime('%Y-%m-%d')

print(f"Start Date: {start_date}")
print(f"End Date: {end_date}")
print(f"Load timestamp: {timestamp}")

@flow(log_prints=True)
def finance_workflow():

    accounts = get_pocketsmith_accounts()
    print(f"Got {len(accounts)} accounts")
    load_extract_table('accounts', json.dumps(accounts), timestamp)

    categories = get_pocketsmith_categories()
    print(f"Got {len(categories)} categories")
    load_extract_table('category', json.dumps(categories), timestamp)

    transactions = get_pocketsmith_transactions(start_date, end_date)
    print(f"Got {len(transactions)} transactions")
    load_extract_table('transaction', json.dumps(transactions), timestamp)

    tasks = get_jira_stories()
    print(f"Got {len(tasks)} tasks")
    load_extract_table('task', json.dumps(tasks), timestamp)

    run_merge = run_merge_extracts(start_date, end_date)
    print (run_merge)

if __name__ == "__main__":
    finance_workflow()