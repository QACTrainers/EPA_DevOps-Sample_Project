from record import Record
from order import Order

from operator import itemgetter
from datetime import datetime

class Service:

    def __init__(self, repo):
        self.repo = repo

    def getAllRecords(self):
        data = self.repo.runQuery("SELECT * FROM records").fetchall()
        dataArray = []
        for entry in data:
            dataObj = self.convertRecord(entry)
            dataArray.append(dataObj.__dict__)
        return dataArray

    def getRecordId(self, id):
        data = self.repo.runQuery(f"SELECT * FROM records WHERE record_id = {id}").fetchall()
        dataObj = self.convertRecord(data[0])
        return dataObj.__dict__
        
    def createRecord(self, data):
        title, artist, genre, runtime, total_stock, cost = itemgetter("title", "artist", "genre", "runtime", "total_stock", "cost")(data)
        query = f"INSERT INTO records (title, artist, genre, runtime, total_stock, cost) VALUES ('{title}', '{artist}', '{genre}', {runtime}, {total_stock}, {cost});"
        return self.repo.runQuery(query)

    def updateRecord(self, id, data):
        title, artist, genre, runtime, total_stock, cost = itemgetter("title", "artist", "genre", "runtime", "total_stock", "cost")(data)
        query = f"UPDATE records SET title = '{title}', artist = '{artist}', genre = '{genre}', runtime = '{runtime}', total_stock = '{total_stock}', cost = '{cost}' WHERE record_id = {id}"
        return self.repo.runQuery(query)

    def deleteRecord(self, id):
        query = f"DELETE from records WHERE record_id = {id}"
        return self.repo.runQuery(query)

    def getRecordSearch(self, search):
        query = f"SELECT * FROM records WHERE (title LIKE '%{search}%') OR (artist LIKE '%{search}%') OR (genre LIKE '%{search}%');"
        data = self.repo.runQuery(query).fetchall()
        dataArray = []
        for entry in data:
            dataObj = self.convertRecord(entry)
            dataArray.append(dataObj.__dict__)
        return dataArray
        
        # return self.repo.runQuery(query)

    def updateStock(self, id, amount):
        data = self.getRecordId(id)
        print(data)

    def deleteAllRecords(self):
        query = "DELETE FROM records WHERE record_id > 0"
        self.repo.runQuery(query)
        return True

    # Orders 

    def getAllOrders(self):
        data = self.repo.runQuery("SELECT * FROM orders").fetchall()
        dataArray = []
        for entry in data:
            dataObj = self.convertOrder(entry)
            dataArray.append(dataObj.__dict__)
        return dataArray

    def getOrderId(self, id):
        data = self.repo.runQuery(f"SELECT * FROM orders WHERE order_id = {id}").fetchall()
        dataObj = self.convertOrder(data[0])
        return dataObj.__dict__

    def createOrder(self, data):
        item_id, quantity, total_cost = itemgetter("item_id", "quantity", "total_cost")(data)
        date_time = datetime.now().isoformat()
        query = f"INSERT INTO orders (item_id, quantity, total_cost, date_time) VALUES ({item_id}, {quantity}, {total_cost}, '{date_time}');"
        return self.repo.runQuery(query)

    def updateOrder(self, id, data):
        item_id, quantity, total_cost = itemgetter("item_id", "quantity", "total_cost")(data)
        date_time = datetime.now().isoformat()
        query = f"UPDATE orders SET item_id = {item_id}, quantity = {quantity}, total_cost = {total_cost}, date_time = '{date_time}' WHERE order_id = {id}"
        return self.repo.runQuery(query)

    def deleteOrder(self, id):
        query = f"DELETE from orders WHERE order_id = {id}"
        return self.repo.runQuery(query)

    def convertRecord(self, data):
        obj = Record(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
        return obj
    
    def convertOrder(self, data):
        obj = Order(data[0], data[1], data[2], data[3], data[4])
        return obj


    

