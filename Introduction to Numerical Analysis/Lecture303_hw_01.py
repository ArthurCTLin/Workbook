# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 15:47:22 2020

@author: ACER
"""
import numpy as np
import matplotlib.pyplot as plt

mnist = np.load('./mnist.npz')
x_train = mnist['x_train'][:10000]/255.
y_train = np.array([np.eye(10)[n] for n in mnist['y_train'][:10000]])
x_test = mnist['x_test']/255.
y_test = np.array([np.eye(10)[n] for n in mnist['y_test']])

from keras.models import Sequential
from keras.layers import Dense, Reshape
from keras.optimizers import SGD
from keras.regularizers import l2

m1 = Sequential()
m1.add(Reshape((784,), input_shape=(28,28)))
m1.add(Dense(30, activation='sigmoid'))
m1.add(Dense(10, activation='softmax'))
m1.compile(loss='categorical_crossentropy',
           optimizer=SGD(lr=1.0), metrics=['accuracy'])

m2 = Sequential()
m2.add(Reshape((784,), input_shape=(28,28)))
m2.add(Dense(30, activation='sigmoid'))
m2.add(Dense(10, activation='softmax', kernel_regularizer=l2(0.01)))
m2.compile(loss='categorical_crossentropy',
           optimizer=SGD(lr=1.0), metrics=['accuracy'])

rec1 = m1.fit(x_train, y_train, epochs=100, batch_size=120,
              validation_data=(x_test, y_test))
rec2 = m2.fit(x_train, y_train, epochs=100, batch_size=120,
              validation_data=(x_test, y_test))

vep = np.linspace(1.,100.,100)
fig = plt.figure(figsize=(6,6), dpi=80)
plt.subplot(2,1,1)
plt.plot(vep,rec1.history['acc'], lw=3)
plt.plot(vep,rec1.history['val_acc'], lw=3)
plt.ylim(0.85,1.01)
plt.grid()
plt.subplot(2,1,2)
plt.plot(vep,rec2.history['acc'], lw=3)
plt.plot(vep,rec2.history['val_acc'], lw=3)
plt.ylim(0.85,1.01)
plt.grid()
plt.show()