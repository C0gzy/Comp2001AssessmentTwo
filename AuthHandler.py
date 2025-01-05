import requests
from flask import request, jsonify, make_response, abort
import json

#https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users



def Userlogin(LoginInfo):
    url = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"

    # Parse the LoginInfo JSON string into a Python dictionary
    LoginInfo = json.loads(LoginInfo)

    # Create the payload for the POST request with email and password
    payload = {
        "Email": LoginInfo["Email"],
        "Password": LoginInfo["Password"]
    }
    
    # Send a POST request to the authentication API with the payload
    response = requests.post(url, json=payload)
    
    # Decode the response 
    response_data = json.loads(response.content.decode('utf-8'))

    if response.status_code == 200:
        # Check if the second element in the response data indicates success
        if response_data[1] == "True":
            print("Authorised")
            return True

    # If the response status code is not 200 or the second element is not "True"
    print("Not Authorised")
    return False