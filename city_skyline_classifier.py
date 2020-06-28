#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import tensorflow as tf
import csv
import numpy as np
import pandas as pd
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, Dropout, Activation
from PIL import Image

header_list = ['path', 'label']
traindf = pd.read_csv('./train_data.csv', dtype = str, names = header_list)
testdf = pd.read_csv('./test_data.csv', dtype = str, names = header_list)

datagen = ImageDataGenerator(rescale = 1./255, validation_split = 0.2)
train_generator = datagen.flow_from_dataframe(dataframe=traindf, directory=None, x_col='path', y_col='label', subset='training', batch_size=10, class_mode='categorical', target_size=(256,256))
valid_generator = datagen.flow_from_dataframe(dataframe=traindf, directory=None, x_col='path', y_col='label', subset='validation', batch_size=10, class_mode='categorical', target_size=(256,256))

test_datagen = ImageDataGenerator(rescale = 1./255)
test_generator = test_datagen.flow_from_dataframe(dataframe=testdf, directory=None, x_col='path', y_col='label', batch_size=10, class_mode='categorical', target_size=(256,256))

# setting up layers
cnn = Sequential()
cnn.add(Conv2D(128, (3,3), padding = 'same', input_shape = (256,256,3), data_format='channels_last', activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (2,2)))
cnn.add(Conv2D(64, (3,3), padding = 'same', data_format='channels_last', activation = 'relu'))
cnn.add(MaxPooling2D(pool_size = (2,2)))
cnn.add(Flatten())   
cnn.add(Dense(64, activation = 'relu'))
cnn.add(Dropout(0.25))
cnn.add(Dense(3, activation = 'softmax'))

# compiling the model 
cnn.compile(keras.optimizers.Adam(lr=0.0001), loss = 'categorical_crossentropy', metrics = ['accuracy'])

# fitting the model 
step_size_train = train_generator.n//train_generator.batch_size
step_size_valid = valid_generator.n//valid_generator.batch_size
cnn.fit(x=train_generator, steps_per_epoch=step_size_train,
                    validation_data=valid_generator,
                    validation_steps=step_size_valid,
                    epochs=20)

# evaluating the model 
step_size_test = test_generator.n//test_generator.batch_size
score = cnn.evaluate(x=test_generator, steps=step_size_test)
print('Test loss:', score[0]) 
print('Test accuracy:', score[1])

# predicting output
test_generator.reset()
pred = cnn.predict(x=test_generator, steps=step_size_test, verbose=1)
predicted_class_indices = np.argmax(pred,axis=1) # array of 0-2 for every predicted image 
labels = (train_generator.class_indices) # {'new york': 0, 'paris': 1, 'toronto': 2}
labels = dict((v,k) for k,v in labels.items()) # {0: 'new york', 1: 'paris', 2: 'toronto'}
predictions = [labels[k] for k in predicted_class_indices] # array of predicted label names for every image 

# save output to csv 
filenames = test_generator.filenames

results = pd.DataFrame({"Filename":filenames, "Predictions":predictions})
results.to_csv("results.csv",index=False)

# saving the model 
cnn.save('city_skyline_cnn.h5')

# predict your own image
my_input = input("The network wants to predict more images! Input a file path to your own image of Toronto, Paris, or New York: ")
my_image = Image.open(my_input)
my_image_2 = my_image.copy()
my_image_2 = my_image_2.resize((256,256))
my_image_2 = np.expand_dims(my_image_2,axis=0)

my_pred = cnn.predict(my_image_2)
my_pred_label = np.argmax(my_pred[0])
my_pred_label = labels[my_pred_label]
print("The network predicts that you are in " + my_pred_label.capitalize() + "!")

