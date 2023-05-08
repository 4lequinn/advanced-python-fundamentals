import requests
url = 'url'
payload = {'product':'uwu'}
query_params={'name':'Jorge'}
response = requests.post(url,data=payload,params=query_params)
print(response.json())