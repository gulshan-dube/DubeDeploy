# 🚀 DubeDeploy – Automated AWS Lambda Deployment with SAM & GitHub Actions

DubeDeploy is a fully automated deployment pipeline for AWS Lambda using the Serverless Application Model (SAM) and GitHub Actions.  
It allows you to write a simple Python function, push your code to GitHub, and automatically deploy it to AWS — no manual steps required.

---

## 🧠 Real-World Analogy (For Non-Tech Folks)

Imagine you write a note and drop it into a mailbox.  
Without doing anything else, that note gets picked up, sorted, and delivered to the right person — automatically.

DubeDeploy works the same way:  
You write code, push it to GitHub, and it gets deployed to AWS Lambda without lifting a finger.

---

## 📚 Table of Contents

- Real-World Analogy
- Tech Stack
- Folder Structure
- How It Works
- Lambda Function Code
- GitHub Actions Workflow
- SAM Commands
- Deployment Output
- Testing
- Final Notes

---

## 🛠️ Tech Stack

| Service           | Purpose                                  |
|-------------------|------------------------------------------|
| AWS Lambda        | Runs the Python function                 |
| AWS API Gateway   | Exposes the function via HTTP            |
| AWS S3            | Stores deployment packages               |
| AWS SAM           | Manages packaging and deployment         |
| GitHub Actions    | Automates deployment on code push        |
| IAM Roles         | Grants secure access between services    |

---

## 📁 Folder Structure



---

## ⚙️ How It Works

1. You write a Lambda function in Python.
2. You push your code to GitHub.
3. GitHub Actions runs a workflow:
   - Packages the app using SAM
   - Uploads it to S3
   - Deploys it to AWS Lambda
4. API Gateway exposes the function via a public URL.
5. Anyone can access the function via HTTP.

---

## 🧾 Lambda Function Code (`hello_world/app.py`)

```python
def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": '{"message": "Hello, world!"}'
    }

```


⚙️ GitHub Actions Workflow (.github/workflows/deploy.yml)

``` Yaml

name: Deploy to AWS

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install AWS SAM CLI
        run: |
          pip install aws-sam-cli

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v2
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Package SAM app
        run: |
          sam package \
            --template-file template.yaml \
            --output-template-file packaged.yaml \
            --s3-bucket aws-sam-cli-managed-default-samclisourcebucket-twoi2fbhlrju

      - name: Deploy SAM app
        run: |
          sam deploy --no-confirm-changeset --no-fail-on-empty-changeset

```

Make sure your AWS credentials are stored as GitHub secrets: AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY

📦 SAM Commands (Used in Workflow)

sam package \
  --template-file template.yaml \
  --output-template-file packaged.yaml \
  --s3-bucket aws-sam-cli-managed-default-samclisourcebucket-twoi2fbhlrju

sam deploy --no-confirm-changeset --no-fail-on-empty-changeset

📤 Deployment Output
After pushing to GitHub, the workflow deploys:

✅ Lambda Function ARN arn:aws:lambda:us-east-1:487527603759:function:dube-lambda-HelloWorldFunction-lL4CLB9AuDcZ

✅ IAM Role arn:aws:iam::487527603759:role/dube-lambda-HelloWorldFunctionRole-vPOfyeCjAlRC

✅ API Gateway URL https://36th270ig1.execute-api.us-east-1.amazonaws.com/Prod/hello/

🧪 Testing

✅ In Browser
Visit: https://36th270ig1.execute-api.us-east-1.amazonaws.com/Prod/hello/

You’ll see:
Json
{"message": "Hello, world!"}


✅ With curl

curl "https://36th270ig1.execute-api.us-east-1.amazonaws.com/Prod/hello/"

📄 Final Notes
DubeDeploy is a hands-on example of how to build a CI/CD pipeline for serverless applications. It shows how GitHub Actions and AWS SAM can work together to automate deployments — making your workflow faster, safer, and more scalable.

This setup is ideal for:

- Microservices
- Event-driven apps
- Lightweight APIs
- Learning serverless DevOps

