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

    #图片拼接
    def imgsplice(self, filename):
        for i in range(self.start,self.end+1):
            #打开文件，转换图片模式
            a = Image.open('{}.png'.format(i))
            # a=a.convert('RGBA')
            self.imglist.append(a)
        # print(self.imglist[1].show())

        #新建空白图片，带有透明度通道
        result=Image.new('RGBA',(self.imglist[0].size[0]*self.rows,self.imglist[0].size[1]*self.cols))
        img_sum = self.cols * self.rows#图片数

        print('数量',img_sum,self.cols,self.rows)

        for col in range(0,self.rows):
            for row in range(0,self.cols):
                if img_sum >0:
                    result.paste(self.imglist[img_sum-1],(col* self.imglist[0].size[0],row* self.imglist[0].size[1]))
                    print('具体参数', img_sum)
                    # result.show()
                    img_sum -= 1
        return result.save('%s.png'%filename)#保存文件


    #转化成透明图片，以第一个像素颜色为基准
    def transparency(self,imgfilename):
        imgs = Image.open('%s.png'%imgfilename)
        img = imgs.convert('RGBA')
        L, H = imgs.size
        color_0 = img.getpixel((0, 0))
        for h in range(H):
            for l in range(L):
                dot = (l, h)
                color_1 = img.getpixel(dot)
                if color_1 == color_0:
                    color_1 = color_1[:-1] + (0,)
                    img.putpixel(dot, color_1)
        img.save('0011.png')

name='' #图片保存名称
img=ImageDeal(0,1,1,2)  #（起始数字,结束数字,宽==*列数,高==*行数）
img.imgsplice('pinjie')#    拼接后的图片
img.transparency('pinjie')#需要处理的透明图片

