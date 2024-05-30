import requests
from datetime import datetime

# Application URL
APP_URL = 'https://www.bharatlabz.com/'

# Expected HTTP status code for a successful response
EXPECTED_STATUS_CODE = 200

def check_app_status():
    try:
        # Send an HTTP request to the application
        response = requests.get(APP_URL)

        # Get the status code from the response
        status_code = response.status_code

        # Check if the status code matches the expected value
        if status_code == EXPECTED_STATUS_CODE:
            print(f'{datetime.now()}: Application is UP. Status code: {status_code}')
        else:
            print(f'{datetime.now()}: Application is DOWN. Status code: {status_code}')

    except requests.exceptions.RequestException as e:
        # Handle exceptions (e.g., network errors, timeouts)
        print(f'{datetime.now()}: Error checking application status: {e}')

if __name__ == '__main__':
    check_app_status()
    
