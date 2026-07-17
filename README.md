# AWS Inventory Monitoring System

A cloud-based inventory monitoring system built with Django and deployed on AWS to automate inventory management, monitor stock levels, and generate low-stock alerts.

## Features

- Secure User Authentication
- Inventory Management (CRUD)
- Product Stock Monitoring
- Low Stock Threshold Alerts
- Automated Email Notifications
- Role-Based Access
- Alert History
- Cloud Deployment on AWS

## Tech Stack

### Backend
- Python
- Django

### Frontend
- HTML
- CSS
- Bootstrap

### Database
- Amazon RDS (MySQL)

### AWS Services
- Amazon EC2
- Amazon RDS
- AWS Lambda
- Amazon SNS
- Amazon CloudWatch
- AWS IAM

## Project Workflow

1. User logs into the application.
2. Products are managed through the dashboard.
3. Inventory data is stored in Amazon RDS.
4. AWS Lambda periodically checks stock levels.
5. Low-stock products trigger email notifications through Amazon SNS.
6. CloudWatch logs monitor the execution of background tasks.

## Future Improvements

- Dashboard Analytics
- Barcode/QR Code Support
- REST API
- Docker Deployment
- CI/CD Pipeline

---
Developed as a cloud computing project demonstrating real-world inventory automation using Django and AWS.