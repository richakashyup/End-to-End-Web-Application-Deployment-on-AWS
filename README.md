# AWS Web Application Deployment: End-to-End Guide

## Overview
This project provides a complete guide for deploying a web application on AWS infrastructure. The deployment process includes setting up an EC2 instance, integrating it with an Amazon RDS database, and deploying a website accessible via the EC2's public IP.

---

## Steps for Deployment

### 1. Create a Database using RDS (mysql)
![image](https://github.com/user-attachments/assets/44515eda-cd34-4e68-8416-def95a5a3398)
![image](https://github.com/user-attachments/assets/38ba1943-1ed5-4bad-aa66-d13e4a685fb8)
![image](https://github.com/user-attachments/assets/ea73dbb7-a050-4f66-b4c4-f0a080602b56)
![image](https://github.com/user-attachments/assets/2ef547d0-4379-4abf-8f73-15400f83ec14)
![image](https://github.com/user-attachments/assets/cb7fdda2-d9f2-495b-9186-d7ab11d30990)
![image](https://github.com/user-attachments/assets/10dd7e9d-4eb0-44dc-b67c-ef0d2e5925e8)
![image](https://github.com/user-attachments/assets/b251a322-fbd3-4a8e-815f-965484469280)
![image](https://github.com/user-attachments/assets/cc523b34-fabd-4390-bbd5-e051d98972d3)


### 2. Create a Bucket
![image](https://github.com/user-attachments/assets/9b56141d-419e-4b3f-aae6-41756d3f7caf)
![image](https://github.com/user-attachments/assets/d328ef68-63fa-4766-8f83-178415429feb)
![image](https://github.com/user-attachments/assets/e8c009c7-edb5-47f1-a47d-f52c8963934d)


### 3. Set Up an EC2 Instance
Launch an Ubuntu-based EC2 instance:
![image](https://github.com/user-attachments/assets/be105574-b364-4da1-a554-5bfb93fb92f2)
![image](https://github.com/user-attachments/assets/5003a808-55f5-474e-82a1-c3fb78aa3372)
![image](https://github.com/user-attachments/assets/6f4f2451-b416-4d76-ae5e-468d8546fe62)
![image](https://github.com/user-attachments/assets/ae0e0cc3-0004-4243-a006-b08a42713dd2)
![image](https://github.com/user-attachments/assets/10aaa133-0205-48e9-9ef9-44a65ef5668b)

- Configure security groups to allow SSH, HTTP, and HTTPS traffic.
![image](https://github.com/user-attachments/assets/39c524f2-c100-4b54-8847-9922b98a57f8)


### 3. Connect to EC2 with Ubuntu
Use SSH to connect to the EC2 instance:
```bash
ssh -i "your-key.pem" ubuntu@<ec2-public-ip>
```
![image](https://github.com/user-attachments/assets/ba382744-1183-4bb2-9814-8534e8bb438e)

Install mysql on ubuntu
![image](https://github.com/user-attachments/assets/028fe184-2855-49b7-8b2a-26bcace327e9)

Connect to RDS
![image](https://github.com/user-attachments/assets/fb31ff13-89ab-44ac-9e8a-f391bddca576)
![image](https://github.com/user-attachments/assets/d1cac1f1-0efa-4045-9db6-b0c07d782f4c)

Deploy on the local machine to check
![image](https://github.com/user-attachments/assets/fe49374a-bf20-4a66-9f3c-d3f623a7456c)

Push it on git hub
Again connect to ubuntu

Create an IAM role
![image](https://github.com/user-attachments/assets/612357ad-9baa-4ea4-8f51-171f52c1b691)
![image](https://github.com/user-attachments/assets/8cef9761-d01d-4f14-a468-a8af710d6ce6)
![image](https://github.com/user-attachments/assets/a07fb2d4-e209-4052-9e1f-570f6f8cb34a)
![image](https://github.com/user-attachments/assets/abde2833-c97f-4829-bf63-5bd35673482f)
![image](https://github.com/user-attachments/assets/eaeacf9f-1f21-4c2e-8f95-e238df0cc462)
![image](https://github.com/user-attachments/assets/3d3068a5-d5f2-4595-af9d-5c52efdd44b2)

Deploy website on ubuntu
![image](https://github.com/user-attachments/assets/6bfdee9d-b00a-4a6f-b111-26cc5b382273)

Browse pubic ip of EC2
![image](https://github.com/user-attachments/assets/8a356b19-c6db-434d-a60b-c3614897f0c9)

Add info on it
![image](https://github.com/user-attachments/assets/c05e03db-4529-41f4-b461-12c201659324)

And click update database
![image](https://github.com/user-attachments/assets/87ab3d82-5303-4c37-94c8-2310dd9ff8a5)
![image](https://github.com/user-attachments/assets/45ee919d-bc62-4f7f-80c7-6627ca52bcee)
![image](https://github.com/user-attachments/assets/fa052040-31c2-4faf-a42d-3874891cf34e)















