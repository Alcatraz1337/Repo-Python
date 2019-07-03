type({}), type({'a'}), type({'a':'单词'})

dicta = {'alpha':'阿尔法'}
dicta['beta'] = '贝塔'
dicta['beta'] = 'β' #会覆盖之前的键值
dicta['beta']

dictb = {'alpha':'阿尔法' , 'beta':'贝塔' , 'beta':'查理'} #键必须唯一
dictb

dictb = {'alpha':'阿尔法' , 'Alpha':'大阿尔法'} #区分大小写
dictb['None'] = '' #可以添加空键值
dictb[''] = 'Empty' #可以添加空键
dictb

choice = ''
phone = {'iPhone':6000 , 'Sony':5000 , 'Samsung':4000, 'BlackBerry':3000}
shoppingCart = {}
while choice != 'q':
    choice = input()
    if choice in phone:
        shoppingCart[choice] = phone[choice]
    else:
        print('Dont have this phone')

del phone #删除整个字典
del phone['iPhone'] #删除一个键
phone.clear() #清空字典，但是保留字典不被删除


stra = 'abc'
stra.replace('a','bc')
stra #str是一个不可变类型

games = ['b', 'a', 'a', 'c', 'b', 'a']
games_new = []
# games = list(set(games)) #直接调整原列表
games_new = [for i in games if i is not in games_new]
games_new

set1 = set([1,2,3])
set2 = set([1,5,6])
set1 = set1 | set2
set1


info = {'CM':('123','DL'), 'TYD':('124', 'DL')}
name = input("Name: ")
address = input("Address: ")
phone = input("Phone: ")
info[name] = (phone, address)

info['CM'] = int(info['CM'][0])

