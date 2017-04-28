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
db = client.mydb

db.authenticate(name=user, password=password)

coll = db.sensor

one = coll.find_one({"event":"Battery"})
print(one)

datetime_str = one["time"]
print(datetime_str)

print(coll.find({"event":"Battery"}).count())

x = []
y = []
for event in coll.find({"event":"Battery"}, {"_id":0}):
    print(event)
    datetime_obj = datetime.datetime.strptime(event["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    x.append(datetime_obj)
    y.append(event["value"])

plt.plot(x, y)
plt.show()