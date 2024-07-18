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

# update rows in YAML file to use your cloud function URIs #
sed -i -e "4s@url: .*@url: ${RUN_QUERY_BIGQUERY_URI}@1" gcp_workflow.yaml
sed -i -e "9s@url: .*@url: ${JSON_LOGGER_URI}@1" gcp_workflow.yaml

# deploy the GCP workflow #
gcloud workflows deploy example-workflow \
    --source gcp_workflow.yaml \
    --project $GCP_PROJECT_ID \
    --location $GCP_REGION \
    --description 'An example workflow illustrating basic functionality of Google Workflows'

# run the GCP workflow #
gcloud workflows run example-workflow

# clean up #
source delete_cloud_functions.sh
source delete_gcp_workflow.sh

```
