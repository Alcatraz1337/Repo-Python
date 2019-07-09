from urllib import request
from lxml import etree
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import gevent
from gevent import monkey

monkey.patch_all()
plt.rcParams['font.sans-serif'] = ['SimHei']


##获取网页
def get_html(url, code):
    response = request.urlopen(url)
    html = response.read().decode(code)
    html = etree.HTML(html)
    html = etree.ElementTree(html)
    return html


##获取关键字段的信息列表
def get_list(html):
    datas = html.xpath('//div[@id="resultList"]/div[@class="el"]')
    list = []
    for i, data in enumerate(datas):
        data = etree.ElementTree(data)
        title = data.xpath('/div/p/span/a/@title')[0]
        name = data.xpath('/div/span/a/text()')[0]
        city = data.xpath('/div/span[2]/text()')[0]
        city = city if city else None
        wage = data.xpath('/div/span[3]/text()')
        wage = wage[0] if wage else None
        date = data.xpath('/div/span[4]/text()')[0]
        link = data.xpath('/div/p/span/a/@href')[0]
        html2 = get_html(link, 'gbk')
        text = html2.xpath('//p[@class="msg ltype"]/text()')
        exp = text[1].strip() if text else None
        xueli = text[2].strip() if text else None
        head = [title, name, city, wage, date, exp, xueli]
        list.append(head)
    return list


##把列表信息写入并保存为CSV文件
def write_row(filename, writetype, list):
    with open(filename, writetype, newline='') as filename:
        writer = csv.writer(filename)
        print(list)
        writer.writerows(list)
    ##写入字段标题名


def write_header(filename, writetype):
    with open(filename, writetype, newline='') as filename:
        writer = csv.writer(filename)
        writer.writerow(('职位', '公司', '城市', '工资', '发布日期', '经验要求', '学历'))

    # 利用gevent并发和for循环完成1~10页的信息爬取


def grab_one_page(url):
    html = get_html(url, 'gbk')
    list = get_list(html)
    write_row('jobs2.csv', 'w', list)


write_header('jobs2.csv', 'w')
tasks = []
for n in range(3,5):
    url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(n)
    task = gevent.spawn(grab_one_page, url)
    tasks.append(task)
# url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,Python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(1)
# task = gevent.spawn(grab_one_page, url)
# tasks.append(task)
# print(tasks)

gevent.joinall(tasks)
