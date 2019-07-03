if 条件:
    代码块
elif 条件:
    代码块
else:
    代码块

a = 0
if a == 1:
    print("a = 1")

print("a = ", a)

a = 124123
if a % 2 == 0:
    print('a is even')
else:
    print('a is odd')

a = int(input("input a: "))
b = int(input("input b: "))
if a > b:
    print(a)
else:
    print(b)

a = []
for i in range(5):
    a.append(int(input("Input: ")))

Max = a[0]
for i in a:
    if a[i] > Max:
        Max = a[i]

print(Max)