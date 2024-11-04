from prefect_gcp import GcpCredentials

service_account_info = {
  "type": "service_account",
  "project_id": "home-dashboard-396803",
  "private_key_id": "f2bcc96cd11be6679e689f9b0ff3c671b4723687",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC41kyP5znc9ShC\n2CIDGDfs6A+MHOejaABNRMOpG3Dm17ly0LiOGdD1peh6662PT8uZCokZ2QYQsvAK\nib9wiW03AFNAX7IXYgFJ8mqrB6QoIw1/1oWNaK0Cvh2gSw4ZoWs1ZQSqH+yLRO88\nFNjhkshDvuLWIGHX8+i2rRqsWqol963T3daWoaqVQiquE+WU2+BnJ1Ae2ndSLQA4\n/fEztTfbqT2ZUxIUnfGcLWF+bB6O70GKdPaMq0oJ1nNuPDLy7uHObwGpbojeueom\nBEMjpvmqbjT40mW759M8E/7W79W4uzqxBomkvXOvoFKuAbzFCQt5673gvm81tU1p\no3ggTW2ZAgMBAAECggEABywRlnfjb+Z3ZHicgUA8U04B5G7ushGECXuEmBg/fkWa\npZDhyGnKCO4iIjro5imzfcHB5iXcrWM0G0STEBvVCBBUKqhL8cpUwHjOmMpYHVKW\n4IIDdqQ8KmIUJjcjWe1AirbbwnowpIrNOaiZbc9TRAWxKZviEA4f1o7K/SsbdROh\nYlJ46FjnELNaakldU87JMWe3bgo2iNiXVIilgr5D8kaEQipwFes6iYmqAdAcSdw4\ngHQF999hoMUDhIzJ2fCqA2hDhVgNXi13pYEOBmkClGQ32fqgqf1YOTcLaaGlaA/0\nP4I0AGfONj9Ayyrh7Q7prl9z6TyNkORJiSCGd9gLnQKBgQDbIdB0IcQeQGvFljOO\nZD7g//SVeEtnsjMx1Tdvh5JWK7NSNoWw0+U5EwrTmAfmp45N24e/SeHzMcJLFXqd\ns6mC1mVXCFDAOL6+y+9rN5maLxOcAYCnp1O87FQsP+5KaxAvlYCP8PK7ScGEYj1/\nrS06TvMny8H9tnARWLoNmGLwqwKBgQDX71+1Uykb0u7YfuHjtK3PKeZwYbzOsBHy\n63qZFsRI0W/GePrbU+rok/yl6WZSe7Z70egKEjqkPjFSkhs8/Pqt/Io6ON3jZy45\n2dwdIpxsh0DNSzqGJbD1Ip9x4UshBtykR0TKoPx9MxYrXzpp/0/QO6skwrF3Fv4e\noRAdFGXCywKBgE993r6iGSDYQcA1kpJO7zhz4WfvcXs2e7fSHwAIcB9uTui9+pWA\n6KBhtgW4GvWjRs4bmwzbYmn0XQUbz5UxvYZG/BAsZg61BwzzsfB1BPWXqkdnjCJF\nYu0f1hEPSAQa/o4kb7THtWYXhWnesWyFh+ilBzQiiEbfTZwdUbDo3MttAoGAdaZD\nVCzyGenMHoLLGmBnzpZ6qkJmN4qwzNTF4EEKQs5xgwaJTxSiyYNPxSmsiUZEP6Q3\nM72I29HS17UpSAphnogY2+393xdplTWA+xLPfUYX5YKWaV6B0p3Bl69zWpQ9hPgb\nn/ckeiZqbskcr4Hef4rzDT1SqZsKa6+/csiZRQ8CgYEAiw5TOLgSVGVmka3Uet4a\nPJw/7AP+MlgxwhbRRTniHPWrFthBKQULSyipqUXgpfcU3CwmXgFY9NXZ8JOKum2z\n40ZufOB0UAimNZuS8LLAacUV0h4lDMrHW1k316fRS1wv+kOnV18AqA9CvC2At7jZ\n9yDuFgHzKp3y2YEOX2tsZ2o=\n-----END PRIVATE KEY-----\n",
  "client_email": "sa-bigquery@home-dashboard-396803.iam.gserviceaccount.com",
  "client_id": "111751702813207283255",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/sa-bigquery%40home-dashboard-396803.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

GcpCredentials(
    service_account_info=service_account_info
).save("gcp-credentials-home-dashboard")

# docker build -t australia-southeast1-docker.pkg.dev/home-dashboard-396803/danieljsmith1510-repository/prefectimage:prefect2python3.10 .
# docker push australia-southeast1-docker.pkg.dev/home-dashboard-396803/danieljsmith1510-repository/prefectimage:prefect2python3.10
