from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
dte = datetime.datetime.now()

# fake DBs:

profileDB = {
    "sucess": True,
    "data": {
        "last_updated": "2/3/2021, 8:48:51 PM",
        "username": "coolname",
        "role": "Engineer",
        "color": "#3478ff"
    }
}

tankDB =[
    {
	    "id": 1,
        "location": "Engineering department",
        "lat": 18.0051862,
        "long": -76.7505108,
        "percentage_full": 92
    },
]

# Index
@app.route("/", methods=["GET"])
def home():
    return "hello lab 2"

# Profile Routes:
@app.route("/profile", methods=["GET", "POST", "PATCH"])
def profile():
    if request.method == "POST":
        # /POST
        profileDB["data"]["last_updated"] = (dte.strftime("%c"))
        profileDB["data"]["username"] = (request.json["username"])
        profileDB["data"]["role"] = (request.json["role"])
        profileDB["data"]["color"] = (request.json["color"])
       
        return jsonify(profileDB)
   
    elif request.method == "PATCH":
        # /PATCH
        profileDB["data"]["last_updated"] = (dte.strftime("%c"))
       
        if request.json["username"] is not None: profileDB["data"]["username"] = (request.json["username"])
        if request.json["role"] is not None: profileDB["data"]["role"] = (request.json["role"])
        if request.json["color"] is not None: profileDB["data"]["color"] = (request.json["color"])

        return jsonify(profileDB)

    else:
        # /GET
        return jsonify(profileDB)

# Data Routes:
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        pass
    else:
        pass

@app.route("/data/<int:tankID>", methods=["PATCH", "DELETE"])
def update(tankID):
     if request.method == "PATCH":
        pass
     else: 
        pass

# Main
if __name__ == '__main__':
   app.run(debug = True)

