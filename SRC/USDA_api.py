import requests
import os
import json
from dotenv import load_dotenv
load_dotenv()

def authotization():
    ''' Get the api key for USDA API '''
    token = os.getenv("API_KEY")
    if not token:
        raise ValueError("You must set an APIKEY token")
    return token

def search_food_USDA(query, sort='r'):

    ''' Make a request to USDA API and return it the id of the desired food a json fomat  '''

    api_key = authotization()
    search_dict = {
        "api_key":api_key,
        "generalSearchInput":query,
        "sort":sort
    }
    endopoint = 'https://api.nal.usda.gov/fdc/v1/search/?'

    res = requests.get(endopoint,search_dict)
    id = res.json()
    return id['foods'][0]['fdcId']


def get_CHO_food(prediction):

    ''' Make a request to USDA API and return the respective carbohydrates  '''
    api_key = authotization()
    food_id= search_food_USDA(prediction)
    search_dict = {
        "api_key":api_key,
    }
    endopoint = f'https://api.nal.usda.gov/fdc/v1/{food_id}/?'
    res = requests.get(endopoint,search_dict).json()
    return res['labelNutrients']['carbohydrates']
