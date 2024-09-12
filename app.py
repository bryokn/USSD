import os
from flask import Flask, request, make_response

app = Flask(__name__)

response = ""

@app.route('/', methods = ['GET','POST'])

def ussd():
    global response
    session_id = request.values.get("sessionId",None)
    servicecode =  request.values.get("serviceCode",None)
    phone_number = request.values.get("phoneNumber",None)
    text = request.values.get("text",None)

    if text == "":
        response = "CON What would you like to check?\n"
        response += "1. My Account\n"
        response += "2. My phone number\n"
    elif text == "1":
        response = "CON Choose a service that you require:\n"
        response += "1. My account number\n"
        response += "2. My account balance\n"
    else:
        response = "END Invalid choice"

    #return response
    return make_response(response, 200, {'Content-Type': 'text/plain'})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
