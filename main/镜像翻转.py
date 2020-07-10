# -*- coding:utf-8 -*-
from PIL import Image
import random

def Jpg(dir_line):
    try:
        im = Image.open(dir_line)
    except IOError as er_info:
        print(er_info)
        exit()
    x = im.size[0]
    y = im.size[1]
    img = im.load()
    c = Image.new("RGBA", (x, y))
    for i in range(0, x):
        for j in range(0, y):
            w = x - i - 1
            h = y - j - 1
            rgb = img[w, j]  # 镜像翻转
            # rgb = img[w, h]  # 翻转180度
            # rgv = img[i, h]  # 上下翻转
            c.putpixel([i, j], rgb)
# 90度的翻转实现
#     c.show()
    c.save("1.png")
if __name__ == "__main__":
    name = "pinjie.png"
    Jpg(name)
