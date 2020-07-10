# -*- coding:utf-8 -*-
from  PIL import Image
import os
from termcolor import *
# 以第一个像素为准，相同色改为透明
def transparent_back(img):
    img = img.convert('RGBA')

    L, H = img.size
    color_0 = img.getpixel((0, 0))
    for h in range(H):
        for l in range(L):
            dot = (l, h)
            color_1 = img.getpixel(dot)
            if color_1 == color_0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot, color_1)
    return img
# os.mkdir('001')
if __name__ == '__main__':

    for i in range(1,4):
        img = Image.open('./00%s.png'%i)
        img = transparent_back(img)
        img.save('%s.png'%i)
        print(colored('保存成功%s'%i,'red','on_blue'))
