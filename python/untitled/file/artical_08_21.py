#----------------------从文章抽取正文-------------
import urllib.request
import urllib.parse
import re
from PIL import Image
import io, urllib
from newspaper import Article
import chardet
import requests
from bs4 import BeautifulSoup
import os

def pic_filter(url1,url2):
    #拼接网址，由相对网址转换为绝对网址
    url3 = urllib.parse.urljoin(url1,url2)
    file1 = urllib.request.urlopen(url3)
    tmpIm1 = io.BytesIO(file1.read())
    im1 = Image.open(tmpIm1)
    x = im1.size[0]
    y = im1.size[1]
    scale = x/y
    if x>300 and y>300 and scale<2:
       # print('ok: '+url3)
        images.append(url3)


lines = [
    'http://www.zz3z.net.cn/html/2017-06/2326.html',
    'http://www.zz5z.net/post/1067.html',
    'http://www.zzbz.net/View/3297.html',
    'http://zz23z.zzedu.net.cn/xysx/2017/06/219710.shtml',
    'http://www.zzszedu.cn/chuzhong/xyks/2013716/181.htm',
    'http://www.zz44z.net/xyxw/2017/06/219688.shtml',
    'http://zz19z.zzedu.net.cn/czb/xydt/2017/08/224264.shtml',
    'http://zz2z.zzedu.net.cn/xndt/xyxw/2017/05/217148.shtml',

    ]

i = 0
n = 0
pic = []
imglist = []
for line in lines:
    images = []
    imglist = []
    i=0
    n+=1
    filedir = ('/home/wpf/Pictures/web/%s' %n)
    if os.path.exists(filedir):
        if os.listdir(filedir):
            for file in os.listdir(filedir):
                os.remove(filedir+'/'+file)
        os.rmdir(filedir)
    os.makedirs(filedir)
    print('------------%d-----------' %n)
    print(line)
    #利用request 下载页面
    page = urllib.request.urlopen(line)
    html1 = page.read().decode('utf-8','ignore')
    html = requests.get(url=line.rstrip()).content
    soup = BeautifulSoup(html, "html5lib")
    #正则找出图片url
    reg = r'src="(.+?\.jpg)"'
    imgre = re.compile(reg)
 #  imglist = imgre.findall(html.decode('utf-8','ignore'))
    imglist = imgre.findall(html1)
    #过滤图片
    for url1 in imglist:
        pic_filter(line,url1)

    # #保存图片
    # for pic in images:
    #     i+=1
    #     urllib.request.urlretrieve(pic,(filedir+'/%s.jpg'%(i)))

    print(soup.title.string)
    a = Article(line, language='zh')
    a.download()
    a.parse()
    artical = a.text.splitlines()
    #artical = a.text.split(' ')
    #print(artical)
    while '' in artical:
        artical.remove('')
    t_re = re.match("[\u4e00-\u9fa5]+", soup.title.string)
    til = t_re.group()
    if til != artical[0] and til.find(artical[0])==-1:
        artical.insert(0,til)
    a_length = []
    #计算平均长度
    for sentence in artical:
        a_length.append(len(sentence))
    average_length = sum(a_length)/len(a_length)
    #倒序排列列表
    artical1 = artical[::-1]
    #插入图片
    sentence1 = ''
    index = 0
    for sentence in artical1:
        if sentence1 == sentence:
            index -=1
        else:
            sentence1 = sentence
            #标题重复时定位标题位置
            index = len(artical1) - artical1.index(sentence)-1
        if len(sentence) < average_length and len(sentence) < 30  and images != []:
            artical.insert(index, images.pop())

    for i in artical:
        print(i)

