import numpy as np
import matplotlib.pylab as plt  
import SimpleLinearRegression as SLR

x = np.array([1., 2., 3., 4., 5.])
y = np.array([1., 3., 2., 3., 5.])
# plt.axis([0, 6, 0, 6])

# plt.scatter(x, y)

# x_mean = np.mean(x)
# y_mean = np.mean(y)

# num = 0
# d = 0
# for x_i, y_i in zip(x, y):
#     num += (x_i - x_mean) * (y_i - y_mean)
#     d += (x_i - x_mean) ** 2

# a = num / d
# b = y_mean - a * x_mean

# x_predict = 2.3
# y_predict = a * x + b

# plt.scatter(x_predict, a * x_predict + b, color = "Orange")
# plt.plot(x, y_predict, color = "red")
# plt.show()
slr = SLR.SimpleLinearRegression1()
slr.fit(x, y)
plt.scatter(x, y, color = "blue")
plt.scatter(2.3, slr._predict(2.3), color = "purple")
plt.plot(x, slr.predict(x), color = "red")
plt.show()


