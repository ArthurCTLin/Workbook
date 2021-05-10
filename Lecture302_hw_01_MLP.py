# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:08:43 2020

@author: ACER
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

y_train = np.random.randint(0,2,5000)
rho = np.abs(np.random.randn(5000)/4.+1.+y_train)
phi = np.random.rand(5000)*np.pi*2
x_train = np.c_[rho*np.cos(phi), rho*np.sin(phi)]

clf = MLPClassifier(hidden_layer_sizes=(10), activation="relu",
                 solver='adam', alpha=0.0001, learning_rate="constant",
                 learning_rate_init=0.001, power_t=0.5, max_iter=2000 ,tol=1e-4)

clf.fit(x_train, y_train)

s_train = clf.score(x_train, y_train)
print('Performance (training):', s_train)

fig = plt.figure(figsize=(6,6), dpi=80)

xv, yv = np.meshgrid(np.linspace(-3.,3.,100),np.linspace(-3.,3.,100))
zv = clf.predict(np.c_[xv.ravel(), yv.ravel()])
plt.contourf(xv, yv, zv.reshape(xv.shape), alpha=.3, cmap='Blues')

plt.scatter(x_train[:,0][y_train==0], x_train[:,1][y_train==0], c = 'y', s=5, alpha=0.8)
plt.scatter(x_train[:,0][y_train==1], x_train[:,1][y_train==1], c = 'g', s=5, alpha=0.8)
plt.show()

