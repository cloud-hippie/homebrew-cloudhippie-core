import base64
import json
import boto3
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

HOMEBREW_BUCKET = 'homebrew-bottles'




def lambda_handler(event, context):
    """This lambda works as an s3 proxy for homebrew"""
    logger.info("Event: {}".format(event))
    logger.info("Context: {}".format(context))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    s3_client = boto3.client('s3')
    result = s3_client.get_object(Bucket=bucket, Key=key)
    logger.info("Result: {}".format(result))

    if result['ResponseMetadata']['HTTPStatusCode'] != 200:
        return {
            'headers': { "Content-Type": "text/plain" },
            'statusCode': 404,
            'body': "Not Found",
            'isBase64Encoded': False
        }
    
    return {
            'headers': { "Content-Type": "image/png" },
            'statusCode': 200,
            'body': base64.b64encode(result).decode('utf-8'),
            'isBase64Encoded': True
    }
