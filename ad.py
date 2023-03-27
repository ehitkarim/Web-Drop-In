from flask import Flask, render_template,jsonify, request, url_for
from flask_cors import CORS
import requests

app = Flask(__name__)
cors = CORS(app)


@app.route('/handle', methods=['POST'])

def addRegion():
    AM = request.form['AM']
    CA = request.form['CA']

    Currency = { "SG":"SGD", "GB":"GBP", "US":"USD", "NL":"EUR", "AU":"AUD"}

    Headers = {"x-API-key": "AQEhhmfuXNWTK0Qc+iSGnWssruqDEIseWIfhSMkKMcCEcDinEMFdWw2+5HzctViMSCJMYAc=-/irxwsKh3s196odKGl0ZNVUylzfzCq1tmbcx5MwStZE=-J]~^%8KbK*fVz^Dw", "content-type": "application/json"}

    body = { "merchantAccount": "VootinECOM",
         "amount": { "value": AM,"currency": Currency[CA] },
         "returnUrl": "http://127.0.0.1:5000/handle",
         "reference": "YOUR_PAYMENT_REFERENCE",
         "countryCode": CA
         }

    Result = requests.post("https://checkout-test.adyen.com/v69/sessions",headers = Headers,json = body)     
    #print(f"Received project filepath: {project_filepath}")
    Result = Result.json()

    #return Result["sessionData"]
    return render_template('checkout.html', Sessions= Result["sessionData"], ID = Result["id"])



@app.route('/')


def func():

	return render_template("ad.html")

@app.route('/checkout', methods=['POST'])

def checkout():
    header2 = request.headers.get('amount')
    #projectpath = request.form['myForm']
    return render_template('checkout.html', am=header2)


if __name__ == "__main__":
    app.run()
