import json

class Record: 

    def __init__(self, item_id, name, artist, genre, runtime, total_stock, cost):
        self.item_id = item_id
        self.name = name
        self.artist = artist
        self.genre = genre
        self.runtime = runtime
        self.total_stock = total_stock
        self.cost = cost

    def lowerStock(self, amount):
        if amount <= 1:
            self.total_stock -= amount
            return self.total_stock
        else:
            return "Cannot lower by a negative"

            
