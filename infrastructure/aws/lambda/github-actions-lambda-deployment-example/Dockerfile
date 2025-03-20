# Use the official Python image as the base image for building
# FROM python:3.12.7
# FROM python:3.13.0-slim
# FROM python:3.13.1-slim-bookworm
# FROM public.ecr.aws/docker/library/python:3.8.12-slim-buster
FROM public.ecr.aws/docker/library/python:3.13.1-slim-bookworm

# Set the working directory inside the container
WORKDIR /app

### install required packages
COPY function/requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY function/*.py .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the Gradio app
CMD ["python", "lambda_function.py"]
