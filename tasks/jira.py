from prefect import task
import requests

jira_headers = {
    "accept": "application/json",
    "authorization": "Basic ZGFuaWVsanNtaXRoMTUxMEBnbWFpbC5jb206QVRBVFQzeEZmR0YwVDdYbE1LVXpmMUpKM21BU2R3cnhsT0ZWaDFPeXdaZmFqZzFnbE5RcmNZSUl3Wjc2SjJvWnUza1g4ZjU1MmFkOWZyczVFTFI1cWdfN2psamRUTUI3M2FxWjZSUnZmZnlUeFpod3RWLU1BampheFRmenhnZ0owVkJmQjNOSTFqeUExVVFMWmZxV2N3aWRzdkNOQkxzWDJKNDdzWmxKZlFiTTlub1lPMUFqOGs0PUJBNkQxNjhE"
}
jira_url_stories = 'https://ernie2022.atlassian.net/rest/api/2/search?jql=type=Story&maxResults=100'

@task(retries=2)
def get_jira_stories():
    """Get stories from JIRA and format as tasks"""
    tasks = []
    response = requests.get(jira_url_stories, headers=jira_headers)
    stories = response.json()
    for element in stories['issues']:
        estimated_cost = element['fields']['customfield_10060']
        if estimated_cost is not None:
            task = {
                'ID': int(element['id']), 
                'Project': element['fields']['parent']['fields']['summary'],
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