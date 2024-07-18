echo 'deleting GCP workflow [example-workflow]'
gcloud workflows delete example-workflow \
  --project $GCP_PROJECT_ID \
  --location $GCP_REGION

echo 'deleting cloud function [RunQueryBigquery]'
gcloud functions delete RunQueryBigquery \
  --project $GCP_PROJECT_ID \
  --region $GCP_REGION
echo 'deleting cloud function [JsonLogger]'
gcloud functions delete JsonLogger \
  --project $GCP_PROJECT_ID \
  --region $GCP_REGION
