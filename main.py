"""
Clockify test application
"""

import configparser
import pandas as pd
import requests
import options

URL_BASE = 'https://api.clockify.me/api/v1/user'

config = configparser.ConfigParser()
config.read('config.ini')
X_Api_Key = config.get('clockify', 'API_KEY')

headers = {'content-type': 'application/json', 'X-Api-Key': X_Api_Key}
try:
    response = requests.get(URL_BASE, headers=headers)
except requests.exceptions.RequestException as error:
    raise SystemExit(error) from error
else:
    json_response_base = response.json()
    print("Records received successfully!")
    workspaceId = json_response_base['activeWorkspace']
    userId = json_response_base['id']

    URL = 'https://reports.api.clockify.me/v1'
    config = configparser.ConfigParser()
    config.read('config.ini')
    X_Api_Key = config.get('clockify', 'API_KEY')

    headers = {'content-type': 'application/json', 'X-Api-Key': X_Api_Key}
    api_report = f'/workspaces/{workspaceId}/reports/summary'
    api_url = URL + api_report
    response = requests.post(api_url, headers=headers, json=options.json)
    json_response_te = response.json()

    df = pd.DataFrame.from_dict(json_response_te['groupOne'][0])
    df['add_date'] = df['children'][0]['children'][0]['_id']
    df.groupby(by=['add_date'])
    for i in df.children:
        print(f'{i["name"]} : {i["duration"]}s\n')
