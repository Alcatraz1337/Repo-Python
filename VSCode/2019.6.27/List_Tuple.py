#[]是列表
#列表中什么类型都可以放
# aList = [0, "1", '2', None, 1.2] #下标相邻且连续
# print(len(aList))

# a = [0,1,2,3,4,5,6,7,8,9]
# a[::-1] #后面再加一个冒号表示隔2个取

# a[:2] = a[3:5]
# a

# a[0] = [1,2,3]
# a#列表中可以加列表

# a[0][1] #按照二位数组的方式访问

# a[0] = 0
# a #列表中的列表也可以换成数字

# a[:2] = [2] #列表中的[0,1]被换成了[2]
# a

# a[:2] = [1,1,1,1,1]
# a

# a=[0,1,2,3,4,5,6,7,8,9]
# del a[1] #删除操作
# del a[:2]
# a

# a += [0,1,2,3,4] #可以做加法 
# a

# #但是不能做减法 和 除法

# a *2 #输出两次
# a

# 10 in a #判断元素是否在列表之中

# for i in a:
#     print(i)

# Sum = 0
# Max = 0
# a = [None] * 10
a = []
for i in range(10):
    a.append(int(input("in"))) #append将内容输入至列表之中

print(sum(a) / 10)
print(max(a))

# for i in a:
#     Sum += i
#     if(i > Max):
#         Max = i

# avg = Sum / 10
# print(Max, avg)

len(list)
max(list)
min(list)
list(seq)

list.append()
list.count()
list.extend()
list.index() #列表中找出某个值第一次匹配的索引位置
list.insert(index, obj)
list.pop(obj = list[-1])
list.remove(obj)
list.reverse()
list.sort([func])
list.clear()
list.copy()

a = [1,2,3,4]
a.extend([5])
print(a)
a.append([5,6,7])
print(a)

a.index(2),
a.insert(3, 2.2)
a.pop()
a.remove(2.2)
a.reverse()
a.sort()
print(a)
b = a.copy()
a.clear()
a, b

#元组() tuple

print(r'D:\application') #r代表原始字符串
print(r"Let's go")

t = (1, 2, 3, 4, 5)
#元组没法直接靠取下标来修改，只能通过构造新的元组来拼接出一个新的
tnew = t[:2] + (1,) + t[3:] #()中的元素后方加一个','来表示是一个元组内容
print(tnew)

print(tnew[-2::-1])
#元组没法直接将一个元素给删除，只能通过del来将整个元组给删除
del tnew

L = [1,2,3]
tuple(L)
L[1] = (2,)
print(L)

range()#生成一个整数序列，可以通过在参数中添加括号来表示生成的范围
range(5,8)
range(1,10,2)#可以规定步长
for i in range(9,1,-2):
    print(i)

