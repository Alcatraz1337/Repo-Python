col = 1
for row in range(1,10):
    for col in range(1, row+1):
            print(col, '*', row, '=', col * row, end = '  ')    
    print()

stra = [1,2,3,4,5,6]
strb = []
for i in range(len(stra)):
        strb.append(stra[i])
print(strb)

x = 0; y = 1; z = 1; mounth = 24 #兔子问题，x是当月，y是上一个月，z是上两个月
for i in range(3, mounth+1):
        x = y + z
        print("第", i, "月一共有", x * 2, "只兔子")
        z = y
        y = x

a = [6,2,6,8,1,7,9]
Min = a[0]
Length = len(a)
# flag = 0
for i in range(Length - 1):
        Min = i
        for j in range(i + 1, Length):
                if a[Min] > a[j]:
                        Min = j
        a[Min], a[i] = a[i], a[Min]
print(a)
        

for i in range(Length - 1):
        for j in range(0, Length - i - 1):
                if a[j] > a[j + 1]:
                        a[j], a[j + 1] = a[j + 1], a[j]
print(a)

L = (
        ('大侦探皮卡丘','Final Fantasy', '夏日大作战'),
        ('唐顿庄园','Gotham','SHIELD'),
        ('King of Fighters','刀魂','英雄萨姆')
)

arr = [1, 'a', 2, 'b', 3, 'c']
for i in range(len(arr) - 1,-1, -1):
        if type(arr[i]) is str:
                print(arr[i])


[i for j in L for i in j]

