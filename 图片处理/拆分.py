# -*- coding:utf-8 -*-
import os
from PIL import Image

im = Image.open('result.gif')
os.mkdir('4boy')
try:
    i = 0
    while True:
        im.seek(i)
        im.save('4boy/' + str(i) + '.png')
        i = i + 1
except:
    pass
print('共拆解图像帧数' + str(i))