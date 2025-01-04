import requests
from flask import request, jsonify, make_response, abort
import json

#https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users




def Userlogin(LoginInfo):
    url = "https://web.socem.plymouth.ac.uk/COMP2001/auth/api/users"

    LoginInfo = LoginInfo.split(",")
    print(LoginInfo)

    payload = {
        "Email": LoginInfo[1],
        "Password": LoginInfo[3]
    }
    

    response = requests.post(url, json=payload)
    response_data = json.loads(response.content.decode('utf-8'))
    print(response_data)

    if response.status_code == 200:
        if response_data[1] == "True":
            print("Authrised")
            return True

    print("Not Authrised")
    return False