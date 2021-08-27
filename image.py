#coding=utf-8
import urllib.request
import urllib
import re
import os
from bs4 import BeautifulSoup

class pictures:

    #正则表达式，定位所有图片
    '''
    def getPng(html):
        reg_png=r'data-src="(https://mmbiz.qpic.cn/mmbiz_png.{5,200}\=png)"'
        
        imgre=re.compile(reg_png)#编译一下，提升运行速度
        imglist=imgre.findall(html)#匹配
        return imglist
    '''
    def getJpg(html):
        #注意jpeg格式图片和png格式图片在资源地址上的诸多不同
        reg_jpg=r'data-src="(https://i1.kspcdn.xyz/galleries/1974283/{1,200}.jpg)"'
        imgre=re.compile(reg_jpg)
        imglist=imgre.findall(html)
        return imglist
        
        
    #对文件指定位置存放
    def reserve_pictures(imglist,paths):
        print("准备")
        num=0

        filterlist=[]
        
        for img in imglist:
            if img in filterlist:
                continue
            num=num+1
            print("\n",img2,"\n")
            urllib.request.urlretrieve(img,'{}{}.jpg'.format(paths,num))
        print("jpg格式图片已爬取完毕")
        return num
