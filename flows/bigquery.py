from prefect import task
from datetime import datetime, timezone
from prefect_gcp.bigquery import GcpCredentials, BigQueryWarehouse

gcp_credentials = GcpCredentials.load("gcp-credentials-home-dashboard")

@task(retries=2)
def load_finances_extract_table(extract_type: str, extract_data: str, timestamp: str):
    """Load API data to finance extracts table"""
    with BigQueryWarehouse(gcp_credentials=gcp_credentials) as warehouse:
         warehouse.execute(
            """
            INSERT INTO finances.extracts (timestamp, extract_type, extract_data) 
            VALUES (%(timestamp)s, %(extract_type)s, %(extract_data:string)s);
            """,
            parameters={"timestamp": timestamp, "extract_type": extract_type, "extract_data": extract_data}        
        )
    return True

@task(retries=2)
def run_finance_merge_extracts(start_date, end_date):
    """Merge new finance extracts data into main tables"""
    with BigQueryWarehouse(gcp_credentials=gcp_credentials) as warehouse:
        warehouse.execute(
            "CALL finances.usp_merge_extracts('" + str(start_date) + "', '" + str(end_date) + "');"
        )
    return True

@task(retries=2)
def load_sports_extract_table(extract_type: str, extract_data: str, timestamp: str):
    """Load data to sports extracts table"""
    with BigQueryWarehouse(gcp_credentials=gcp_credentials) as warehouse:
         warehouse.execute(
            """
            INSERT INTO home-dashboard-396803.bronze.extracts (timestamp, extract_type, extract_data) 
            VALUES (%(timestamp)s, %(extract_type)s, %(extract_data:string)s);
            """,
            parameters={"timestamp": timestamp, "extract_type": extract_type, "extract_data": extract_data}        
        )
    return True

@task(retries=2)
def run_sports_merge_main_extracts(run_date):
    """Merge main sports extracts data into tables"""
    with BigQueryWarehouse(gcp_credentials=gcp_credentials) as warehouse:
        warehouse.execute(
            "CALL bronze.usp_merge_main_extracts('" + str(run_date.strftime('%Y-%m-%d')) + "');"
        )
    return True

@task(retries=2)
def run_sports_merge_performance_prediction(run_date):
    with BigQueryWarehouse(gcp_credentials=gcp_credentials) as warehouse:
        warehouse.execute(
            "CALL silver.usp_merge_playerperformanceprediction('" + str(run_date.strftime('%Y-%m-%d')) + "');"
        )
    return True

@task(retries=2)
def run_sports_merge_odds_extracts():
    """Merge odds sports extracts data into tables"""
    with BigQueryWarehouse(gcp_credentials=gcp_credentials) as warehouse:
        warehouse.execute(
            "CALL bronze.usp_merge_odds_extracts();"
        )
    return True