### ===========================================================================
### using public api
### ===========================================================================

import os
import json
import requests

def lambda_handler(event, context):
    # Retrieve environment variables
    api_key = os.getenv('API_KEY', 'default_key')  # Use default value if API_KEY is not set
    db_host = os.getenv('DB_HOST', 'default_db_host')
    environment = os.getenv('ENVIRONMENT', 'development')
    
    # Log the environment variables for debugging (will show up in CloudWatch logs)
    print(f"API Key: {api_key}")
    print(f"Database Host: {db_host}")
    print(f"Environment: {environment}")

    # Example: Making an API request using a public API (jsonplaceholder)
    api_url = "https://jsonplaceholder.typicode.com/todos"
    
    # No headers needed for this public API
    response = requests.get(api_url)
    
    # Return the response from the API call
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Data Retrieved Successfully',
            'data': response.json(),  # Data from the public API
            'env': {
                'api_key': api_key,
                'db_host': db_host,
                'environment': environment
            }
        })
    }
### ===========================================================================
### using your own API
### ===========================================================================

import os
import json
import requests

def lambda_handler(event, context):
    # Retrieve environment variables
    api_key = os.getenv('API_KEY')
    db_host = os.getenv('DB_HOST')
    environment = os.getenv('ENVIRONMENT')
    
    # Log the environment variables for debugging (will show up in CloudWatch logs)
    print(f"API Key: {api_key}")
    print(f"Database Host: {db_host}")
    print(f"Environment: {environment}")

    # Example: Making an API request using the API key from env variables
    api_url = "https://api.example.com/data"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    response = requests.get(api_url, headers=headers)
    
    # Return the response from the API call
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Data Retrieved Successfully',
            'data': response.json(),
            'env': {
                'api_key': api_key,
                'db_host': db_host,
                'environment': environment
            }
        })
    }
