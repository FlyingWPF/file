#-------------------从首页抽取学校地址、联系方式，查找学校简介链接并抽取学校简介------------
import urllib.request
import chardet
import requests
from bs4 import BeautifulSoup
import html5lib
import re
from newspaper import Article
import newspaper
import urllib.parse

line = 'http://www.zz3z.net.cn/'
line2 = 'http://www.zz5z.net/'

m=0
web_path  = '/home/wpf/PycharmProjects/untitled/file/web_path.txt'

pattern1 = '概况|简介|地址'
pattern2 = '地址|联系方式'
with open(web_path) as path :
    lines = path.readlines()


for line in lines:
    m+=1
    html = requests.get(url=line.rstrip()).content
    cd =chardet.detect(html)['encoding']
    print(cd+'     '+str(m))
    #soup = BeautifulSoup(html,"html5lib")
    soup = BeautifulSoup(html, "lxml")
    print(line)
    if soup.title:
        print(soup.title.string)
    regexp = re.compile("地址|电话")
    for b in soup.find_all(text=regexp):
        print(b)
    for a in soup.find_all('a'):
        key = a.string
        if isinstance(key, (str, bytes)):
            if re.search(pattern1, key):
                print('**************')
                print(key)
                if 'http' in a['href']:
                    try:
                        a = Article(a['href'], language='zh')
                        a.download()
                        a.parse()
                    except newspaper.article.ArticleException:
                        print('failed with 404 Client Error: Not Found for url')
                    print(a.text)
                else:
                    url = urllib.parse.urljoin(line.rstrip(), a['href'])
                    a = Article(url, language='zh')
                    a.download()
                    a.parse()
                    print(a.text)
                print('**************')

