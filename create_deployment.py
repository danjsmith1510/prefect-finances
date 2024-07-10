from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/danjsmith1510/prefect-finances.git",
        entrypoint="finance_workflow.py:finance_workflow",
    ).deploy(
        name="finance_workflow",
        work_pool_name="my-managed-pool",
        cron="0 1 * * *",
    )