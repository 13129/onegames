# -*- coding:utf-8 -*-
from PIL import Image, ImageDraw
import numpy as np
import termcolor,os
#处理非透明部分的最小外接区域，并可以透明化
def edge(img):
    np_data = np.array(img)
    rr = np.where(np_data[:, :, 3] != 0)#判断
    xmin = min(rr[1])
    ymin = min(rr[0])
    xmax = max(rr[1])
    ymax = max(rr[0])
    return xmin, ymin, xmax, ymax
# os.mkdir('003')
# os.mkdir('005')
if __name__ =='__main__':
# for i in range(0,153):
    img = Image.open('0.png')
    img = img.convert('RGBA')
    img_edge = edge(img)
    print(img_edge)
    draw=ImageDraw.Draw(img)
    draw.rectangle((img_edge),outline='red')
    img.show()
    # region=img.crop(img_edge)#裁剪图像,参数，x,y,x+width,y=height
    # region.save('003.png')
    # for jj in range(0,153):
    #     imgs = Image.open('003/%s.png' % jj)
    #     img=imgs.convert('RGB')
    #     img.save('005/%s.png'%jj)
ass={(43,122),(39,113),(46,113),(46,114),
     (46,114),(45,115),(61,115),(52,114)}

max_width=61
mx_height=115
#im.paste(image, box)
max=(62,116)