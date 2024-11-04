from finance_workflow import finance_flow

if __name__ == "__main__":
    finance_flow.deploy(
        "finances-gcp-flow",
        work_pool_name="gcp-cloud-run-push",
        image="australia-southeast1-docker.pkg.dev/home-dashboard-396803/danieljsmith1510-repository/prefectimage:prefect2python3.10",
        build=False,
        cron="0 * * * *"
    )