The AWS Serverless Application Model (SAM) CLI is an open-source CLI tool that helps you develop serverless applications containing Lambda functions, Step Functions, API Gateway, EventBridge, SQS, SNS and more. Some of the features it provides are:

# reference
https://github.com/aws/aws-sam-cli

# use aws-lambda-web-adaptor
https://github.com/awslabs/aws-lambda-web-adapter/blob/main/examples/fastapi/README.md

# update dockerfile to include following
FROM public.ecr.aws/docker/library/python:3.8.12-slim-buster
COPY --from=public.ecr.aws/awsguru/aws-lambda-adapter:0.8.4 /lambda-adapter /opt/extensions/lambda-adapter