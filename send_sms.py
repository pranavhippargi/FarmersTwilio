'''from twilio.rest import Client
#from Credentials import account_sid, auth_token, my_cell, my_twilio


client = Client('ACdf3fe78024277d62b37d232d6c420592', '125903a4cc62889e863b0f775caed4d7')

my_msg = "This is from twilio"

message = client.messages.create(to="+19163379294", from_="5303631182",
                                     body=my_msg)
'''

import requests
import os
from twilio.rest import Client

class Hello():
    
    api_key = 'http://api.openweathermap.org/data/2.5/weather?appid=c38e770a1da2d9c102a1e4a5ae98f0d1&q='
    city = input("Input your city name: ")
    url = api_key + city
    data = requests.get(url).json()
    formatted_data = data['weather'][0]['description']
    greeting = "Hi Dad, this is Pranav and this is a python app I made , It is " 
    hello1 =  greeting + (str(formatted_data) + " in Syracuse right now. This will help farmers know the exact weather conditions so they can conserve water.")
    print(hello1)
    print(str(hello1))
    
    
    client = Client('ACdf3fe78024277d62b37d232d6c420592', '125903a4cc62889e863b0f775caed4d7')
    message = client.messages.create(to="+19167305433", from_="5303631182",
                                     body=hello1)
                                     


    