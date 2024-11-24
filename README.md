# AWS Web Application Deployment: End-to-End Guide

## Overview
This project provides a complete guide for deploying a web application on AWS infrastructure. The deployment process includes setting up an EC2 instance, integrating it with an Amazon RDS database, and deploying a website accessible via the EC2's public IP.

---

## Steps for Deployment

### 1. Create a Database using RDS (mysql)
![image](https://github.com/user-attachments/assets/44515eda-cd34-4e68-8416-def95a5a3398)



### 1. Create a Bucket
Set up an S3 bucket as part of the deployment infrastructure. This step may involve storing configuration files or static assets.

![Create Bucket](./path-to-image-create-bucket.png)

---

### 2. Set Up an EC2 Instance
Launch an Ubuntu-based EC2 instance:
- Go to the AWS Management Console.
- Choose Ubuntu as the operating system.
- Configure security groups to allow SSH, HTTP, and HTTPS traffic.

![EC2 Instance Setup](./path-to-image-ec2.png)

---

### 3. Connect to EC2 with Ubuntu
Use SSH to connect to the EC2 instance:
```bash
ssh -i "your-key.pem" ubuntu@<ec2-public-ip>
