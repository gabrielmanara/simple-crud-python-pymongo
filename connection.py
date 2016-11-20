from pymongo import MongoClient

class connection(object):
    client = MongoClient()
    db = client.apoiadores
    collection = client.local.apoiadores

    def __init__(self):
        pass

    def Close(self):
        self.client.close()

