import os
import shutil
   
            
def move_images(information, folder):

    ''' Divide all the images in test, and train and save the images in the respective folders ''' 
    
    path ='food/'
    for classes, url in information.items():
        for imagePath in url:
            filename = imagePath.split(os.path.sep)[-1]
            dirPath = os.path.join(path,folder) 
            if not os.path.exists(dirPath):
                os.mkdir(dirPath)
            p = os.path.join(dirPath,classes+filename)
            shutil.copy2(imagePath,p)
