from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
dte = datetime.datetime.now()

# fake DBs:
dummyNum = 0

profileDB = {
    "sucess": True,
    "data": {
        "last_updated": "2/3/2021, 8:48:51 PM",
        "username": "coolname",
        "role": "Engineer",
        "color": "#3478ff"
    }
}

tankDB = []

# Index
@app.route("/", methods=["GET"])
def home():
    return "hello lab 2"

# PROFILE Routes:
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

# DATA Routes:
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "POST":
        # /POST
        global dummyNum
        dummyNum += 1   
        
        posts = {}
       
        posts["id"] = dummyNum
        posts["location"] = (request.json["location"])
        posts["lat"] = (request.json["lat"])
        posts["long"] = (request.json["long"])
        posts["percentage_full"] = (request.json["percentage_full"])

        tankDB.append(posts)

        return jsonify(tankDB)

    else:
        # /GET
        return jsonify(tankDB)

@app.route("/data/<int:tankID>", methods=["PATCH", "DELETE"])
def update(tankID):
     if request.method == "PATCH":
        # /PATCH
        for index in tankDB:
            if tankDB[index]["id"] == tankID:
                if request.json["location"] is not None: tankDB[index]["location"] = (request.json["location"])
                if request.json["lat"] is not None: tankDB[index]["lat"] = (request.json["lat"])
                if request.json["long"] is not None: tankDB[index]["long"] = (request.json["long"])
                if request.json["percentage_full"] is not None: tankDB[index]["percentage_full"] = (request.json["percentage_full"])
        
        return jsonify(tankDB) 
        
     elif request.method == "DELETE":
        # /DELETE
        for index in tankDB:
            if tankDB[index]["id"] == tankID:
                del tankDB[index]
        
        return jsonify(tankDB)

     else:
         # /GET
        return jsonify(tankDB)

# Main
if __name__ == '__main__':
   app.run(debug = True)

