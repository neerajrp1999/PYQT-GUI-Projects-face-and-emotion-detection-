# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 12:45:29 2023

@author: neera
"""


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://neerajrp1999:AjZmmeRxT4DRLFCM@meetu.b9tewzu.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri)

try:
    MEETUDATABASE=client.MEETUDATABASE
    MEETUCOLLECTION=MEETUDATABASE.MEETUCOLLECTION
except Exception as e:
    print(e)

def insert():
    data={"name":"neej","email":"neerajrp1999@gmail.com","password":"1234"}
    MEETUCOLLECTION.insert_one(data)

def fetch():
    data=MEETUCOLLECTION.find()
    for datai in data:
        print(datai)
    
def fetch_user(n):
    c=MEETUCOLLECTION.count_documents(filter={"name":n,"email":"neerajrp1999@gmail.com"})
    print(c)

def range_sort():
    q={
        "$and":[
            {"age":{"$gte":23}},
            {"age":{"$lte":33}}
        ]
    }
    p=MEETUCOLLECTION.find(q).sort("age")
def update1(n):
    #MEETUCOLLECTION.update_one(filter={"name":n,"email":"neerajrp1999@gmail.com"},
    #                          update={"$set":{"contact.[$e1].radherp1999@gmail.com":{"name":"radhe"}}})
    
    MEETUCOLLECTION.update_one({"name":n,"email":"neerajrp1999@gmail.com"}, {"$push":{
            "contact":{"neerjrp999@gmail.com" : {"name":"radhe"}
    }}}
        )
    
def replace(n):
    c=MEETUCOLLECTION.replace_one({"_id":8},{"name":n,"email":"neerajrp1999@gmail.com"})#delete all data of id and replace with this
    print(c)
def delete(n):
    c=MEETUCOLLECTION.delete_one({"_id":8})#delete all data of id and replace with this
    print(c)
#mongodb+srv://neerajrp1999:<password>@meetu.b9tewzu.mongodb.net/

if __name__=="__main__":
    update1("neeraj")