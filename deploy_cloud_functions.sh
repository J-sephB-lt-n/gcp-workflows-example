cd cloud_functions/run_query_bigquery/
echo 'deploying cloud function [RunQueryBigQuery]'
source deploy_cloud_function.sh
cd ../../cloud_functions/json_logger/
echo 'deploying cloud function [JsonLogger]'
source deploy_cloud_function.sh
cd ../..
