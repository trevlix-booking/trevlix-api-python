import config
import requests

# example variables
days = 3


print ("GET /bookings-latest")
print ("Days: " + str(days))

body = {
    'days' : days
}

url = '?'
for key, value in body.items():
    url = url + str(key) + '=' + str(value) + '&'

from requests.auth import HTTPBasicAuth
response = requests.get(config.api_json_url + "bookings-latest/" + url, auth=HTTPBasicAuth(config.api_key_username, config.api_key_password))

# print (response.content)
# print (response.text)

if (response.status_code != 200):
    print ("Error: ")
    print (response.status_code)
    raise Exception('Request failed')
else:
    print ("Request OK")

data = response.json()

for booking in data["bookings"]:
    name = booking["name"]
    print(f"Booking name: {name}")

# print (data)
print ("Bookings JSON: " + str(data['bookings']))
