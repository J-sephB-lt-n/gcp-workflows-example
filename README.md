# gcp-workflows-example

```bash
# deploy the cloud functions #
GCP_PROJECT_ID='your-gcp-proj-id'
GCP_REGION='europe-west2'
source deploy_cloud_functions.sh

# test out the cloud functions #
# (these URIs are shown in terminal when the functions are deployed)
RUN_QUERY_BIGQUERY_URI='https://put-your-cloud-function-uri-here'
JSON_LOGGER_URI='https://put-your-cloud-function-uri-here'
curl -m 30 -X POST $RUN_QUERY_BIGQUERY_URI \
    -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
    -H "Content-Type: application/json" \
    -d '{"query_string":"SELECT * FROM `projname.datasetname.tablename` LIMIT 69;"}'
# you will need to check GCP log explorer to see that this cloud function worked:
curl -m 30 -X POST $JSON_LOGGER_URI \
    -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
    -H "Content-Type: application/json" \
    -d '[{"id": 1, "status":"BAD"}, {"id": 2, "status": "GOOD"}]'

# clean up #
source delete_cloud_functions.sh

```
