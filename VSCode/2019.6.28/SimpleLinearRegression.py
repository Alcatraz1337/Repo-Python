import numpy as np
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
        x_mean_ = np.mean(x_train)
        y_mean_ = np.mean(y_train)

        num = 0
        d = 0
        
        for x_i, y_i in zip(x_train, y_train):
            num += (x_i - x_mean_) * (y_i - y_mean_)
            d += (x_i - x_mean_) ** 2

        self.a_ = num / d
        self.b_ = y_mean_ - self.a_ * x_mean_

        return self

    def predict(self, x_predict):
        """给定待预测数据集x_predict，返回表示x_predict的结果向量"""
        assert x_predict.ndim == 1, \
            "Simple Linear Regressor can only solve single feature training data."
        assert self.a_ is not None and self.b_ is not None, \
            "must fit before predict!"

        y_predict = self.a_ * x_predict + self.b_

        return y_predict
        
       

    def _predict(self, x_single):
        """给定单个待预测数据x，返回x的预测结果值"""
        
        y_single = self.a_ * x_single + self.b_
        return y_single

    def __repr__(self):
        return "SimpleLinearRegression1()"