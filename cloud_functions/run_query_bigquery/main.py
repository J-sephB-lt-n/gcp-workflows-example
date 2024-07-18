"""Cloud function endpoint which runs a query on BigQuery and returns the results as JSON"""

import json

import functions_framework
import google.cloud.bigquery

bigquery_client = google.cloud.bigquery.Client()


@functions_framework.http
def entrypoint_function(request) -> tuple[str, int, dict[str, str]]:
    """Runs the query in BigQuery, returning the
    result as JSON (a list of dicts)"""
    query_str: str = request.get_json()["query_string"]
    result_rows: list[dict] = [
        dict(zip(row.keys(), row.values()))
        for row in bigquery_client.query(query_str).result()
    ]
    return (
        json.dumps({"query_result": result_rows}),
        200,
        {"Content-Type": "application/json"},
    )
