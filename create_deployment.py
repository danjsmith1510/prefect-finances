from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/prefecthq/demos.git",
        entrypoint="pocketsmith.py:get_pocketsmith_data",
    ).deploy(
        name="get-pocketsmith-data",
        work_pool_name="my-managed-pool",
        cron="0 1 * * *",
    )