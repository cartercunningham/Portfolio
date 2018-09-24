# Module used to connect Python with MongoDb
import pymongo

print(dir(pymongo))

# The default port used by MongoDB is 27017
# https://docs.mongodb.com/manual/reference/default-mongodb-port/
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define the 'classDB' database in Mongo
<<<<<<< HEAD
db = client.Dumpster_DB
print("showing dbs",client.database_names())
print("showing collections for test",db.list_collection_names())
# Query all students
=======
db = client.classDB
# print("showing dbs", client.database_names())
# print("show collections for test", db.list_collection_names())



# Query all students
# Here, db.students refers to the collection 'classroom '
# destinations = db.destinations.find()

# # Iterate through each student in the collection
# for student in classroom:
#     print(student)

# # Insert a document into the 'students' collection
# db.classroom.insert_one(
#     {
#         'name': 'Ahmed',
#         'row': 3,
#         'favorite_python_library': 'Matplotlib',
#         'hobbies': ['Running', 'Stargazing', 'Reading']
#     }
# )

# # Update a document
# db.classroom.update_one(
#     {'name': 'Ahmed'},
#     {'$set':
#         {'row': 4}
#      }
# )

# # Add an item to a document array
# db.classroom.update_one(
#     {'name': 'Ahmed'},
#     {'$push':
#         {'hobbies': 'Listening to country music'}
#      }
# )

# # Delete a field from a document
# db.classroom.update_one({'name': 'Ahmed'},
#                         {'$unset':
#                          {'gavecandy': ""}
#                          }
#                         )


# # Delete a document from a collection
# db.classroom.delete_one(
#     {'name': 'Ahmed'}
# )
>>>>>>> 93c22ebfa65717f84010ecb2600cea08cc934027
