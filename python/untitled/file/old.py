# -*- coding: utf-8 -*-

from time import sleep
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

# 获得关于学校的简介
#def getSchoolIntrInfo(searchUrl):

# 获得学校的地址与联系方式
def getSchoolAddInfo(searchUrl):
    html = urlopen(searchUrl)
    bs = BeautifulSoup(html.read().decode('gbk'), 'html.parser')
    div = bs.find("div", {"class": "bottom"})
    linkInfo = div.text
    with open(filename,'a',encoding='utf-8') as file_object:
        file_object.write(linkInfo)
        file_object.write("\n")
    #print(linkInfo)

if __name__ == "__main__":
    url = "http://www.hj6z.com/index.aspx"
    filename = 'D:\collect.txt'
    file_path = 'D:\webset.txt'
    with open(file_path) as file_object:
        for line in file_object:
            print(line)
            getSchoolAddInfo(line)



    #filename= 'collect.txt'
   # getSchoolAddInfo(url)

