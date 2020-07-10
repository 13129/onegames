# -*- coding:utf-8 -*-
from os import listdir
from PIL import Image

#图片处理
class ImageDeal():
    def __init__(self,start,end,rows,cols):
        self.end=end    #结束
        self.start=start    #开始
        self.rows=rows  #行数
        self.cols=cols  #列数
        self.imglist=[]

    #拼接
    def imgsplice(self, filename):
        for i in range(self.start,self.end+1):
            self.imglist.append(Image.open('/{}.png'.format(i)))
        result=Image.new('RGB',(self.imglist[0].size[0]*self.cols,self.imglist[0].size[1]*self.rows))
        for i in range(0,self.cols):
            for j in range(0,self.rows):
                result.paste(self.imglist[i],(i* self.imglist[0].size[0],j* self.imglist[0].size[1]))
        result.save('%s.png'%filename)
    def transparency(self,imgfilename):
        imgs = Image.open('%s.png'%imgfilename)
        img = imgs.convert('RGBA')
        L, H = img.size
        color_0 = img.getpixel((0, 0))
        for h in range(H):
            for l in range(L):
                dot = (l, h)
                color_1 = img.getpixel(dot)
                if color_1 == color_0:
                    color_1 = color_1[:-1] + (0,)
                    img.putpixel(dot, color_1)
        img.save('%s1.png'%imgfilename)

name='' #图片保存名称
img=ImageDeal(124,132,1,8)  #（起始数字,结束数字,行数,列数）
img.imgsplice('pinjie')
img.transparency('pinjie')

