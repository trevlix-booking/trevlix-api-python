import config
import requests

# example variables
# change it to your real booking id to cancel (please note, that you can cancel only bookings created by your API Key)
id_booking_cancel = 583

print ("POST /booking-cancel")
print ("id: " + str(id_booking_cancel))

body = {
    'id' : id_booking_cancel
}

# data =  please note: using data argument to send body; requests will encode these to a application/x-www-form-urlencoded mimetype body: 
from requests.auth import HTTPBasicAuth
response = requests.post(config.api_json_url + "booking-cancel/", auth=HTTPBasicAuth(config.api_key_username, config.api_key_password), data=body)

# print (response.content)
# print (response.text)

if (response.status_code != 200):
    print ("Error: ")
    print (response.status_code)
    raise Exception('Request failed')
else:
    print ("Request OK")

data = response.json()

print (data)
