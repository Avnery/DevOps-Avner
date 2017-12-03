from flask import Flask
import boto3
import json

extractor = Flask(__name__)


@extractor.route("/secret")
def dynamdb_extractor():
    boto3.setup_default_session(region_name='us-west-2',
                                aws_secret_access_key='76RYu48cJ6zDRzaZ3FIam6uFYPfVxEL3nVJhsJ7P',
                                aws_access_key_id='AKIAJUPSIZ7XWH4KYICQ')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('devops-challenge')
    response = table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('code_name').eq('thedocker')
    )
    items = response['Items']
    return json.dumps(items)


@extractor.route("/health")
def health():
    items = {'container': r"https://cloud.docker.com/app/avnery/repository/docker/avnery/dynamoextractor/general",
             'project': "https://github.com/Avnery/DevOps-Avner", 'status': "Healthy"}
    return json.dumps(items)

if __name__ == "__main__":
    extractor.run(host="0.0.0.0", port=5000)
