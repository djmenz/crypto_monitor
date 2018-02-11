from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-west-2')


table = dynamodb.create_table(
    TableName='PeakCoin',
    KeySchema=[
        {
            'AttributeName': 'coin',
            'KeyType': 'HASH'  #Partition key
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'coin',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("Table status:", table.table_status)