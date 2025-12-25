import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EventRegistrations')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])

        event_id = body['eventId']
        name = body['name']
        email = body['email']

        registration_id = str(uuid.uuid4())

        table.put_item(
            Item={
                'registrationId': registration_id,
                'eventId': event_id,
                'name': name,
                'email': email
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Registration Successful'})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
