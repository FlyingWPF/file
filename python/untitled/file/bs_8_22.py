#--------------------从页面抽取校园资讯链接---------------
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

pattern1 = '校内新闻|新闻动态|校园动态|校园快讯|校园新闻|学校新闻|校园时讯'

with open(web_path) as path :
     lines = path.readlines()
# lines = [
# 'http://www.zz3z.net.cn',
# 'http://www.zz5z.net',
# 'http://www.zzbz.net',
# 'http://zz23z.zzedu.net.cn',
# 'http://www.zzszedu.cn/chuzhong',
# ]
artical_page = {}
for line in lines:
    m+=1
    try:
        html = requests.get(url=line.rstrip()).content
        cd =chardet.detect(html)['encoding']
        #出现ascii 无法识别时处理办法
        if cd =='ascii':
            html = requests.get(url=line.rstrip()).text
            print('ascii')
        print(cd+'     '+str(m))
        soup = BeautifulSoup(html, "lxml")
    except requests.exceptions.ConnectionError:
        print('requests error')
    #soup = BeautifulSoup(html,"html5lib")

    print(line)
    title = ''
    if soup.title:
        title = soup.title.string
        print(title)
    for a in soup.find_all('a'):
        key = a.string
        if isinstance(key, (str, bytes)):
            if re.search(pattern1, key):
                print('**************')
                print(key)
                if 'http' in a['href']:
                    try:

                        print(a['href'])
                        artical_page[title] = a['href']


                        # a = Article(a['href'], language='zh')
                        # a.download()
                        # a.parse()
                    except newspaper.article.ArticleException:
                        print('failed with 404 Client Error: Not Found for url')
                    print(a.text)
                else:
                    url = urllib.parse.urljoin(line.rstrip(), a['href'])
                    # a = Article(url, language='zh')
                    # a.download()
                    # a.parse()
                    #artical_page.append(url
                    artical_page[title] = url

                    print(url)


                print('**************')

print('----------------------------------------------')

print(artical_page)

