#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 11:51:05 2019

@author: juhichecker
"""

import numpy as np #used to import mathematical operations
import matplotlib.pyplot as plt #used to plot different things in python
import pandas as pd #import data sets and manage data sets


#import dataset
#so make the directory so store dataset
dataset = pd.read_csv('para_data_train_shuffle.csv')
X_train = dataset.iloc[: , :38].values  #independant variable vector
#iloc[] means first : is for rows(i.e.select all the lines) and 2nd : is for column (i.e.select all columns execpt last column)
Y_train = dataset.iloc[: , 38:].values

dataset1 = pd.read_csv('para_data_test_shuffle.csv')
X_test = dataset1.iloc[: , :38].values  #independant variable vector
#iloc[] means first : is for rows(i.e.select all the lines) and 2nd : is for column (i.e.select all columns execpt last column)
Y_test = dataset1.iloc[: , 38:].values

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from keras.models import Sequential
from keras.utils import np_utils
from keras.layers import Dense, Dropout, GaussianNoise, Conv1D
from keras.preprocessing.image import ImageDataGenerator
from keras import regularizers

import matplotlib.pyplot as plt
import seaborn as sns

'''
scaler = StandardScaler()
scaler.fit(X_train)
X_sc_train = scaler.transform(X_train)
X_sc_test = scaler.transform(X_test)


pca = PCA(n_components=70)
pca.fit(X_train)

plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of components')
plt.ylabel('Cumulative explained variance')

#choose 45 components

NCOMPONENTS = 50

pca = PCA(n_components=NCOMPONENTS)
X_pca_train = pca.fit_transform(X_sc_train)
X_pca_test = pca.transform(X_sc_test)
pca_std = np.std(X_pca_train)

print(X_sc_train.shape)
print(X_pca_train.shape)


'''
#Model

model = Sequential()
layers = 10
units = 15

model.add(Dense(units, input_dim=38, activation='relu', kernel_regularizer=regularizers.l1(0.1)))
#model.add(GaussianNoise(pca_std))
for i in range(layers):
    model.add(Dense(units, activation='relu'))
    #model.add(GaussianNoise(pca_std))
    #model.add(Dropout(0.1))
model.add(Dense(6, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['categorical_accuracy'])

history = model.fit(X_train, Y_train, epochs=1000, batch_size=512, validation_split=0.30, verbose=2)

_, test_acc = model.evaluate(X_test, Y_test, verbose=1)
print('Test: ',test_acc)

from keras.models import load_model

model.save('Job_Role_model.h5')
print("Model saved")

'''
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'y', label='Training loss')
plt.plot(epochs, val_loss, 'r', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()

print(history.history())

acc = history.history['acc']
val_acc = history.history['val_acc']
plt.plot(epochs, acc, 'y', label='Training acc')
plt.plot(epochs, val_acc, 'r', label='Validation acc')
plt.title('Training and validation accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()


predictions = model.predict_classes(X_pca_test, verbose=0)

def write_predictions(predictions, fname):
    pd.DataFrame({"ImageId": list(range(1,len(predictions)+1)), "Label": predictions}).to_csv(fname, index=False, header=True)

write_predictions(predictions, "pca-keras-mlp.csv")

'''
