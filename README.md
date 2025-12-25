# Serverless Event Registration System

A fully serverless backend application built using AWS.

## AWS Services Used
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- AWS IAM
- Amazon CloudWatch

## Features
- Register users for events
- Retrieve registered users
- Pay-as-you-go serverless architecture

## API Endpoints

### POST /events
Registers a user for an event.

Request Body:
```json
{
  "eventId": "AWS_EVENT_01",
  "name": "Priyanka",
  "email": "priyanka@gmail.com"
}

