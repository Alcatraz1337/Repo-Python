import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import os
path = 'E://GitLocalSource//Project_Python//VSCode//Project-AdmissionPrediction//LogiReg_data.txt'
pdData = pd.read_csv(path, header = None, names = ['Exam 1', 'Exam 2', 'Admitted'])

#查看头部
pdData.head()
pdData.shape

positive = pdData[pdData['Admitted'] == 1]
negative = pdData[pdData['Admitted'] == 0]

#查看数据
fig, ax = plt.subplots(figsize = (10,5))
ax.scatter(positive['Exam 1'], positive['Exam 2'], s = 30, c = 'b', marker = 'o', label = 'Admitted')
ax.scatter(negative['Exam 1'], negative['Exam 2'], s = 30, c = 'r', marker = 'x', label = 'Rejected')
ax.legend()
ax.set_xlabel('Exam 1 Score')
ax.set_ylabel('Exam 2 Score')
plt.show()

pdData.insert(0, 'Ones' , 1)
#获取特征矩阵和标签矩阵
orig_data = pdData.as_matrix()
cols = orig_data.shape[1]
X = orig_data[:, 0:cols - 1]
y = orig_data[:, cols - 1:cols]
theta = np.zeros([1,3])
print(X[:5])
print(X.shape, y.shape, theta.shape)

#sigmoid
def sigmoid(x):
    return 1 / 1(np.exp(-x))

#画图

nums = np.arange(-10, 10, step = 1)
fig, ax = plt.subplots(figsize = (12, 4))
ax.plot(nums, sigmoid(nums), 'r')
plt.show()