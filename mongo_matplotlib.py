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
event_type = sys.argv[5]

print("Connecting to " + host + ":" + port)
print("Event: " + event_type)

client = MongoClient("mongodb://" + host + ":" + port + "/")
db = client.mydb

db.authenticate(name=user, password=password)

coll = db.sensor

one = coll.find_one({"event": event_type})
print(one)

datetime_str = one["time"]
print(datetime_str)

count = coll.find({"event": event_type}).count()
print("Found " + str(count))

x = []
y = []
for event in coll.find({"event": event_type}, {"_id":0}).sort("time"):
    datetime_obj = datetime.datetime.strptime(event["time"], "%Y-%m-%dT%H:%M:%S.%fZ")
    x.append(datetime_obj)
    y.append(event["value"])

plt.title(event_type)
plt.plot(x, y)
# beautify the x-labels
plt.gcf().autofmt_xdate()
plt.show()