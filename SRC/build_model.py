import numpy as np
import json
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.preprocessing import LabelBinarizer
from keras.models import Sequential,load_model
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers.core import Activation, Flatten, Dropout, Dense
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.optimizers import Adam
from keras.preprocessing import image
from keras.callbacks import ModelCheckpoint


def create_model(model_path='output/model.h5'):
    ''' Build train model with a CNN ''' 
    X =[]
    path = 'input/'
    filenames = sorted(os.listdir(os.path.join(path,"united")))
    for file in filenames:
        print(os.path.join(path,"united",file))
        img = img = cv2.resize(cv2.cvtColor(cv2.imread(os.path.join(path,"united",file)), cv2.COLOR_BGR2RGB), (224, 224))
        X.append(img.astype(np.float32))
    X = np.array(X)

    y=np.concatenate((np.zeros(1000),np.ones(1000), np.array([float(2)]*1000),np.array([float(3)]*1000),np.array([float(4)]*1000),np.array([float(5)]*1000),np.array([float(6)]*1000),np.array([float(7)]*1000)))
    
    # split train and test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    num_classes = len(dictionary)
    X_train = X_train.astype('float32')
    X_test = X_test.astype('float32')
    X_train /= 255
    X_test /= 255

    # convert class vectors to binary class matrices
    y_train = keras.utils.to_categorical(y_train, num_classes, dtype='float32' )
    y_test = keras.utils.to_categorical(y_test, num_classes, dtype='float32')

    print(f"X.shape: {X.shape}")
    print(f"y.shape: {y.shape}")

    # Compile the CNN
    model = Sequential()
    inputShape = (224, 224, 3)
    chanDim = -1

    if K.image_data_format() == "channels_first":
        chanDim = 1
    model.add(Conv2D(32, (3, 3), padding="same", input_shape=inputShape))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(3, 3)))
    model.add(Dropout(0.25))
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(64, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Conv2D(128, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(Conv2D(128, (3, 3), padding="same"))
    model.add(Activation("relu"))
    model.add(BatchNormalization(axis=chanDim))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(1024))
    model.add(Activation("relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.5))
    model.add(Dense(n_classes))
    model.add(Activation("softmax"))

    model.summary()

    EPOCHS = 30
    INIT_LR = 1e-3
    batch_size = 32
    opt = Adam(lr=INIT_LR, decay=INIT_LR / EPOCHS)

    #Training the model

    model.compile(loss='categorical_crossentropy',
                    optimizer=opt, metrics=['accuracy'])


    model.fit(X_train, y_train,
            batch_size=batch_size,
            epochs=EPOCHS,
            verbose=1,
            validation_data=(X_test, y_test))

    if os.path.exists(model_path):
        os.remove(model_path)

    model.save(model_path)
    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)
    model.save_weights("model.h5")