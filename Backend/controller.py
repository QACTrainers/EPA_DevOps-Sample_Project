from flask import Flask, Request

app = Flask(__name__)

""" Record API Requests """
@app.route("/record")
def getAllRecords():
    return "Get All Records"

@app.route("/record/<id>")
def getRecord(id):
    return f"Get Record {id}"

@app.route("/record", methods=['POST'])
def createRecord():
    record = request.get_json()
    return record

@app.route("/record/<id>", methods=['PUT'])
def updateRecord(id):
    record = request.get_json()
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