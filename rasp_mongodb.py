import datetime
from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient('localhost', 27017)

# Connect to the database
db = client['mydatabase']

# Connect to the collection
collection = db['mycollection']

# Get the current date and time
now = datetime.datetime.now()

# Create a document with the data and the date
document = {
  'humidity': humidity,
  'temperature': temperature,
  'wind_speed': wind_speed,
  'date': now
}

# Insert the document into the collection
collection.insert_one(document)
