# import json
from prefect import flow
# import datetime as dt
# from tasks.finance_database import load_extract_table, run_merge_extracts
# from tasks.pocketsmith import get_pocketsmith_accounts, get_pocketsmith_categories, get_pocketsmith_transactions
# from tasks.jira import get_jira_stories

# start_date_raw = dt.datetime.today() - dt.timedelta(days=7)
# start_date = start_date_raw.strftime('%Y-%m-%d')
# end_date = dt.datetime.today().strftime('%Y-%m-%d')

@flow(log_prints=True)
def finance_workflow():

    print ('TEST RUN')

    # accounts = get_pocketsmith_accounts()
    # print(f"Got {len(accounts)} accounts")
    # load_extract_table('accounts', json.dumps(accounts))

    # categories = get_pocketsmith_categories()
    # print(f"Got {len(categories)} categories")
    # load_extract_table('category', json.dumps(categories))

    # transactions = get_pocketsmith_transactions(start_date, end_date)
    # print(f"Got {len(transactions)} transactions")
    # load_extract_table('transaction', json.dumps(transactions))

    # tasks = get_jira_stories()
    # print(f"Got {len(tasks)} tasks")
    # load_extract_table('task', json.dumps(tasks))

    # run_merge = run_merge_extracts(start_date, end_date)
    # print (run_merge)

if __name__ == "__main__":
    finance_workflow()