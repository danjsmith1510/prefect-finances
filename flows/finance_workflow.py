from prefect import flow
import json, pytz, datetime as dt
from helpers import get_missing_pocketsmith_categories
from bigquery import load_finances_extract_table, run_finance_merge_extracts
from pocketsmith import get_pocketsmith_accounts, get_pocketsmith_categories, get_pocketsmith_transactions, post_pocketsmith_category
from jira import get_jira_epics, get_jira_stories

tz = pytz.timezone('Australia/Sydney')
timestamp = dt.datetime.now(tz).isoformat()
start_date_raw = dt.datetime.today().astimezone(tz) - dt.timedelta(days=10)
start_date = start_date_raw.strftime('%Y-%m-%d')
end_date = dt.datetime.today().astimezone(tz).strftime('%Y-%m-%d')

@flow(log_prints=True)
def finance_flow():

    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print(f"Load timestamp: {timestamp}")

    jira_categories = get_jira_epics()
    pocketsmith_categories = get_pocketsmith_categories()
    missing_pocketsmith_categories = get_missing_pocketsmith_categories(jira_categories, pocketsmith_categories)
    if len(missing_pocketsmith_categories) > 0:
        print(f"Need to add {len(missing_pocketsmith_categories)} categories to PocketSmith")
        for missing_pocketsmith_category in missing_pocketsmith_categories:
            print(f"Adding {missing_pocketsmith_category['title']} category to PocketSmith")
            post_pocketsmith_category(missing_pocketsmith_category)
    else:
        print(f"All JIRA epics have a corresponding category")

    accounts = get_pocketsmith_accounts()
    print(f"Got {len(accounts)} accounts")
    load_finances_extract_table('account', json.dumps(accounts), timestamp)

    categories = get_pocketsmith_categories()
    print(f"Got {len(categories)} categories")
    load_finances_extract_table('category', json.dumps(categories), timestamp)

    transactions = get_pocketsmith_transactions(start_date, end_date)
    print(f"Got {len(transactions)} transactions")
    load_finances_extract_table('transaction', json.dumps(transactions), timestamp)

    tasks = get_jira_stories()
    print(f"Got {len(tasks)} tasks")
    load_finances_extract_table('task', json.dumps(tasks), timestamp)

    run_merge = run_finance_merge_extracts(start_date, end_date)
    print (run_merge)

if __name__ == "__main__":
    finance_flow()