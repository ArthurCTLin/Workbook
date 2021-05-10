import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


mnist = np.load('./mnist.npz')
x_train = mnist['x_train'][mnist["y_train"]>=8]/255
y_train = mnist['y_train'][mnist["y_train"]>=8]
x_test = mnist['x_test'][mnist["y_test"]>=8]/255
y_test = mnist['y_test'][mnist["y_test"]>=8]
eight_and_nine = mnist['x_train'][mnist["y_train"]>=8]

x_train = np.array([img.reshape((784,)) for img in x_train])
x_test = np.array([img.reshape((784,)) for img in x_test])

clf = LinearDiscriminantAnalysis()
f_train = clf.fit_transform(x_train, y_train)

s_train = clf.score(x_train, y_train)
s_test = clf.score(x_test, y_test)

print("Performance of training", s_train)
print("Performance of testing", s_test)

fig = plt.figure(figsize=(9,6), dpi=80)
for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(eight_and_nine[i], cmap='Greys')
plt.show()