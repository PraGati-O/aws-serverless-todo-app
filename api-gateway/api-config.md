# API Gateway Configuration

This API Gateway exposes REST endpoints for the serverless todo application.

## Endpoints

### GET /all
- Description: Fetch all pending todo items
- Integration: AWS Lambda (`get_all_todos`)

### POST /create
- Description: Create a new todo item
- Integration: AWS Lambda (`create_todo`)

### GET /markDone
- Description: Mark a todo item as completed
- Integration: AWS Lambda (`mark_done`)

## Deployment
- API is deployed using a REST API Gateway
- Stage name: dev
