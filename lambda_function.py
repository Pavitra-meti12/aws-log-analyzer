import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):

    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    response = s3.get_object(
        Bucket=bucket,
        Key=key
    )

    content = response['Body'].read().decode('utf-8')

    error_count = 0

    for line in content.splitlines():
        if "ERROR" in line:
            error_count += 1

    report = {
        "file": key,
        "error_count": error_count
    }

    return {
        "statusCode": 200,
        "body": json.dumps(report)
    }