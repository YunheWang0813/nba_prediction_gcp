import json
import boto3
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    print('## EVENT')
    print(event)
    print(event['queryStringParameters'])
    team = event['queryStringParameters']['Team']
    oppt = event['queryStringParameters']['Oppt']
    
    # connect to the data base
    NBA_database = dynamodb.Table('nba-match')
    # queue the data base database with given information
    queue_response = NBA_database.get_item(
        Key={
            'Team': team,
            'Oppt':oppt
        }
    )
    
    # create a response
    responseObject = {}
    queue_response['ResponseMetadata']['HTTPStatusCode']
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = queue_response['Item']
	
    return {'statusCode': 200,
        'body': json.dumps(responseObject)
        }