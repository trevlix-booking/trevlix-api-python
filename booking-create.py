import config
import requests

from datetime import datetime, timedelta

# example variables
date_from = datetime.today() + timedelta(days=10)
date_to = datetime.today() + timedelta(days=13)

print ("POST /booking-create")

body = {
    'idRoomType' : 1,
    'dateFrom' : date_from.strftime('%Y-%m-%d'),
    'dateTo' : date_to.strftime('%Y-%m-%d'),
    'timeArrival' : '16:30',
    'name' : 'John Newman',
    'email' : 'john.newman@mydomain.com',
    'phone' : '(+420) 777 123 456',
    'price' : 230.5,
    'currency' : 'EUR',
    'voucher' : 'DSCNT-20',
    'numberOfGuests' : 3,
    'numberOfChildren' : 1,
    'numberOfAdults' : 2
}

print ("Booking data: ")
print (body)

# data =  please note: using data argument to send body; requests will encode these to a application/x-www-form-urlencoded mimetype body: 
from requests.auth import HTTPBasicAuth
response = requests.post(config.api_json_url + "booking-create/", auth=HTTPBasicAuth(config.api_key_username, config.api_key_password), data=body)

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
