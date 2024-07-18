"""Cloud function endpoint which receives JSON and logs it to google cloud logging"""

import json
import logging

import functions_framework

# set up python logger #
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@functions_framework.http
def entrypoint_function(request) -> tuple[str, int]:
    """Writes received JSON body to google cloud logging"""
    input_json = request.get_json()
    logger.info(json.dumps(input_json, indent=4, default=str))
    return ("OK", 200)
