#coding=utf-8
import urllib.request
import urllib
import os
from bs4 import BeautifulSoup
from pictures import pictures as p 
import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import (QFileDialog, QWidget, QLabel, QMessageBox, QPushButton, QTextEdit, QGridLayout, QApplication)


def getHtml(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    req = urllib.request.Request(url=url,headers=headers)
    page = urllib.request.urlopen(req)
    html = page.read()
    return html.decode('UTF-8')

def requestImages(url,paths):
    
    '''
    path_select = input("是否采用默认的图片存储地址？（y/n）：")
    file_name = input("想要将该存储图片的文件夹命名为：")
    
    #文件储存地址设置
    if path_select=="Y" or path_select=="y" or path_select=="Yes" or path_select=="yes":
        #文件夹命名加上天数，以加以区别
        path="e:\\python练习\网站图片爬虫\搜集图片\\" + file_name
    else:
        path=input("请输入文件存储地址（格式为E:\\...\）：")
        if file_name != '':
            path = path + file_name
    
    if not os.path.isdir(path):
        print("默认地址不存在，现在新建了一个文件夹地址")
        os.makedirs(path)
    
    paths = path + '\\'
    '''


    print(u'----------现在开始获取图片---------')
    #打开网页,读取源码
    html = getHtml(url)
    jpgList = p.getJpg(html)
    pngList = p.getPng(html)
    if len(jpgList) != 0:
        p.reserve_pictures(jpgList,paths)
    if len(pngList) != 0:
        p.reserve_pictures(pngList,paths)
    
class Example(QWidget):
    directory_paths = "C:/Users"
    #存储地址，默认C盘

    def __init__(self):
        super().__init__()
        self.initUI()

    def msg(self):
        directory = QFileDialog.getExistingDirectory(None,"选取文件夹","C:/Users")
        #起始的文件夹路径
        print("type(directory) = ",type(directory),"\n directory = ",directory)
        directory_paths = directory

    def initUI(self):
        self.review = QLabel('Please input the web site: ')
        self.reviewEdit = QTextEdit()
        '''
        用QGridLayout模块制作标签和文本编辑窗口
        '''

        grid = QGridLayout()
        #一个QGridLayout类
        #QGridLayout(parent)，在构建新网格布局时必须将其插入父布局，没有则为self。

        grid.setSpacing(10)
        #各个控件之间的间距（包括上下左右）设置为10px
        
        startBtn = QPushButton(text='开始', parent=self)
        #创建一个继承自QPushButton的按钮，用于开始爬虫程序
        startBtn.clicked.connect(self.requestStart)

        folderBtn = QPushButton(text='存储于...', parent=self)
        #创建一个继承自QPushButton的按钮，用于选择文件存储地址
        folderBtn.clicked.connect(self.msg)

        #接下来为组件添加以下控件
        grid.addWidget(self.review)
        grid.addWidget(self.reviewEdit)
        grid.addWidget(startBtn)
        grid.addWidget(folderBtn)
        

        self.setLayout(grid) 
        #设置布局管理器，一个QWidget控件中只能设置一个

        self.setWindowTitle('准备爬虫')    
        self.show()
        
    def requestStart(self):
        #判断网址链接是否为空，或者是否为全空字符串
        if self.reviewEdit.toPlainText() == "" or self.reviewEdit.toPlainText().isspace () == True:
            reply = QMessageBox.question(self, 'Message',"Please input your url correctly.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        else:
            print("开始请求")
            print(self.reviewEdit.toPlainText())
            requestImages(self.reviewEdit.toPlainText(),self.directory_paths)



    
if __name__ == '__main__':
    print(u'---------准备开始网页抓取图片，现在进行准备工作----------')
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())




