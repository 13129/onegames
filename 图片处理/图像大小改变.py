# -*- coding:utf-8 -*-

# !/usr/bin/env python

from PIL import Image, ImageSequence
import sys, os

import imageio

# 需要合在一起的图片
# image_list = [r'../001boy/' + str(x) + ".png" for x in range(0, 153)]
# # gif的图片名
# gif_name = r'动作.gif'
#
# frames = []
# for image_name in image_list:
#     frames.append(imageio.imread(image_name))
#
# # druation : 图片切换的时间，单位秒
# imageio.mimsave(gif_name, frames, 'GIF', duration=0.3)

# if len(sys.argv) < 3:
#     print("input invalid!")
#     print("you need input ingif and outgif.")
#     exit(1)
#
# inf = sys.argv[1]
# outf = sys.argv[2]

gif = Image.open('动作.gif')
dura = gif.info['duration']
print(dura)
imgs = [f.copy() for f in ImageSequence.Iterator(gif)]

index = 0
imglist = []
# os.mkdir("images")
for frame in imgs:
    frame.save("./images/%d.png" % index)
    im = Image.open("./images/%d.png" % index)
    # im.thumbnail((244, 244), Image.ANTIALIAS)
    im=im.resize((244, 244))
    imglist.append(im)
    index += 1

os.system("rm -rf ./images")

imglist[0].save('ss.gif', 'gif', save_all=True, append_images=imglist[1:], loop=0, duration=dura)