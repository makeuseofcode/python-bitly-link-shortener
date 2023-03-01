import requests
import json
import time
import sys

# In the cmd, you need to type pip install requests

# Get the URL you want to shorten from the command line argument

commandLineArgs = sys.argv

if len(commandLineArgs) > 1:
    url = commandLineArgs[1]
else:
    print('Please enter the URL you want to shorten as a command line argument')
    sys.exit()
    
print('Generating shortened URL...')
 
# Enter your Bitly access token here
access_token = '9a3902a9950af14e707fd278291920f5b446d7eb'



# Bitly API endpoint for shortening URLs
endpoint = 'https://api-ssl.bitly.com/v4/shorten'

# Create the API request headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json',
}

# Define the maximum number of retries
max_retries = 3

# Initialize the retry counter
retry_count = 0


while retry_count < max_retries:
    # Create the API request body with the URL to shorten
    data = {
        'long_url': url,
    }

    # Send the API request to shorten the URL
    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

    # Check if the API request was successful
    if response.status_code == 200:
        # Get the shortened URL from the API response
        shortened_url = json.loads(response.content)['link']
        print(f'Shortened URL: {shortened_url}')
        break
    else:
        retry_count += 1
        if retry_count < max_retries:
            time.sleep(5)
else:
    print('URL shortening was not successful.')

    