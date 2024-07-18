# gcp-workflows-example

```bash
# deploy the cloud functions #
GCP_PROJECT_ID='your-gcp-proj-id'
GCP_REGION='europe-west2'
source deploy_cloud_functions.sh

# test out the cloud functions #
RUN_QUERY_BIGQUERY_URI='https://put-your-cloud-function-uri-here'

curl -m 30 -X POST $RUN_QUERY_BIGQUERY_URI \
    -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
    -H "Content-Type: application/json" \
    -d '{"query_string":"SELECT * FROM `projname.datasetname.tablename` LIMIT 69;"}'


# clean up #
source delete_cloud_functions.sh

```

