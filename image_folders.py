import os
import shutil
   
            
def move_images(information, folder):

    ''' Unite all the image in a unique folder with includying its class in the name ''' 
    
    path ='input/'
    for classes, url in information.items():
        for imagePath in url:
            filename = imagePath.split(os.path.sep)[-1]
            dirPath = os.path.join(path,folder) 
            if not os.path.exists(dirPath):
                os.mkdir(dirPath)
            p = os.path.join(dirPath,classes+filename)
            shutil.copy2(imagePath,p)
