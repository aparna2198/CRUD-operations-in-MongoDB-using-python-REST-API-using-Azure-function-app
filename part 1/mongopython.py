# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 08:34:09 2020

@author: APARNA
"""


from pymongo import MongoClient
import pprint
class db:
    def db_connect():
        connect_str = <insert connection string from command prompt>
        db = MongoClient(connect_str).testu1
        collection = db.user
        return collection
    

class crud:
    def create(collection,data):
        data = collection.insert_one(data)
        return data
    def get(collection):
        data = list(collection.find())
        return data
    def update(collection,id_,data):
        data = collection.update_one({"Username":id_},{'$set':data},upsert = True)
        return data
    def delete(collection,id_):
        data = collection.delete_one({"Username":id_})
        return data


def main():
    dict1 = { "Username" : "Chandler201","FirstName":"Chandler", "LastName" : "Bing", "Email" : "muriel@something.com", "TokenID" : 754 }
    collection = db.db_connect()
    data = crud.create(collection,dict1)
    data = crud.update(collection,"Chandler201",{"Email":"chan@something.com"})
    data = crud.delete(collection,"Makas897")
    data = crud.get(collection)
    pprint.pprint(data)
    
if __name__ == '__main__':
    main()
    