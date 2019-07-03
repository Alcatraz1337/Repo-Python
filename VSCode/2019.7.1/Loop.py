for i in range(1, 6): #在1到5行内
    for j in range(6 - i, 0, -1): #递减操作
        print(' ', end = '')
    for j in range(i):
        print('* ', end = '')
    print()


stra = ''
for i in range(1, 6):
    stra += ' ' * (6 - i) + '* ' * i + '\n'
print(stra)

L = [1]
while count <= 6:
    L = [x+y for x, y in zip([0] + L, L + [0])]
for t in range(1,6):
    for i in range(6 - i, 0, -1):
        print(' ', end = '')
    for j in range(len(L[t])):
        print(L[t][j], end = ' ')
    print()

#break 只可用于终止循环

for row in range(9):
    for col in range(row):
        print(row, ' x ', col, ' = ', row * col)

    



