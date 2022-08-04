import config
import requests

from datetime import datetime, timedelta

# example variables
date_from = datetime.today() + timedelta(days=1)
date_to = datetime.today() + timedelta(days=14)

print ("GET /bookings")
print ("Dates: " + date_from.strftime('%Y-%m-%d') + ' - ' + date_to.strftime('%Y-%m-%d'))

body = {
    'dateFrom' : date_from.strftime('%Y-%m-%d'),
    'dateTo' : date_to.strftime('%Y-%m-%d')
}

url = '?'
for key, value in body.items():
    url = url + str(key) + '=' + str(value) + '&'

from requests.auth import HTTPBasicAuth
response = requests.get(config.api_json_url + "bookings/" + url, auth=HTTPBasicAuth(config.api_key_username, config.api_key_password))

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
print ("Bookings: " + str(data['bookings']))