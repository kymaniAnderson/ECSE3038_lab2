from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
dte = datetime.datetime.now()

# fake Databases:

profileDB = {
        "last_updated": "2/3/2021, 8:48:51 PM",
        "username": "coolname",
        "role": "Engineer",
        "color": "#3478ff"
    }

tankDB ={
        "tankID": 1,
        "tankLocDesc": "South-West",
        "tankprcFull": 12,
        "tankLatitude": 9,
        "tankLongitude": "Master"
    }

# Index
@app.route("/", methods=["GET"])
def home():
    pass

# Profile Routes:
@app.route("/profile", methods=["GET", "POST", "PATCH"])
def profile():
    if request.method == "POST":
        # /POST
        profileDB["last_updated"].append(dte.strftime("%c"))
        profileDB["username"].append(request.json["username"])
        profileDB["role"].append(request.json["role"])
        profileDB["color"].append(request.json["color"])
       
        return jsonify(profileDB)
   
    elif request.method == "PATCH":
        # /PATCH
        profileDB["last_updated"].append(dte.strftime("%c"))
        print("") if request.json["username"] is None else profileDB["username"].append(request.json["username"])
        print("") if request.json["role"] is None else profileDB["role"].append(request.json["role"])
        print("") if request.json["color"] is None else profileDB["color"].append(request.json["color"])

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

