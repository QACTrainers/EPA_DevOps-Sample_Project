from flask import Flask, request, jsonify
from flask_cors import CORS
from service import Service
from repo import Repo

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})

""" Setting up Service Object """

repo = Repo()
print(repo.createTable())
service = Service(repo)

""" Record API Requests """
@app.route("/record")
def getAllRecords():
    data = service.getAllRecords()
    return jsonify(response = data)

@app.route("/record/<id>")
def getRecord(id):
    data = service.getRecordId(id)
    print(data)
    return data

@app.route("/record", methods=['POST'])
def createRecord():
    record = request.get_json()
    return service.createRecord(record)

@app.route("/record/<id>", methods=['PUT'])
def updateRecord(id):
    record = request.get_json()
    service.updateRecord(id, record)
    return record

@app.route("/record/<id>", methods=["DELETE"])
def deleteRecord(id):
    return service.deleteRecord(id)

@app.route("/record/query")
def getRecordSearch():
    args = request.args
    search = args.get('search')
    data = service.getRecordSearch(search)
    return jsonify(response = data)

""" Order API Requests """

@app.route("/order")
def getAllOrders():
    data = service.getAllOrders()
    return jsonify(response = data)

@app.route("/order/<id>")
def getOrder(id):
    return service.getOrderId(id)

@app.route("/order", methods=['POST'])
def createOrder():
    order = request.get_json()
    return service.createOrder(order)

@app.route("/order/<id>", methods=['PUT'])
def updateOrder(id):
    order = request.get_json()
    return service.updateOrder(id, order)

@app.route("/order/<id>", methods=["DELETE"])
def deleteOrder(id):
    return service.deleteOrder(id)

if __name__ == "__main__":
    app.run(debug=True, host= "0.0.0.0", port=5000)