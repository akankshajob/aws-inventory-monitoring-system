# AWS Inventory Monitoring System


A cloud-hosted inventory management system developed for automate stock monitoring and inventory management using **Django** and **Amazon Web Services (AWS)**.

The application enables administrators and warehouse managers to manage inventory through a secure web interface while automatically monitoring stock levels. 
A scheduled AWS Lambda function checks inventory against configured thresholds and sends email notifications using Amazon SNS whenever products fall below their minimum stock level.

---

## Architecture

![AWS Architecture](docs/aws-architecture.png)

---

## Project Highlights

- Cloud deployment using Amazon EC2
- Managed MySQL database with Amazon RDS
- Automated inventory monitoring using AWS Lambda
- Scheduled background execution with Amazon EventBridge
- Email notifications through Amazon SNS
- CloudWatch logging for monitoring Lambda execution
- Role-Based Access Control (Admin & Warehouse Manager)
- Secure cloud configuration using AWS IAM

---

## Features

### Administrator

- Secure login
- Dashboard overview
- Add, edit and delete products
- Configure minimum stock thresholds
- View alert history
- Manage inventory records

### Warehouse Manager

- Secure login
- Dashboard overview
- Update stock quantities
- View alert history
- Monitor available inventory

### Automated Monitoring

- Scheduled inventory checks
- Low-stock detection
- Automatic email notifications
- Alert history logging

---



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