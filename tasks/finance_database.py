import json
from prefect import task
from datetime import datetime
from prefect_gcp.bigquery import GcpCredentials, BigQueryWarehouse

gcp_credentials = GcpCredentials.load("gcp-credentials-home-dashboard")

@task(retries=2)
def load_extract_table(extract_type: str, extract_data: str):
    """Load API data to extracts table"""
    # gcp_credentials = GcpCredentials.load("gcp-credentials-home-dashboard")
    timestamp = datetime.now().isoformat()
    with BigQueryWarehouse(gcp_credentials=gcp_credentials) as warehouse:
        response = warehouse.execute(
            """
            INSERT INTO home-dashboard-396803.finances.extracts (timestamp, extract_type, extract_data) 
            VALUES (%(timestamp)s, %(extract_type)s, %(extract_data:string)s);
            """,
            parameters={"timestamp": timestamp, "extract_type": extract_type, "extract_data": extract_data}        
        )
    return True

@task(retries=2)
def run_merge_extracts(start_date, end_date):
    """Merge new extracts data into main tables"""
    # gcp_credentials = GcpCredentials.load("gcp-credentials-home-dashboard")
    with BigQueryWarehouse(gcp_credentials=gcp_credentials) as warehouse:
        response = warehouse.execute(
            "CALL finances.usp_merge_extracts('" + str(start_date) + "', '" + str(end_date) + "');"
        )
    print (response)
    return True