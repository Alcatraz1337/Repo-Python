import numpy as np
import matplotlib.pyplot as plt
from timeit import timeit
class SimpleLinearRegression1:

    def __init__(self):
        """初始化Simple Linear Regression 模型"""
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        """根据训练数据集x_train,y_train训练Simple Linear Regression模型"""
        assert x_train.ndim == 1, \
            "Simple Linear Regressor can only solve single feature training data."
        assert len(x_train) == len(y_train), \
            "the size of x_train must be equal to the size of y_train"

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = 0.0
        d = 0.0
        for x, y in zip(x_train, y_train):
            num += (x - x_mean) * (y - y_mean)
            d += (x - x_mean) ** 2

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        """给定待预测数据集x_predict，返回表示x_predict的结果向量"""
        print("x_predict.ndim=", x_predict.ndim)
        assert x_predict.ndim == 1, \
            "Simple Linear Regressor can only solve single feature training data."
        assert self.a_ is not None and self.b_ is not None, \
            "must fit before predict!"

        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        """给定单个待预测数据x，返回x的预测结果值"""
        return self.a_ * x_single + self.b_

    def __repr__(self):
        return "SimpleLinearRegression1()"

class SimpleLinearRegression2():
    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        assert x_train.ndim == 1, \
            "Simple Linear Regressor can only solve single feature training data."
        assert len(x_train) == len(y_train), \
            "the size of x_train must be equal to the size of y_train"

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)

        num = (x_train - x_mean).dot(y_train - y_mean)
        d = (x_train - x_mean).dot(x_train - x_mean)

        self.a_ = num / d
        self.b_ = y_mean - self.a_ * x_mean

        return self

    def predict(self, x_predict):
        """给定待预测数据集x_predict，返回表示x_predict的结果向量"""
        assert x_predict.ndim == 1, \
        "Simple Linear Regressor can only solve single feature training data."
        assert self.a_ is not None and self.b_ is not None, \
        "must fit before predict!"

        return np.array([self._predict(x) for x in x_predict])

    def _predict(self, x_single):
        """给定单个待预测数据x，返回x的预测结果值"""
        return self.a_ * x_single + self.b_

    def __repr__(self):
        return "SimpleLinearRegression2()"

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 3, 2, 3, 5])
reg1 = SimpleLinearRegression1()
reg1.fit(x, y)
x_predict = [8,9,10]
reg1.predict(np.array(x_predict))
y_hat1 = reg1.predict(x)
plt.scatter(x, y)
plt.plot(x, y_hat1, color = 'r')
plt.axis([0,6,0,6])
plt.show()

reg2 = SimpleLinearRegression2()
reg2.fit(x, y)
x_predict = [8,9,10]
reg2.predict(np.array(x_predict))
y_hat2 = reg2.predict(x)
plt.scatter(x, y)
plt.plot(x, y_hat1, color = 'r')
plt.axis([0,6,0,6])
plt.show()

m = 1000000
big_x = np.random.random(size = m)
big_y = big_x * 2 + 3 + np.random.normal(size = m)
timeit(reg1.fit(big_x, big_y))