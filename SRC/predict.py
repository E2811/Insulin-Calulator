import json
from keras.models import load_model
from keras.models import model_from_json
import cv2 
import numpy as np

def food_prediction(image_path):
    ''' Recognice the food in a given image ''' 

    # load model 
    
    model_json = open('output/model.json', 'r')
    loaded_model = model_json.read()
    model_json.close()
    model = model_from_json(loaded_model)
    model.load_weights("output/model.h5")

    # image preprocessing 

    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    image = cv2.resize(image,(224,224))
    np_image = np.array(image, dtype =np.float32)/ 255.0
    
    # predict

    pred = model.predict(np.expand_dims(np_image,axis=0))[0]
    classses = ['cheese','egg','fruit&veggies','hamburguer','meat','pasta','pizza','rice']

    print(f'Probability: {max(pred)}--> {classses[np.argmax(pred)]}')
    return classses[np.argmax(pred)], np_image