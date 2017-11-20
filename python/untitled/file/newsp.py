#-------------从页面提取文章url-------------------
import newspaper
from newspaper import Article
from bs4 import BeautifulSoup
import urllib.request
import requests
import chardet
from newspaper import Article
import re
import urllib.parse

urls = [
    'http://www.zz3z.net.cn/html/xydt/index.html',
    'http://www.zzbz.net/List/228-1.html',
    'http://zz23z.zzedu.net.cn/xysx/index.shtml',
    'http://www.zzszedu.cn/chuzhong/xyks/',
    'http://www.zz5z.net/post/xw.html',
    'http://www.zz44z.net/xyxw/index.shtml',
    'http://zz19z.zzedu.net.cn/czb/xydt/index.shtml',
    'http://zz2z.zzedu.net.cn/xndt/xyxw/index.shtml',
    ]

a_title = []
a_length = []
for line in urls:
    print('---------------------------------------')
    html = requests.get(url=line.rstrip()).content
    cd = chardet.detect(html)['encoding']
    # 出现ascii 无法识别时处理办法
    print(cd)
    if cd == 'ascii':
        html = requests.get(url=line.rstrip()).text
        print('ascii')
    soup = BeautifulSoup(html, "lxml")
    if soup.title:
        t_title = soup.title.string
    print(line)
    title = soup.find_all('a')
    for a in title:
        a_length.append(len(str(a)))
    average_length = sum(a_length) / len(a_length)
    articals = {}
    for a in title:
        if len(str(a))>average_length and len(str(a.string))>10:
            if 'http' in a['href']:
                articals[a.string] = a['href']
            else:
                url = urllib.parse.urljoin(line.rstrip(), a['href'])
                articals[a.string] = url
    for key,value in articals.items():
        print(key+':'+value)

