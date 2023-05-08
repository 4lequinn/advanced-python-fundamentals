import requests

response = requests.get('url',params={'q':'python'})
response.status_code == 200
print(response.json()['user'])