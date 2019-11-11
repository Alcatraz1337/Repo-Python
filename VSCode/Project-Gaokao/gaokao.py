from multiprocessing.pool import Pool
import csv
import requests
from bs4 import BeautifulSoup
# import pymongo
import re

# client = pymongo.MongoClient('localhost', 27017)
# gaokao = client['gaokao']
# provice_href = gaokao['provice_href']
# score_detail = gaokao['score_detail']

def write_row(filename, writetype, list):
    with open(filename, writetype, newline = '', encoding = 'utf-8') as filename:
        writer = csv.writer(filename)
        writer.writerow(list)

# 获取省份及链接
pro_link = []
def get_provice(url):
    web_data = requests.get(url, headers=header)
    soup = BeautifulSoup(web_data.content, 'lxml')
    provice_link = soup.select('.area_box > a')
    for link in provice_link:
        href = link['href']
        province = link.select('span')[0].text

        # data = {
        #     'href': href,
        #     'province': province
        # }
        row = [href, province]
        write_row('Province_data.csv', 'a', row)
        pro_link.append(href)
    print('OK')


# 获取分数线
def get_score(url):
    web_data = requests.get(url)
    # web_data = requests.get(url, headers=header)
    soup = BeautifulSoup(web_data.content, 'lxml')
    # 获取省份信息
    province = soup.select('.col-nav span')[0].text[0:-5]
    # 获取文理科
    categories = soup.select('h3.ft14')
    category_list = []
    for item in categories:
        category_list.append(item.text.strip().replace(' ', ''))
    # 获取分数
    tables = soup.select('h3 ~ table')
    for index, table in enumerate(tables):
        tr = table.find_all('tr', attrs={'class': re.compile('^c_\S*')})
        for j in tr:
            td = j.select('td')
            score_list = []
            for k in td:
                # 获取每年的分数
                if 'class' not in k.attrs:
                    score = k.text.strip()
                    score_list.append(score)

                # 获取分数线类别
                elif 'class' in k.attrs:
                    score_line = k.text.strip()

                # score_data = {
                #     'province': province.strip(),#省份
                #     'category': category_list[index],#文理科分类
                #     'score_line': score_line,#分数线类别
                #     'score_list': score_list#分数列表
                # }
                row = [province.strip(), category_list[index], score_line, score_list]
            write_row('Score_data.csv', 'a', row)
        print("detail insert ok")






header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    'Connection': 'keep - alive'}
url = 'http://www.gaokao.com/sichuan/fsx/'
get_provice(url)
get_score(url)
    # pool = Pool()
    # pool.map(get_score, [i for i in pro_link])#使用多线程
