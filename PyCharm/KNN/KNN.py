import numpy as np
import matplotlib .pyplot as plt
from sklearn import  datasets

iris = datasets.load_iris()
X = iris.data[:, :2]

plt.scatter(X[:, 0], X[:, 1])
plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.show()
