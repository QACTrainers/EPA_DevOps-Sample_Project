from flask import Flask, request, jsonify
from service import Service
from repo import Repo

app = Flask(__name__)

""" Setting up Service Object """

repo = Repo()
service = Service(repo)

""" Record API Requests """
@app.route("/record")
def getAllRecords():
    data = service.getAllRecords()
    print(data[0])
    return data

@app.route("/record/<id>")
def getRecord(id):
    data = service.getRecordId(id)
    print(data)
    return data

@app.route("/record", methods=['POST'])
def createRecord():
    record = request.get_json()
    print(record)
    return record

@app.route("/record/<id>", methods=['PUT'])
def updateRecord(id):
    record = request.get_json()
    print(record)
    return record

""" Order API Requests """

@app.route("/order")
def getAllOrders():
    return "Get All orders"

@app.route("/order/<id>")
def getOrder(id):
    return f"Get order {id}"

@app.route("/order", methods=['POST'])
def createOrder():
    order = request.get_json()
    return order

@app.route("/order/<id>", methods=['PUT'])
def updateOrder(id):
    order = request.get_json()
    return order

if __name__ == "__main__":
    app.run(debug=True, host= "0.0.0.0", port=5000)