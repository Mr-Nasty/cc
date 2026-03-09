import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    length = event['length']
    width = event['width']
    area = calculateArea(length, width)

    data = {
        "length": length,
        "width": width
    }

    return json.dumps(data)

def calculateArea(length, width):
    return length * width

#{
#  "length":23
#  'width": 45
#}
