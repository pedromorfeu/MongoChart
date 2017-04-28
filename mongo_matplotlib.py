import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pymongo
from pymongo import MongoClient
import sys

host = sys.argv[1]
port = sys.argv[2]
user = sys.argv[3]
password = sys.argv[4]
print(host)

client = MongoClient("mongodb://" + host + ":" + port + "/")
print(client)
db = client.mydb
print(db)

db.authenticate(name=user, password=password)

print(db.collection_names())

coll = db.sensor
print(coll)

one = coll.find_one({"event":"Battery"})
print(one)

datetime_str = one["time"]
print(datetime_str)

datetime_obj = datetime.datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")
print(datetime_obj)
print(datetime_obj.date())
print(datetime_obj.time())

plt.plot([1,2,3,4], [2,4,6,8])
plt.ylabel('some numbers')
plt.show()