# -*- coding:utf-8 -*-
from PIL import Image
import os,sys,re


class ReadImage():
    def __init__(self):
        self.all_width = []  # 宽度参数集合
        self.all_height = []  # 高度参数集合
        self.all_para = []
        self.blankmax_w=None   #最大
        self.blankmax_h=None  #最大
        self.imgname=[]

    def image(self):
        pic_list = os.listdir('站立行走')  # 读取指定目录所有的文件，返回一个列表
        for img  in pic_list:
            image_size = Image.open('站立行走/'+str(img))
            # image_size=image_size.convert('RGBA')
            self.all_width.append(image_size.size[0])    #宽度
            self.all_height.append(image_size.size[1])   #高度
            self.all_para.append(image_size)    #列表元组size
        # print(self.blankmax_w, self.all_width)
        self.blankmax_w=max(self.all_width)
        self.blankmax_h=max(self.all_height)
        if self.blankmax_w//2 !=0 and self.blankmax_h // 2 != 0:#尺寸是否为奇数
            self.blankmax_w+=1
            self.blankmax_h += 1
        elif self.blankmax_h//2 !=0:
            self.blankmax_h+=1
        elif self.blankmax_w // 2 != 0:
            self.blankmax_w += 1
        else:
            print('sss')
    def generate(self):
        # os.mkdir('soze')
        cmax_w, cmax_h = self.blankmax_w // 2, self.blankmax_h // 2
        # result=Image.new('RGB',(self.blankmax_w,self.blankmax_h))#每个图片分别创建一个空白图像
        for para in range(0,len(self.all_para)):
            result = Image.new('RGBA', (self.blankmax_w, self.blankmax_h))
            center_w, center_h = self.all_para[para].size[0]//2,self.all_para[para].size[1]//2
            result.paste(self.all_para[para], (cmax_w - center_w, cmax_h - center_h))
            result.save('soze/%s.png'%para)
            # result.show()
            self.imgname.append(Image.open('soze/%s.png'%para))


im=ReadImage()
im.image()
im.generate()



