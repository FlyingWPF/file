from PIL import Image
import urllib.parse
import requests
import io

images1 = {
    'http://p2.cri.cn/M00/33/E2/CqgNOln2dYeASrv2AAAAAAAAAAA344.500x332.jpg',
    'http://pic41.nipic.com/20140511/18712552_182746472000_2.png'
}

def imagefilter2(images1):
    images2 = []
    num = 0
    filedir = ('C:/Users/Administrator/Desktop')
    for url in images1:
        num += 1
        # 拼接网址，由相对网址转换为绝对网址
        headers1 = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) '
                                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                                  'Chrome/56.0.2924.87 Safari/537.36'}
        req = requests.get(url, headers=headers1)
        tmpIm1 = io.BytesIO(req.content)
        try:
            im1 = Image.open(tmpIm1)
        except OSError :
            continue
        x = im1.size[0]
        y = im1.size[1]
        scale = x / y
        im2 = im1.resize((600,round(600/scale)))
        p1 = url.rindex('/')
        picpath = filedir + url[p1:]
        im2.save(picpath)
        print(scale)
        # with open (picpath,'wb') as file :
        #     file.write(im2)
        #     file.close()


        # file1.close()
    return images2






images2 = imagefilter2(images1)
