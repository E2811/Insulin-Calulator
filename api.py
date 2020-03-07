from pymongo import MongoClient, InsertOne
from bson.json_util import dumps
from errorHandler import error_handler
from config import dbURL

client = MongoClient(dbURL)
db =client['chatgroup']
users = db['users']

@error_handler
def createUser(username):
    ''' Create users in mongodb and return the user_id '''
    query = list(users.find({'username':username}, {'_id':1}))
    if query:
        raise ValueError(f'username alredy exists {query}')
    user_id = uniqueID()
    users.insert_one({'user_id':user_id, 'username':username})
    return {'user_id': str(user_id), 'username':username}

