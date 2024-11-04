from prefect import task

@task(retries=2)
def get_missing_pocketsmith_categories(jira_categories, pocketsmith_categories):
    """Return a list of JIRA epics without a corresponding pocketsmith category"""
    missing_pocketsmith_categories = []
    project_travel_categories = []
    for pocketsmith_category in pocketsmith_categories:
        colour = pocketsmith_category['colour']
        if colour in('#ff9800', '#9c27b0'):
            project_travel_categories.append(pocketsmith_category['title'].upper())
    for jira_category in jira_categories:
        if jira_category['summary'] not in project_travel_categories:
            new_pocketsmith_category = {
                'title': jira_category['summary'],
                'colour': jira_category['colour']
            }
            missing_pocketsmith_categories.append(new_pocketsmith_category)
    return missing_pocketsmith_categories