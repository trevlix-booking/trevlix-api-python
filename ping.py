import config
import requests

print ("GET /ping")

from requests.auth import HTTPBasicAuth
response = requests.get(config.api_json_url + "ping/", auth=HTTPBasicAuth(config.api_key_username, config.api_key_password))

# print (response.content)

print (response.text)

if (response.status_code != 200):
    print ("Error: ")
    print (response.status_code)
    raise Exception('Connecton failed')
else:
    print ("Connection OK")