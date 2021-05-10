import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


mnist = np.load('./l301practice.npz')

x_train = mnist['x_train'][mnist["y_train"]<=2]/255
y_train = mnist['y_train'][mnist["y_train"]<=2]

clf = LinearDiscriminantAnalysis(n_components=(2)) #The n_component = (n_classes -1)
f_train = clf.fit_transform(x_train, y_train)

fig = plt.figure(figsize=(6,6), dpi=80)
for i in range(0,3):
    plt.scatter(f_train[:,0][y_train==i], f_train[:,1][y_train==i], s=50, marker="$"+str(i)+"$", alpha=0.5)
plt.show()

