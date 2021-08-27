#coding=utf-8
import urllib.request
import urllib
import re
import os
import time
import random
from bs4 import BeautifulSoup

class pictures:

    #正则表达式，定位所有图片
    
    def getPng(html):
        reg_png=r'data-src="(https://.*/[0-9]{1,3}.png)"'
        imgre=re.compile(reg_png)
        imglist=imgre.findall(html)
        print("png数组长度：")
        print(len(imglist))
        return imglist
        '''
        reg_png=r'data-src="(https://mmbiz.qpic.cn/mmbiz_png.{5,200}\=png)"'
        imgre=re.compile(reg_png)#编译一下，提升运行速度
        imglist=imgre.findall(html)#匹配
        return imglist
        '''
    
    def getJpg(html):
        #注意jpeg格式图片和png格式图片在资源地址上的诸多不同
        #reg_jpg=r'data-src="(https://i1.kspcdn.xyz/galleries/1974283/[0-9]{1,3}.jpg)"'
        reg_jpg=r'data-src="(https://.*/[0-9]{1,3}.jpg)"'
        imgre=re.compile(reg_jpg)
        imglist=imgre.findall(html)
        print("jpg数组长度：")
        print(len(imglist))
        return imglist
        
        
    #对文件指定位置存放
    def reserve_pictures(imglist,paths):
        print("准备")
        num = 0
        filterlist=[]
        
        for img in imglist:
            try:
                print("\n",img,"\n")
                #urllib.request.urlretrieve(img,'{}{}.jpg'.format(paths,num))
                opener = urllib.request.build_opener()
                opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
                urllib.request.install_opener(opener)
                num = num + 1
                urllib.request.urlretrieve(img,'{}{}.jpg'.format(paths,num))

                #time.sleep(random.randint(2,5))   #随机睡一会
            except Exception as e:
                print(e)
                

            
        print("该格式图片已爬取完毕")
        return num

