import json

import functions_framework
import google.cloud.bigquery

bigquery_client = google.cloud.bigquery.Client()


@functions_framework.http
def run_bigquery_query(query_str: str) -> tuple[str, int, dict[str, str]]:
    """Runs the query in BigQuery, returning the
    result as JSON (a list of dicts)"""
    result_rows: list[dict] = [
        dict(zip(row.keys(), row.values()))
        for row in bigquery_client.query(query_str).result()
    ]
    return (json.dumps(result_rows), 200, {"Content-Type": "application/json"})
