from record import Record
from order import Order

class Service:

    def __init__(self, repo):
        self.repo = repo

    def getAllRecords(self):
        return "get All Records"

    def getRecordId(self, id):
        return "get One Record"

    def createRecord(self, data):
        record = Record(data)
        return "Create new record"

    def updateRecord(self, id, data):
        record = Record(data)
        return "Update one Record"

    # Orders 

    def getAllOrders(self):
        return "get All Orders"

    def getOrderId(self, id):
        return "get All Records"

    def createOrder(self, data):
        order = Order(data)
        return "Created order"

    def updateOrder(self, id, data):
        order = Order(data)
        return "Updated order"

    def deleteOrder(self, id):
        return "Deleted order"

    

