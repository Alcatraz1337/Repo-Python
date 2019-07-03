import numpy as np
import matplotlib.pylab as plt
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:, :2]

# plt.scatter(X[:, 0], X[:, 1])
# plt.xlabel("Sepal length")
# plt.ylabel("Sepal width")
# plt.show()

y = iris.target
# plt.scatter(X[y == 0, 0], X[y == 0, 1], color = "red", marker = "*")
# plt.scatter(X[y == 1, 0], X[y == 1, 1], color = "green", marker = "x")
# plt.scatter(X[y == 2, 0], X[y == 2, 1], color = "blue", marker = "o")
# plt.xlabel("Sepal length")
# plt.ylabel("Sepal width")
# plt.title("Iris Sepal Data")
# plt.show()

X = iris.data[:, 2:]
plt.scatter(X[y == 0, 0], X[y == 0, 1], color = 'r', marker = "*")
plt.scatter(X[y == 1, 0], X[y == 1, 1], color = 'g', marker = "x")
plt.scatter(X[y == 2, 0], X[y == 2, 1], color = 'b', marker = "o")
plt.xlabel("Petal length")
plt.ylabel("Petal width")
plt.title("Iris Petal Data")
plt.show()

raw_data_X = [[3.393533211, 2.331273381],
              [3.110073483, 1.781539638],
              [1.343808831, 3.368360954],
              [3.582294042, 4.679179110],
              [2.280362439, 2.866990263],
              [7.423436942, 4.696522875],
              [5.745051997, 3.533989803],
              [9.172168622, 2.511101045],
              [7.792783481, 3.424088941],
              [7.939820817, 0.791637231]
             ]
raw_data_y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

X_train = np.array(raw_data_X)
y_train = np.array(raw_data_y)
# plt.scatter(X_train[y_train == 0, 0], X_train[y_train == 0, 1], color = "red")
# plt.scatter(X_train[y_train == 1, 0], X_train[y_train == 1, 1], color = "green")
# plt.show()

x = np.array([8.09, 3.34])

from math import sqrt

#欧拉距离
distance = [sqrt(np.sum((x_train - x)**2)) for x_train in X_train]
print(distance, '\n')
# distance = [sqrt(np.sum(x_train - x)**2) for x_train in X_train] #original
# print(distance) 上方求和中，顺序出错

#将每个值对应的序号排序，类似于按照值排序了指针
nearest = np.argsort(distance)
k = 6
topK_y = [y_train[i] for i in nearest[:k]]
from collections import Counter
votes = Counter(topK_y)
y_predict = votes.most_common(1)[0][0]
print(y_predict)