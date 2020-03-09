from pymongo import MongoClient, InsertOne
from bson.json_util import dumps
from errorHandler import error_handler
from bson.objectid import ObjectId
import datetime
import json
from bson.json_util import dumps
from config import dbURL

client = MongoClient(dbURL)
db =client['diabetes']
users = db['users']


def createUser(username):
    ''' Create users in mongodb and return the user_id '''
    query = list(users.find({'username':username}, {'_id':1}))
    if query:
        raise ValueError(f'username alredy exists {query}')
    users_id = users.insert_one({'username':username}).
    return {'user_id': str(user_id), 'username':username}


def get_information(username):
    ''' Get all the information from a user '''
    query = list(users.find({'username':username}))
    if not query:
        raise ValueError('user not found')
    return { "messages": query[0]['messages']}

def enterInformation(username)
    query = list(users.find({'username':username}))
    if not query:
        raise ValueError('user not found')
    user.update_one({'username':username} , { "$push": { "dose": {"dosage": dose,"time": datetime.datetime.now()}}})
    