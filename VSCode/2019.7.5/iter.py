# def do_iter(ls):

#     try:
#         it = iter(ls)
#         flag = True
#         while flag:
#             try:
#                 print(next(it))
#             except StopIteration as e:
#                 flag = False
#                 print(e)
#     except TypeError as t:
#         print(t)


# def sumii(*x):
#     return x[0] + x[1]


# X = sumii(2, 1)
# print(X)

# hero("小黑", 150)

# from mathutil import circle
# result = circle.circle(5)
# print(result)

# num = 1


# def print_num():
#     # num = 456
#     global num
#     print("1======", num)
#     num = 123
#     print('2======', num)


# print('3=====', num)
# print_num()

# def func_a():
#     sumi = 10
    
#     def fun_b():
#         nolocal sumi
#         print(sumi)


# def fact(num):
#     if num == 1:
#         return 1
#     else:
#         return num * fact(num - 1)

# # def fact2(num):
# #     yield
    


# # result = fact2(5)
# # print(result)

# result = lambda x: 1 if x==1 else x * result(x - 1)

# print(result(5))


# print(result(2, 3))

from hero import Hero

h = Hero("xiaohei", 200, 100, "speed")
h.say_hello()