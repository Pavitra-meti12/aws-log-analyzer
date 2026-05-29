\# ☁️ Cloud-Based Automated Log Analyzer Using AWS



\## 📌 Project Overvie

This project is a \*\*serverless cloud-based log analysis system\*\* built using AWS services.  

It automatically processes log files uploaded to Amazon S3, analyzes logs using AWS Lambda, detects errors and warnings, generates structured reports, and sends real-time email alerts using Amazon SNS.



\---



\## 🎯 Problem Statement

Modern applications generate large volumes of log data. Manually analyzing these logs is:

\- Time-consuming

\- Error-prone

\- Not scalable



This project solves this problem by automating log monitoring and alerting using AWS cloud services.



\---



\## 🎯 Objectives

\- Automatically analyze uploaded log files

\- Detect ERROR, WARNING, FAIL, CRITICAL, EXCEPTION

\- Generate structured JSON reports

\- Send real-time email alerts

\- Store processed reports in S3

\- Monitor system using CloudWatch



\---



\## ☁️ AWS Services Used



| Service | Purpose |

|--------|--------|

| Amazon S3 | Store log files and reports |

| AWS Lambda | Process and analyze logs |

| Amazon SNS | Send email alerts |

| AWS IAM | Manage permissions securely |

| Amazon CloudWatch | Monitor logs and execution |



\---



\# ☁️ Cloud-Based Automated Log Analyzer Using AWS



\## 📌 Project Overview

This project is a \*\*serverless cloud-based log analysis system\*\* built using AWS services.

It automatically processes log files uploaded to Amazon S3, analyzes logs using AWS Lambda, detects errors and warnings, generates structured reports, and sends real-time email alerts using Amazon SNS.



\---



\## 🎯 Problem Statement

Modern applications generate large volumes of log data. Manually analyzing these logs is:

\- Time-consuming

\- Error-prone

\- Not scalable



This project solves this problem by automating log monitoring and alerting using AWS cloud services.



\---



\## 🎯 Objectives

\- Automatically analyze uploaded log files

\- Detect ERROR, WARNING, FAIL, CRITICAL, EXCEPTION

\- Generate structured JSON reports

\- Send real-time email alerts

\- Store processed reports in S3

\- Monitor system using CloudWatch



\---



\## ☁️ AWS Services Used



| Service | Purpose |

|--------|--------|

| Amazon S3 | Store log files and reports |

| AWS Lambda | Process and analyze logs |

| Amazon SNS | Send email alerts |

| AWS IAM | Manage permissions securely |

| Amazon CloudWatch | Monitor logs and execution |



\---



\## 🏗️ System ArcS3 (logs upload)

↓

Lambda Trigger

↓

Log Processing (Python)

↓

Error Detection

↓

JSON Report Generation

↓

Store in S3 (reports/)

↓

SNS Email Alert

↓

CloudWatch Monitoringhitecture





\---



\## ⚙️ Working Flow



1\. User uploads log file to S3 (`logs/`)

2\. S3 triggers AWS Lambda function

3\. Lambda reads and processes log file

4\. Detects errors, warnings, and critical issues

5\. Generates JSON report

6\. Stores report in S3 (`reports/`)

7\. Sends email alert using SNS

8\. CloudWatch monitors execution



\---



\## 🧠 Features



\- Fully automated log analysis

\- Real-time error detection

\- Email notification system

\- Serverless architecture

\- Scalable and cost-efficient

\- Easy maintenance



\---



\## 📂 Project Structure

aws-log-analyzer/

│

├── lambda\_function.py

├── README.md



\---



\## 📊 Sample Output



```json

{

\&#x20; "error\\\_count": 2,

\&#x20; "warning\\\_count": 1,

\&#x20; "severity": "MEDIUM",

\&#x20; "errors": \\\[

\&#x20;   "Database connection failed",

\&#x20;   "Timeout occurred"

\&#x20; ]

}



📧 Email Alert Example



Subject: Cloud Log Analyzer Alert



File: logs.txt

Severity: MEDIUM

Errors detected in log file.




\---



\## ⚙️ Working Flow



1\. User uploads log file to S3 (`logs/`)

2\. S3 triggers AWS Lambda function

3\. Lambda reads and processes log file

4\. Detects errors, warnings, and critical issues

5\. Generates JSON report

6\. Stores report in S3 (`reports/`)

7\. Sends email alert using SNS

8\. CloudWatch monitors execution



\---



\## 🧠 Features



\- Fully automated log analysis

\- Real-time error detection

\- Email notification system

\- Serverless architecture

\- Scalable and cost-efficient

\- Easy maintenance



\---



\## 📂 Project Structure

aws-log-analyzer/

│

├── lambda\_function.py

├── README.md



\---



\## 📊 Sample Output

{

&#x20; "error\_count": 2,

&#x20; "warning\_count": 1,

&#x20; "severity": "MEDIUM",

&#x20; "errors": \[

&#x20;   "Database connection failed",

&#x20;   "Timeout occurred"

&#x20; ]

}

📧 Email Alert Example



Subject: Cloud Log Analyzer Alert



File: logs.txt

Severity: MEDIUM

Errors detected in log file.



