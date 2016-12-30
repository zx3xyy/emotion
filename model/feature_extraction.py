from keras.models import Sequential,Model
from keras.layers.core import Flatten, Dense, Dropout,Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D, ZeroPadding2D
from keras.optimizers import SGD
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input,VGG16
from keras.layers.recurrent import LSTM
from keras.layers import TimeDistributed,Input, Convolution2D, ZeroPadding2D, MaxPooling2D, Flatten, Dense, Dropout
from keras.applications.resnet50 import ResNet50
from config import VGG_face_weights_path
from glob import glob
import os
import numpy as np
import tensorflow as tf
tf.python.control_flow_ops = tf
import cv2
def VGG():
    return VGG16(include_top=False, weights='imagenet')

def ResNet50_pooling():
	CNN =  ResNet50(include_top=False)
	return CNN

def get_feature(img_path,compiled_model):
	#prepare image
    im = prepare_image(img_path)
    feature = compiled_model.predict(im)
    return feature

def get_features_from_directory(img_directroy,compiled_model):
	features = []
	file_paths = sorted(glob(os.path.join(img_directroy,"*")))
    # file_paths = [x if "jpg" in x for x in file_paths]
    # print(file_paths)
	for img_path in file_paths:
		feature = get_feature(img_path,compiled_model)
		features.append(feature)
	features = np.asarray(features)
	# features : (M,N) array
	# M is number of images in the directory and N is the dimension of each feature.
	return features    

def prepare_image(path):
    img_path = path
    from keras.applications.vgg16 import preprocess_input
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    return x



# def vgg_face_fc6(weights_path=VGG_face_weights_path):
#     img = Input(shape=(3, 224, 224))

#     pad1_1 = ZeroPadding2D(padding=(1, 1))(img)
#     conv1_1 = Convolution2D(64, 3, 3, activation='relu', name='conv1_1')(pad1_1)
#     pad1_2 = ZeroPadding2D(padding=(1, 1))(conv1_1)
#     conv1_2 = Convolution2D(64, 3, 3, activation='relu', name='conv1_2')(pad1_2)
#     pool1 = MaxPooling2D((2, 2), strides=(2, 2))(conv1_2)

#     pad2_1 = ZeroPadding2D((1, 1))(pool1)
#     conv2_1 = Convolution2D(128, 3, 3, activation='relu', name='conv2_1')(pad2_1)
#     pad2_2 = ZeroPadding2D((1, 1))(conv2_1)
#     conv2_2 = Convolution2D(128, 3, 3, activation='relu', name='conv2_2')(pad2_2)
#     pool2 = MaxPooling2D((2, 2), strides=(2, 2))(conv2_2)

#     pad3_1 = ZeroPadding2D((1, 1))(pool2)
#     conv3_1 = Convolution2D(256, 3, 3, activation='relu', name='conv3_1')(pad3_1)
#     pad3_2 = ZeroPadding2D((1, 1))(conv3_1)
#     conv3_2 = Convolution2D(256, 3, 3, activation='relu', name='conv3_2')(pad3_2)
#     pad3_3 = ZeroPadding2D((1, 1))(conv3_2)
#     conv3_3 = Convolution2D(256, 3, 3, activation='relu', name='conv3_3')(pad3_3)
#     pool3 = MaxPooling2D((2, 2), strides=(2, 2))(conv3_3)

#     pad4_1 = ZeroPadding2D((1, 1))(pool3)
#     conv4_1 = Convolution2D(512, 3, 3, activation='relu', name='conv4_1')(pad4_1)
#     pad4_2 = ZeroPadding2D((1, 1))(conv4_1)
#     conv4_2 = Convolution2D(512, 3, 3, activation='relu', name='conv4_2')(pad4_2)
#     pad4_3 = ZeroPadding2D((1, 1))(conv4_2)
#     conv4_3 = Convolution2D(512, 3, 3, activation='relu', name='conv4_3')(pad4_3)
#     pool4 = MaxPooling2D((2, 2), strides=(2, 2))(conv4_3)

#     pad5_1 = ZeroPadding2D((1, 1))(pool4)
#     conv5_1 = Convolution2D(512, 3, 3, activation='relu', name='conv5_1')(pad5_1)
#     pad5_2 = ZeroPadding2D((1, 1))(conv5_1)
#     conv5_2 = Convolution2D(512, 3, 3, activation='relu', name='conv5_2')(pad5_2)
#     pad5_3 = ZeroPadding2D((1, 1))(conv5_2)
#     conv5_3 = Convolution2D(512, 3, 3, activation='relu', name='conv5_3')(pad5_3)
#     pool5 = MaxPooling2D((2, 2), strides=(2, 2))(conv5_3)

#     flat = Flatten()(pool5)
#     fc6 = Dense(4096, activation='relu', name='fc6')(flat)
#     #fc6_drop = Dropout(0.5)(fc6)
#     #fc7 = Dense(4096, activation='relu', name='fc7')(fc6_drop)
#     #fc7_drop = Dropout(0.5)(fc7)
#     #out = Dense(2622, activation='softmax', name='fc8')(fc7_drop)

#     model = Model(input=img, output=fc6)
#     if weights_path:
#         model.load_weights(weights_path,by_name=True)

#     sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
#     model.compile(optimizer=sgd, loss='categorical_crossentropy')
#     return model