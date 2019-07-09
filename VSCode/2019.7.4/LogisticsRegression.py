import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.datasets import make_gaussian_quantiles
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# #模拟数据集
import numpy as np
import matplotlib.pyplot as plt

# 随机生成数据集
np.random.seed(666)
X = np.random.normal(0, 1, size=(200, 2))
print(X.shape)
y = np.array(X[:, 0] ** 2 + X[:, 1] ** 2 < 1.5, dtype='int')
noiseX = [-2, 2]
# noiseY = [0]
p_arr = np.concatenate((p_arr,[p_]))
X = np.concatenate((X, [2, 2]))
X = np.append(X, [2, 2])
XCopy = list(X)
XCopy.append(np.array([2, 2]))
X = np.array(XCopy)
y = np.append(y, 1)
print(X)
print(y)
plt.scatter(X[y == 0, 0], X[y == 0, 1])
plt.scatter(X[y == 1, 0], X[y == 1, 1])
plt.show()
#
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
#
# # 分割训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
#
logReg = LogisticRegression(solver='liblinear')
logReg.fit(X_train, y_train)
print(logReg.score(X_train, y_train))
score = logReg.score(X_test, y_test)
print(score)


# 决策边界
def plot_decision_boundary(model, axis):
    x0, x1 = np.meshgrid(
        np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 100)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1, 1),
    )
    X_new = np.c_[x0.ravel(), x1.ravel()]
    y_predict = model.predict(X_new)
    zz = y_predict.reshape(x0.shape)
    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])
    plt.contourf(x0, x1, zz, linewidth=5, cmap=custom_cmap)


plot_decision_boundary(logReg, axis=[-4, 4, -4, 4])
plt.scatter(X[y == 0, 0], X[y == 0, 1])
plt.scatter(X[y == 1, 0], X[y == 1, 1])
plt.show()
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


# 多项式逻辑回归代价函数
def PolynomialLogisticRegression(degree):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('logReg', LogisticRegression())
    ])


polyLogReg = PolynomialLogisticRegression(degree=6)
polyLogReg.fit(X_train, y_train)
# polyLogReg.score(X_train, y_train)
print(polyLogReg.score(X_test, y_test))
plot_decision_boundary(polyLogReg, axis=[-4, 4, -4, 4])
plt.scatter(X[y == 0, 0], X[y == 0, 1])
plt.scatter(X[y == 1, 0], X[y == 1, 1])
plt.show()


polyLogReg2 = PolynomialLogisticRegression(degree=10)
polyLogReg2.fit(X_train, y_train)
polyLogReg2.score(X_train, y_train)
polyLogReg2.score(X_test, y_test)
plot_decision_boundary(polyLogReg2, axis=[-4, 4, -4, 4])
plt.scatter(X[y == 0, 0], X[y == 0, 1])
plt.scatter(X[y == 1, 0], X[y == 1, 1])
plt.show()

# 多项式逻辑回归梯度下降
def PolynomialLogisticRegression(degree, C):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('logReg', LogisticRegression(C=C))
    ])


poly_logReg3 = PolynomialLogisticRegression(degree=20, C=0.1)
poly_logReg3.fit(X_train, y_train)
poly_logReg3.score(X_train, y_train)
poly_logReg3.score(X_test, y_test)
plot_decision_boundary(poly_logReg3, axis=[-4, 4, -4, 4])
plt.scatter(X[y == 0, 0], X[y == 0, 1])
plt.scatter(X[y == 1, 0], X[y == 1, 1])
plt.show()



