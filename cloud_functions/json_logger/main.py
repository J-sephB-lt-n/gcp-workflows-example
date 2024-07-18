"""Cloud function endpoint which receives JSON and logs it to google cloud logging"""

import datetime
import json
import logging

import functions_framework
import google.cloud.logging

gcp_logging_client = google.cloud.logging.Client()
gcp_logging_client.setup_logging()

# set up python logger #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@functions_framework.http
def entrypoint_function(request) -> tuple[str, int, str]:
    """Writes received JSON body to google cloud logging"""
    input_json = request.get_json()
    logger.info(json.dumps(input_json, indent=4, default=str))
    return (
        f'{{"completed_at_utc": "{datetime.datetime.now(tz=datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S")}"}}',
        200,
        "application/json",
    )
