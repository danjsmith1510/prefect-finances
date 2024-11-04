from prefect import task
import requests

pocketsmith_headers = {
    "accept": "application/json",
    "X-Developer-Key": "a19c67978a0aed584594880d07a4235dbff975d1cf2c81b0cb90626e132bb6dfe9bacfdf0030c0f4386e141b7edfdc044e3c95265eee2f1d6b399a0a80a1f4ce"
}
pocketsmith_url_categories = 'https://api.pocketsmith.com/v2/users/401501/categories'
pocketsmith_url_accounts = "https://api.pocketsmith.com/v2/users/401501/accounts"
pocketsmith_url_credit_card_transactions = 'https://api.pocketsmith.com/v2/accounts/2307979/transactions'
pocketsmith_url_offset_transactions = 'https://api.pocketsmith.com/v2/accounts/2307976/transactions'
pocketsmith_url_post_category = 'https://api.pocketsmith.com/v2/users/401501/categories'
pocketsmith_credit_card_transactions_pages_to_fetch = 10

@task(retries=2)
def get_pocketsmith_categories():
    """Get categories from pocketsmith"""
    response = requests.get(pocketsmith_url_categories, headers=pocketsmith_headers)
    categories = response.json()
    return categories


@task(retries=2)
def get_pocketsmith_accounts():
    """Get accounts from pocketsmith"""
    response = requests.get(pocketsmith_url_accounts, headers=pocketsmith_headers)
    accounts = response.json()
    return accounts

def get_pocketsmith_transactions(start_date, end_date):
    """Get transactions from pocketsmith"""
    transactions = []
    a = 1
    while a <= pocketsmith_credit_card_transactions_pages_to_fetch:
        response = requests.get(
            pocketsmith_url_credit_card_transactions + '?start_date=' + start_date + '&end_date='+ end_date + '&page=' + str(a), 
            headers=pocketsmith_headers
        )
        if 'Requested page is out of bounds' not in str(response.json()):
            transactions.extend(response.json())
        a=a+1
    response = requests.get(
        pocketsmith_url_offset_transactions + '?start_date=' + start_date + '&end_date='+ end_date, 
        headers=pocketsmith_headers
    )
    transactions.extend(response.json())
    return transactions

@task(retries=2)
def post_pocketsmith_category(new_pocketsmith_category):
    """Create new pocketsmith category"""
    response = requests.post(pocketsmith_url_post_category, json = new_pocketsmith_category, headers=pocketsmith_headers)
    print (response)
    return True