import sqlalchemy as db
import pandas as pd
import os
from dotenv import load_dotenv
load_dotenv()

url= os.getenv('URL')
engine = db.create_engine(url)
connection = engine.connect()


def adduser(username, password, weight):
    ''' Insert information of a new user '''
    query = """INSERT INTO user (username, password, weight) 
        VALUES ('{}','{}','{}');""".format(username, password, weight)
    id = connection.execute(query) 
    return id.lastrowid


def addfood(user_id, path, prediction):
    ''' Insert information of food image '''
    query = """INSERT INTO fotos (path, comida, user_user_id, create_time) 
        VALUES ('{}','{}','{}',CURRENT_TIMESTAMP);""".format(path, prediction, user_id)
    id = connection.execute(query) 
    return id.lastrowid

def adddose(foto_id, carbohydrates, dose):
    ''' Insert dose needed '''
    query = """INSERT INTO calculo (carbohydrates, dose, fotos_fotos_id, create_time) 
        VALUES ('{}','{}','{}',CURRENT_TIMESTAMP);""".format(carbohydrates,dose, foto_id)
    connection.execute(query) 
    return "everything OK"

def getDataUser(user_id):
    ''' Get information from user ''' 
    query = """
        SELECT weight FROM user WHERE user_id='{}'
    """.format(user_id)
    df= pd.read_sql_query(query, engine)
    return df

def getDataFoto(foto_id):
    ''' Get information from foto ''' 
    query = """
        SELECT path, comida, create_time FROM fotos WHERE foto_id='{}'
    """.format(foto_id)
    df= pd.read_sql_query(query, engine)
    return df

def getDataCalculo(foto_id):
    ''' Get information from foto ''' 
    query = """
        SELECT carbohydrates, dose, create_time FROM calculo WHERE fotos_foto_id='{}'
    """.format(foto_id)
    df= pd.read_sql_query(query, engine)
    return df

print(getDataFoto(1))
