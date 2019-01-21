import numpy as np
np.random.seed(2)
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPooling2D, Conv2D
from keras.utils import np_utils
from sklearn.model_selection import train_test_split
import numpy as np

def NeuralNet(data, labels):

    model = Sequential()

    model.add(Conv2D(64, (3, 3), input_shape=(96, 96, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))
    model.add(Flatten())
    model.add(Dense(2))
    model.add(Activation('softmax'))

    model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

    (trainX, testX, trainY, testY) = train_test_split(data,
	labels, test_size=0.2)

    print("Fitting Data")
    model.fit(trainX, trainY, batch_size=1, epochs=10, verbose=1)
    score = model.evaluate(testX, testY, verbose=0)
    print(score)
    # pred = model.predict(testX)

    return model
