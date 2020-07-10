# -*- coding:utf-8 -*-
from os import listdir
from PIL import Image
#图形合并
im_list=[]
for i in range(0,2,1):
    im_list.append(Image.open('%s.png'%i))
print(im_list[0].size[0])
print(im_list)
# 图片转化为相同的尺寸
# 创建空白长图7*22=154,330.244
result = Image.new('RGBA', (496, 116*2))
print(result)
# 拼接图片
for j in range(0,1):#宽坐标
    for i in range(0,2):#高坐标
        result.paste(im_list[i],(j * 496,i * 116))
#行数，列数，
# (width,0)(width,0)
result.save('22.png')

