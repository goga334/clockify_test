import requests
import configparser

url_base = 'https://api.clockify.me/api/v1/user'
url = 'https://api.clockify.me/api/v1'

config = configparser.ConfigParser()
config.read('config.ini')
X_Api_Key = config.get('clockify', 'API_KEY')

headers = {'content-type': 'application/json', 'X-Api-Key': X_Api_Key}
try:
    response = requests.get(url_base, headers=headers)
except requests.exceptions.RequestException as e:
    raise SystemExit(e)
else:
    json_response_base = response.json()
    print("Records received successfully!")
