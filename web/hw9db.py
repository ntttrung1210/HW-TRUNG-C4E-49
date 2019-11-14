import pymongo
from bson import objectid
client=pymongo.MongoClient("mongodb://dbNTT:nttrung1210husT@cluster0-shard-00-00-4ghnr.mongodb.net:27017,cluster0-shard-00-01-4ghnr.mongodb.net:27017,cluster0-shard-00-02-4ghnr.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")

ntt = client.NTTRUNG

def get_all_bikes():
    return list(ntt.bikes.find())
def add_new_bike(a,b,c,d):
    ntt.bikes.insert_one({'model':a,'fee':b,'image':c,'date':d})

print(list(ntt.bikes.find()))

