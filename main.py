from model import NeuralNet
import cv2
import os
from imutils import paths
import random
from keras.preprocessing.image import img_to_array
from keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from keras.utils import np_utils
import numpy as np

IMAGE_DIMS = (96, 96, 3)
nameToNum = {'happy':0, 'sad':1}

if __name__ == "__main__":

    data = []
    labels = []

    print("Loading Data")
    imagePaths = sorted(list(paths.list_images("dataset")))
    random.seed(42)
    random.shuffle(imagePaths)

    # loop over the input images
    for imagePath in imagePaths:
        image = cv2.imread(imagePath)
        image = cv2.resize(image, (IMAGE_DIMS[0], IMAGE_DIMS[1]))
        image = img_to_array(image)
        data.append(image)

        # update labels list
        label = imagePath.split(os.path.sep)[-2]
        labels.append(label)

    data = np.array(data, dtype="float") / 255.0
    labels = np.array(labels)

    for i in range(len(labels)):
        labels[i] = nameToNum[labels[i]]

    labels = to_categorical(labels, num_classes=2)

    model = NeuralNet(data, labels)


