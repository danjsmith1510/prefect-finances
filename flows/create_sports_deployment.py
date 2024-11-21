from nba_main_workflow import nba_main_workflow
from nba_odds_workflow import nba_odds_workflow

if __name__ == "__main__":
    nba_main_workflow.deploy(
        "nba-main-workflow",
        work_pool_name="gcp-cloud-run-push",
        image="australia-southeast1-docker.pkg.dev/home-dashboard-396803/danieljsmith1510-repository/prefectimage:prefect2python3.10",
        build=False,
        cron="0 21 * * *"
    )

    nba_odds_workflow.deploy(
        "nba-odds-workflow",
        work_pool_name="gcp-cloud-run-push",
        image="australia-southeast1-docker.pkg.dev/home-dashboard-396803/danieljsmith1510-repository/prefectimage:prefect2python3.10",
        build=False,
        cron="0 8 * * *"
    )