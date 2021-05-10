# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:08:43 2020

@author: ACER
"""
import numpy as np
import matplotlib.pyplot as plt
#from sklearn import svm

y_train = np.random.randint(0,2,5000)
rho = np.abs(np.random.randn(5000)/4.+1.+y_train)
phi = np.random.rand(5000)*np.pi*2
x_train = np.c_[rho*np.cos(phi), rho*np.sin(phi)]
y_train = np.array([[[1,0],[0,1]][n] for n in y_train])

from neurons import neurons
model = neurons([2,10,2])
model.fit(x_train, y_train, 20, 30, 1.0)

print('Performance (training)')
print('Loss: %.5f, Acc: %.5f' % model.evaluate(x_train, y_train))

fig = plt.figure(figsize=(6,6), dpi=80)

xv, yv = np.meshgrid(np.linspace(-3.,3.,100),np.linspace(-3.,3.,100)) 
zv = np.array([model.predict(i) for i in np.c_[xv.ravel(), yv.ravel()]])

plt.contourf(xv, yv, zv[:,1].reshape(xv.shape), alpha=.3, cmap='Blues')

plt.scatter(x_train[:,0][y_train[:,1]==0], x_train[:,1][y_train[:,1]==0], c = 'y', s=5, alpha=0.8)
plt.scatter(x_train[:,0][y_train[:,1]==1], x_train[:,1][y_train[:,1]==1], c = 'g', s=5, alpha=0.8)
plt.show()

