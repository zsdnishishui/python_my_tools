import os
import random
import threading
import requests
from bs4 import BeautifulSoup
from headers import headers_list

headers = random.choice(headers_list)
htmlUrl = 'https://cl.3525x.xyz/htm_data/2406/16/6333339.html'
html = requests.get(htmlUrl, headers=random.choice(headers_list)).text
# 创建Beautiful Soup对象
soup = BeautifulSoup(html, 'html.parser')
list = []
name = soup.select('h4[class="f16"]')[0].get_text()
# 提取链接
img = soup.find_all('img')
for i in img:
    if i.has_attr('ess-data'):
        list.append(i['ess-data'])
        # print(i['ess-data'])
dir = 'd:/Temp/img/' + str(name);
if not os.path.exists(dir):
    os.makedirs(dir)

print("总共 %d 张照片" % (len(list)))


def downLoad(i, url, dir):
    # print(url)
    file = url.split("/")[-1]
    try:
        r = requests.get(url, headers=random.choice(headers_list))
    except:
        for j in range(4):  # 循环去请求网站
            r = requests.get(url, headers=random.choice(headers_list))
            if r.status_code == 200:
                break

    # 下载图片
    with open(dir + '/' + file, mode="wb") as f:
        f.write(r.content)  # 图片内容写入文件
        print('已下载第 %d 张' % (i + 1))


for i, url in enumerate(list):
    threading.Thread(target=downLoad, args=(i, url, dir)).start()
    # downLoad(i,url,dir)
