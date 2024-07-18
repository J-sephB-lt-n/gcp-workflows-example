gcloud functions deploy JsonLogger \
  --gen2 \
  --runtime python312 \
  --project $GCP_PROJECT_ID \
  --region $GCP_REGION \
  --source=. \
  --entry-point=entrypoint_function \
  --trigger-http \
  --allow-unauthenticated \
  --timeout 60 \
  --min-instances 0 \
  --max-instances 1
