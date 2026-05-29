
import json
import boto3

# ✅ FIX: Add region (IMPORTANT for Jenkins + local run)
REGION = "us-east-1"   # change to "ap-south-1" if your AWS is Mumbai

s3 = boto3.client('s3', region_name=REGION)
sns = boto3.client('sns', region_name=REGION)

# ✅ Your SNS Topic ARN (KEEP YOURS OR UPDATE)
TOPIC_ARN = "arn:aws:sns:us-east-1:785379201908:loganalyzer-alerts"


def lambda_handler(event, context):
    print("Lambda started")

    try:
        # Get bucket and file info from S3 event
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        print("Bucket:", bucket)
        print("Key:", key)

        # Read file from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        content = response['Body'].read().decode('utf-8')

        # Counters
        errors = []
        warnings = []
        criticals = []
        fails = []
        exceptions = []

        # Analyze logs
        for line in content.splitlines():
            line = line.strip()

            if "ERROR" in line:
                errors.append(line)
            elif "WARNING" in line:
                warnings.append(line)
            elif "CRITICAL" in line:
                criticals.append(line)
            elif "FAIL" in line:
                fails.append(line)
            elif "EXCEPTION" in line:
                exceptions.append(line)

        total_issues = len(errors) + len(criticals) + len(fails) + len(exceptions)

        # Severity
        if total_issues >= 4:
            severity = "HIGH"
        elif total_issues >= 2:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        # Final report
        report = {
            "file": key,
            "error_count": len(errors),
            "warning_count": len(warnings),
            "critical_count": len(criticals),
            "fail_count": len(fails),
            "exception_count": len(exceptions),
            "severity": severity
        }

        print("Report:", report)

        # Save report to S3 (reports folder)
        report_key = f"reports/report_{context.aws_request_id}.json"

        s3.put_object(
            Bucket=bucket,
            Key=report_key,
            Body=json.dumps(report, indent=2)
        )

        print("Report saved to:", report_key)

        # Send SNS alert
        if total_issues > 0:
            message = f"""
AWS Log Analyzer Alert

File: {key}
Severity: {severity}

Errors: {len(errors)}
Warnings: {len(warnings)}
Criticals: {len(criticals)}
Fails: {len(fails)}
Exceptions: {len(exceptions)}
"""

            sns.publish(
                TopicArn=TOPIC_ARN,
                Message=message,
                Subject="Log Analyzer Alert"
            )

            print("SNS ALERT SENT")

        return {
            "statusCode": 200,
            "body": json.dumps(report)
        }

    except Exception as e:
        print("Error:", str(e))

        return {
            "statusCode": 500,
            "body": json.dumps(str(e))
        }