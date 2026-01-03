# AWS Serverless Todo Application

## Overview
This project is a serverless Todo application built using AWS services.
It demonstrates how to design and deploy a backend without managing servers.

## Architecture
Frontend (S3 Static Website)  
→ API Gateway  
→ AWS Lambda  
→ DynamoDB  

## AWS Services Used
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3 (Static Website Hosting)

## Features
- Create a new todo item
- Fetch all todo items
- Mark a todo as completed

## Project Structure
This repository contains:
- Lambda function source code
- DynamoDB table schema
- API Gateway configuration details
- Frontend build files
- Architecture documentation

## How to Use
1. Frontend is hosted on S3
2. API Gateway exposes REST endpoints
3. Lambda functions handle requests
4. DynamoDB stores todo data

## Author
Pragati Ojha 
