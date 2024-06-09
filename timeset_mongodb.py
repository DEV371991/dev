from pymongo import MongoClient

# Set the connection timeout to 30 seconds (30000 milliseconds) 
# and the socket timeout to 10 seconds (10000 milliseconds)
client = MongoClient('localhost', 27017, connectTimeoutMS=30000, socketTimeoutMS=10000)

# Now use the client to interact with the MongoDB server
