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

    errors = []
    warnings = []

    for line in content.splitlines():

        if "ERROR" in line:
            errors.append(line)

        elif "WARNING" in line:
            warnings.append(line)

    report = {
        "file": key,
        "error_count": len(errors),
        "warning_count": len(warnings)
    }

    # Save report to S3
    report_key = f"reports/report_{context.aws_request_id}.json"

    s3.put_object(
        Bucket=bucket,
        Key=report_key,
        Body=json.dumps(report, indent=2)
    )

    return {
        "statusCode": 200,
        "body": json.dumps(report)
    }