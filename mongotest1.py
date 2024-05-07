
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://ds5301:pk1053@cluster0.6tqcwny.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

d = {
    "name" : "pankaj",
    "email" : "pankh@gmail.com",
    "surname" : "Kumar"
}
db1 = client['mongotest1']
coll = db1['test']
coll.insert_one(d )

d1 = {
    "name" : "ayesha",
    "surname" : "naaz",
    "city" : "kolkata"
}
db2 = client['mongotest1']
coll1 = db2['test']
coll1.insert_one(d1 )
