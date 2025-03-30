import json
import pandas as pd
import requests

def lambda_handler(event, context):
    # Example pandas DataFrame
    data = {'Name': ['John', 'Anna'], 'Age': [23, 34]}
    df = pd.DataFrame(data)

    # Log DataFrame to CloudWatch
    print("Pandas DataFrame:")
    print(df)

    # Example of HTTP requests to a real API (with correct endpoint)
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    response_data = response.json()

    # Returning Response data
    return {
        'statusCode': 200,
        'body': json.dumps({
           'message': 'Data Retrieved Successfully',
           'data': response_data
        })
    }
