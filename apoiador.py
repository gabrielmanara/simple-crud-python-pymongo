from pprint import pprint

class apoiador(object):
    #Atributos
    HasError, MsgError, apoiador_id, apoiador_imagem, apoiador_name = False, None, None, None, None

    def __init__(self, db, conn, collection):
        self.db = db
        self.conn = conn
        self.collection = collection

    def insert(self):
        self.HasError = False
        self.MsgError = ""

        try:
            apoiadorList = {"id" : self.apoiador_id,
                            "picture" : self.apoiador_imagem,
                            "name" : self.apoiador_name
                            }
            row = self.collection.insert_one(apoiadorList)

        except:
            self.HasError = True
            self.MsgError = row
            pass

    def listarApoiador(self, pCodigo):
        self.HasError = False
        self.MsgError = ""

        try:
            if pCodigo == 0:
                row = self.collection.find()
            else:
                row = self.collection.find({ "id": str(pCodigo)})


            for document in row:
                pprint(document)

        except:
            self.HasError = True
            if pCodigo == 0:
                self.MsgError = row
            else:
                self.MsgError = row
            pass

    def update(self, pCodigo):
        self.HasError = False
        self.MsgError = ""

        try:
            apoiadorList = {"id": self.apoiador_id,
                            "picture": self.apoiador_imagem,
                            "name": self.apoiador_name
                            }


            row = self.collection.find_and_modify(query={'id': str(pCodigo)}, update={"$set": apoiadorList}, upsert=False, full_response=True)

        except:
            self.HasError = True
            self.MsgError = row
            pass

    def delete(self, pCodigo):
        self.HasError = False
        self.MsgError = ""

        try:
            row = self.collection.delete_many({"id": str(pCodigo)})
        except:
            self.HasError = True
            self.MsgError = row
            pass