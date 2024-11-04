FROM prefecthq/prefect:2-python3.10

# Add our requirements.txt file to the image and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt --trusted-host pypi.python.org --no-cache-dir
ADD flows /opt/prefect/flows

# docker build -t australia-southeast1-docker.pkg.dev/home-dashboard-396803/danieljsmith1510-repository/prefectimage:prefect2python3.10 .
# docker push australia-southeast1-docker.pkg.dev/home-dashboard-396803/danieljsmith1510-repository/prefectimage:prefect2python3.10