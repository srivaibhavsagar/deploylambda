# import json
# import requests
# import sqlalchemy
# # import psycopg2
# import oracledb

def lambda_handler(event, context):
    # TODO implement
    print('hello from VSCODE')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
