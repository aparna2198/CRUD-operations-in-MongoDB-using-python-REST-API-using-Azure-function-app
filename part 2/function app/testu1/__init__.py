import logging

import azure.functions as func
from pymongo import MongoClient
import pprint
import pandas as pd
class db:
    def db_connect():
        connect_str = <insert connection string from command prompt>
        db = MongoClient(connect_str)[<insert database name>]
        col = db[<insert collection name>]
        return col
class crud:
     def create(collection,data):
         data1 = collection.insert_one(data)
         return data1
    
     def retrieve(collection):
        data = list(collection.find())
        return data
     def update(collection,id_,data):
         data = collection.update_one({"_id" :id_},{'$set':data})
         return data

     def delete(collection,id_):
         data = collection.delete_many({"Username" :id_})
         return data
         
        
# def main():
#       ob = db.db_connect()
#       data = list(ob.find())
#       df = pd.DataFrame(data)
#       df.to_excel('dumpPs.com')
#       # dict1 = {"Username" : "cab109", "FirstName" : "cab", "LastName" : "Tribiaani", "Email" : "cab@something.com", "TokenID" : 100 }
#       # data = crud.create(ob,dict1)
#       # data = crud.update(ob,{"Username":"cab109"},{"LastName":"Hecla"})
#       # data = crud.delete(ob, {"Username": "cab109"})
#       # data = crud.retrieve(ob)
#       print(data)
    
def main(req: func.HttpRequest) -> func.HttpResponse:
      ob = db.db_connect()
      if req.method == 'GET':
          data = crud.retrieve(ob)
          return func.HttpResponse(
              str(data),
              status_code = 200)
      if req.method == 'POST':
          data = req.get_json()
          data = crud.create(ob,data)
          return func.HttpResponse(
              str(data),
              status_code = 200)
      if req.method == 'PUT':
            data = req.get_json()
            logging.warn(data)
            id_ = data.get('_id')
            data = crud.update(ob,id_,data)
            return func.HttpResponse(
                str(data),
                status_code = 200)
      if req.method == 'DELETE':
          data = req.get_json()
          id_ = data.get('Username')
          data = crud.delete(ob,id_)
          return func.HttpResponse(
            str(data),
            status_code = 200)
          
     
     
         
         
         
if __name__=="__main__":
    main()