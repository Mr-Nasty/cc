import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):

    # Get values from event
    length = event["length"]
    width = event["width"]

    # Calculate area
    area = calculate_area(length, width)

    # Log information
    logger.info("Length: %s, Width: %s", length, width)
    logger.info("Area calculated: %s", area)

    # Response
    response = {
        "length": length,
        "width": width,
        "area": area
    }

    return response


def calculate_area(length, width):
    return length * width

#{
#  "length": 23,
#  "width": 45
#}
