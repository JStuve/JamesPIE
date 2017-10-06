# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import config
from twilio.rest import Client

account_sid = config.account_sid
auth_token  = config.auth_token

client = Client(account_sid, auth_token)

message = client.messages.create(
    to= config.Master_number, 
    from_= config.James_number,
    body="Hello from Python!")

print(message.sid)

