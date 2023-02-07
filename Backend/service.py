from record import Record
from order import Order

class Service:

    def __init__(self, repo):
        self.repo = repo

    def getAllRecords(self):
        data = self.repo.runQuery("SELECT * FROM records").fetchall()
        dataArray = []
        for entry in data:
            dataObj = self.convertRecord(entry)
            dataArray.append(dataObj)
        return dataArray

    def getRecordId(self, id):
        data = self.repo.runQuery(f"SELECT * FROM records WHERE record_id = {id}").fetchall()
        dataObj = self.convertRecord(data[0])
        return dataObj
        
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

    def convertRecord(self, data):
        recordObj = Record(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        return recordObj.__dict__



    

