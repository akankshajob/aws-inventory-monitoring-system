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
## Technology Stack

### Backend

- Python
- Django

### Frontend

- HTML
- CSS
- Bootstrap

### Database

- MySQL
- Amazon RDS

### AWS Services

- Amazon EC2
- Amazon RDS
- AWS Lambda
- Amazon EventBridge
- Amazon SNS
- Amazon CloudWatch
- AWS IAM

### Deployment

- Ubuntu Linux
- Gunicorn
- Nginx
- Git
- GitHub

---

## Project Workflow

1. Users log in to the application.
2. Administrators manage products and configure stock thresholds.
3. Warehouse managers update product quantities.
4. Inventory data is stored in Amazon RDS.
5. Amazon EventBridge triggers AWS Lambda on a schedule.
6. Lambda compares current stock with configured thresholds.
7. If stock falls below the threshold, Amazon SNS sends an email notification.
8. CloudWatch records execution logs for monitoring and troubleshooting.

---

## Application Screenshots

### Admin Login

![Admin Login](assets/admin%20login.png)

---

### Admin Dashboard

![Admin Dashboard](assets/admin%20dashboard.png)

---

### Add Product

![Add Product](assets/admin%20add%20product.png)

---

### Alert History

![Alert History](assets/admin%20alert%20history.png)

---

### Manager Login

![Manager Login](assets/manager%20login.png)

---

### Manager Dashboard

![Manager Dashboard](assets/manager%20-dashboard.png)

---

### Update Stock

![Update Stock](assets/manager-update%20stock.png)

---

### Manager Alert History

![Manager Alert History](assets/manager%20alert%20history.png)

---

## Repository Structure

```
aws-inventory-monitoring-system
│
├── assets/
│   ├── admin login.png
│   ├── admin dashboard.png
│   ├── admin add product.png
│   ├── admin alert history.png
│   ├── manager login.png
│   ├── manager -dashboard.png
│   ├── manager-update stock.png
│   └── manager alert history.png
│
├── docs/
│   └── aws-architecture.png
│
├── inventory/
├── inventory_project/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/akankshajob/aws-inventory-monitoring-system.git
```

Move into the project directory

```bash
cd aws-inventory-monitoring-system
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Start the development server

```bash
python manage.py runserver
```

---

## Future Enhancements

- Multi-warehouse inventory support
- Inventory analytics dashboard
- Barcode and QR code integration
- REST API
- Docker containerization
- CI/CD using GitHub Actions

---

## Skills Demonstrated

- Cloud Deployment
- Serverless Computing
- AWS Service Integration
- Django Web Development
- MySQL Database Management
- Cloud Monitoring
- Cloud Security
- IAM Configuration
- Role-Based Access Control
- Git Version Control

---

## Acknowledgement

Developed as a cloud computing project demonstrating real-world inventory automation using Django and AWS.