import config
import requests

print ("GET /room-types")

from requests.auth import HTTPBasicAuth
response = requests.get(config.api_json_url + "room-types/", auth=HTTPBasicAuth(config.api_key_username, config.api_key_password))

# print (response.content)
# print (response.text)

if (response.status_code != 200):
    print ("Error: ")
    print (response.status_code)
    raise Exception('Request failed')
else:
    print ("Request OK")

data = response.json()

# print (data)
print ("RoomTypes: " + str(data['roomTypes']))