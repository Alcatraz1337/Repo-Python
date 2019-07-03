L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
for i in L:
    print(i[1])

for i,val in enumerate(L):#i 和 val一一对应枚举变量的内容
    print(val[1])

Lnew = [for i in L if j < len(i)]
print(Lnew)
