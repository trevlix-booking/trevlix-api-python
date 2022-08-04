import config
import requests

# example variables
id_booking = 123

print ("GET /booking")
print ("id: " + str(id_booking))

body = {
    'id' : id_booking
}

url = '?'
for key, value in body.items():
    url = url + str(key) + '=' + str(value) + '&'

from requests.auth import HTTPBasicAuth
response = requests.get(config.api_json_url + "booking/" + url, auth=HTTPBasicAuth(config.api_key_username, config.api_key_password))

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
print ("Booking: " + str(data['booking']))