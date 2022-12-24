from flask import Flask,request,jsonify

app = Flask(__name__)

contacts = [{"id":1,"contact":"9987644456","name":"Raju","done":False},
             {"id":2,"contact":"9876543222","name":"Rahul","done":False}]

@app.route("/add-data",methods = ["POST"])
def addtask():
    if not request.json:
        return jsonify({"status":"error","message":"Fill in the details"},400)
    
    contact = {
        "id":contacts[-1]["id"]+1,
        "contact":request.json.get("contact",""),
        "name":request.json["name"],
        "done":False
        }
    contacts.append(contact)

    return jsonify({"status":"Success","message":"Details successfully submitted"},200)


@app.route("/getdata")
def getdata():
    return jsonify({"data":contacts})


if __name__ == "__main__":
    app.run(debug=True)