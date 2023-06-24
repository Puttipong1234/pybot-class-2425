from flask import Flask , request
from cryptotrade import *
import json

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

""" new route crypto signals route """

@app.route("/crypto",methods=["POST"])
def crypto_trade():
    if request.method == "POST":
        
        data = request.data
        signal_dict = json.loads(data) # json(binary) --> dictionary
        
        pair = signal_dict["pair"]
        action = signal_dict["action"]
        amt = float(signal_dict["amount"])
        
        if "OPEN LONG" in action:
            result = openlong(pair=pair,amount=amt)
        
        elif "TPSL LONG" in action:
            """ TPSL/LONG/100 """
            partial_close = float(action.split(" ")[2])
            result = closelong(pair=pair,amount=amt*(partial_close/100))
        
        elif "OPEN SHORT" in action:
            result = openshort(pair=pair,amount=amt)
        
        elif "TPSL SHORT" in action:
            partial_close = float(action.split(" ")[2])
            result = closeshort(pair=pair,amount=amt*(partial_close/100))
        
        
        return "200"

@app.route("/crypto/checkwallet")
def crypto_checkwallet():
    r = checkwallet()
    return r

if __name__ == '__main__':
    app.run(debug=True)
    