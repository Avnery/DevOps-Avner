FROM python:2.7-slim
WORKDIR /app
ADD . /app
EXPOSE 5000
RUN pip install --trusted-host pypi.python.org -r requirements.gitignore
CMD ["python", "DynamoExtractor.py"]