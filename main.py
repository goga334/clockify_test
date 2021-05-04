import pandas as pd
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
#
# workspaceId = json_response_base['activeWorkspace']
# userId = json_response_base['id']
#
# start_utc = '2020' + '-' + '01' + '-' + '01' + 'T00:00:00Z'
# params={'start': start_utc, 'page-size' : 1000}
# api_time_entries = f'/workspaces/{workspaceId}/user/{userId}/time-entries'
# api_url = url + api_time_entries
# response = requests.get(api_url, headers=headers, params=params)
# json_response_te = response.json()
#
# df = pd.DataFrame.from_dict(json_response_te)
# df = df[['description','billable','timeInterval']]
# df = pd.concat([df.drop('timeInterval', axis=1), pd.DataFrame(df['timeInterval'].values.tolist())], axis=1)
# df['start'] = pd.to_datetime(df['start'])
# df['end'] = pd.to_datetime(df['end'])
# df['duration'] = df['end'] - df['start']
# df.fillna('', inplace=True)
#
# for i in range(df.shape[0]):
#     print(df.loc[i], "\n\n")