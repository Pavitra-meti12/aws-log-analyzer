import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    
    try:
        # Get S3 details
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']
        
        # Read file
        file = s3.get_object(Bucket=bucket, Key=key)
        content = file['Body'].read().decode('utf-8')
        
        errors = []
        warnings = []
        
        # ✅ SMART LOG ANALYSIS
        error_keywords = ["ERROR", "FAIL", "CRITICAL", "EXCEPTION"]
        warning_keywords = ["WARNING", "WARN"]
        
        for line in content.split("\n"):
            line = line.strip()
            upper_line = line.upper()
            
            if any(word in upper_line for word in error_keywords):
                errors.append(line)
            elif any(word in upper_line for word in warning_keywords):
                warnings.append(line)
        
        # ✅ SEVERITY CLASSIFICATION
        severity = "LOW"
        if len(errors) >= 3:
            severity = "HIGH"
        elif len(errors) > 0:
            severity = "MEDIUM"
        
        print("Errors:", errors)
        print("Warnings:", warnings)
        
        # ✅ REPORT GENERATION
        report = {
            "file": key,
            "error_count": len(errors),
            "warning_count": len(warnings),
            "severity": severity,
            "errors": errors,
            "warnings": warnings
        }
        
        print("Final Report:", report)
        
        # ✅ SAVE REPORT TO S3
        report_json = json.dumps(report, indent=2)
        
        s3.put_object(
            Bucket=bucket,
            Key=f"reports/report_{context.aws_request_id}.json",
            Body=report_json
        )
        
        # ✅ SMART EMAIL ALERT
        if len(errors) > 0:
            message = f"""
🚨 Log Analyzer Alert 🚨

File: {key}
Severity: {severity}
Error Count: {len(errors)}
Warning Count: {len(warnings)}

Errors:
{chr(10).join(errors)}

Warnings:
{chr(10).join(warnings)}
"""
            sns.publish(
                TopicArn='arn:aws:sns:ap-south-1:785379201908:loganalyzer-alerts',
                Message=message,
                Subject=f'Log Alert - {severity}'
            )
        
        return {
            'statusCode': 200,
            'body': json.dumps(report)
        }

    except Exception as e:
        print("Error occurred:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing log file')
        }