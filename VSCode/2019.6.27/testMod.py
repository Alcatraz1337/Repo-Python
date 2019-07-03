print(10 % 3)
print(-10 % 3)
print(-10 % -3)
print(10 % -3)

print(27 / 10)
print(27 / -10)
print(-27 / 10)
print(-27 / -10)
print(27 // 10)
print(27 // -10)
print(-27 // -10)
print(-27 // 10)

a = 9
0 < a < 10 #区间判断

#python中没有 && 来表示 且， 而是用 and 关键字
# & 是位运算的且, | 是按位或

#and 讲究就近原则
2 & 3, 2 | 3, 2 and 3, 0 and 2, 2 and 0

#判断是否在范围之中
1 not in (1, 2, 3, 4)

#is用于判断绝对相等，包括类型和值
1 is True, 1 == True

#python也有优先级
x = 3
x = bool(x) == True
x

x = 1
y = 2
z = 3
x += y + z
x

stra = 'hello world'
stra[0], stra[5], stra[10], #stra[11]越界
stra[2:12] #越界了的部分不会被访问，所以， ： 后面的部分可以不写，来表示渠取到末尾
stra[2:-1] #取到最后一位的前一位

stra[10], stra[10:], stra[-1], stra[-1:]

for i in (0,1,2,3,4,5,6,7,8,9,10,11): #for循环之后要加':'，且没有花括号标志一个块，退出
    print(stra[i+1:], stra[:i])        #需要回车退出


