provinceSiChuan = {'成都':['都江堰', '聚源'],'绵阳':['某县1', '某县2']}
provinceLiaoNing = {'沈阳':['某县1','某县2'],'大连':['开发区','大黑山']}
provinceHeiLongJiang = {'齐齐哈尔':['某县1','某县2'], '哈尔滨':['某县1','某县2'], '佳木斯':['某县1', '某县2']}
province = {'四川':provinceSiChuan, '辽宁':provinceLiaoNing,'黑龙江':provinceHeiLongJiang}

p = ''
c = ''
x = ''

while p != 'q':
    print('Showing all the provinces: ')
    for p in province: #province
        print(p, end = ' ')
    p = input("Enter Province: ")
    if p in province:
        for city in province[p]: #City
            print(city, end = ' ')
        c = input('Enter City: ')
        if c in province[p]:
            for country in province[p][c]:
                print(country, end = ' ') #country
        else:
            print('No such city')
    else:
        print('No such provice')
            

