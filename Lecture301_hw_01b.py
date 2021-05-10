import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import svm

mnist = np.load('./l301practice.npz')

x_train = mnist['x_train'][mnist["y_train"]<=2]
y_train = mnist['y_train'][mnist["y_train"]<=2]
x_test  = mnist["x_test"][mnist["y_test"]<=2]
y_test  = mnist["y_test"][mnist["y_test"]<=2]


clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(x_train, y_train)

s_train = clf.score(x_train, y_train)
s_test  = clf.score(x_test, y_test)

print("Performance of training : ", s_train)
print("Performance of testing : ", s_test)

#print(s_train.shape)

fig = plt.figure(figsize=(6,6), dpi=80)
xv, yv = np.meshgrid(np.linspace(-9.,7,200),np.linspace(-5,9,200))
zv = clf.predict(np.c_[xv.ravel(), yv.ravel()])
plt.contourf(xv, yv, zv.reshape(xv.shape), alpha=.3, cmap='Blues')

for i in range(0,3):
    plt.scatter(x_train[:,0][y_train==i], x_train[:,1][y_train==i], s=50, marker="$"+str(i)+"$", alpha=0.5)
plt.show()


