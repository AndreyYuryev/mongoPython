import pymongo

# Connect to the MongoDB instance
client = pymongo.MongoClient("mongodb://mongodb:27017/", username='root', password='example')

# Select the database and collection you want to use
db = client["mydatabase"]
collection = db["mycollection"]

# Define the document you want to insert
document = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Insert the document into the collection
result = collection.insert_one(document)

# Print the ID of the inserted document
print(result.inserted_id)

# Find a document in the collection
document = collection.find_one({"name": "John"})

# Print the document
print(document)