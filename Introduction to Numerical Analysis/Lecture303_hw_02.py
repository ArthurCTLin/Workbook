# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:00:06 2021

@author: ACER
"""
import numpy as np
import matplotlib.pyplot as plt

mnist = np.load('./mnist.npz')
x_train = mnist['x_train']/255.
y_train = np.array([np.eye(10)[n] for n in mnist['y_train']])
x_test = mnist['x_test']/255.
y_test = np.array([np.eye(10)[n] for n in mnist['y_test']])

from skimage.transform import rotate
x_test = np.array([rotate(img,np.random.uniform(-25.,+25.)) for img in x_test])

from keras.models import Sequential
from keras.layers import Reshape, Dense, Dropout
from keras.optimizers import Adadelta

model = Sequential()
model.add(Reshape((28*28,), input_shape=(28,28)))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=20, batch_size=128)

print('Performance (training)')
print('Loss: %.5f, Acc: %.5f' % tuple(model.evaluate(x_train, y_train)))
print('Performance (testing)')
print('Loss: %.5f, Acc: %.5f' % tuple(model.evaluate(x_test, y_test)))

p_test = model.predict(x_test)
failedsample = [[img,y,p] for img,y,p in zip(mnist['x_test'],y_test,p_test) if y.argmax()!=p.argmax()]
print('# of failed test samples:',len(failedsample))

fig = plt.figure(figsize=(10,10), dpi=80)
for i in range(len(failedsample[:100])):
    plt.subplot(10,10,i+1)
    plt.axis('off')
    plt.imshow(failedsample[i][0], cmap='Greys')
    plt.text(0.,0.,'$%d\\to%d$' % (failedsample[i][1].argmax(),failedsample[i][2].argmax()),color='Red',fontsize=15)
plt.show()