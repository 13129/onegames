# -*- coding:utf-8 -*-
import imageio
import os
import sys
import re

def sort_key(s):
    # 排序关键字匹配
    # 匹配开头数字序号
    if s:
        try:
            c = re.findall('^\d+', s)[0]
        except:
            c = -1
        return int(c)

def strsort(alist):
    alist.sort(key=sort_key)
    return alist


def create_gif(source, name, duration):
    """
     生成gif的函数，原始图片仅支持png
     source: 为png图片列表（排好序）
     name ：生成的文件名称
     duration: 每张图片之间的时间间隔
    """
    frames = []  # 读入缓冲区
    for img in source:
        print(img)
        frames.append(imageio.imread(img))
    imageio.mimsave(name, frames, 'GIF', duration=duration)
    print("处理完成")


def main(or_path):
    """
    or_path: 目标的文件夹
    """
    path = os.chdir(or_path)#改变当前目录，到指定目录
    pic_list = os.listdir()#读取指定目录所有的文件，返回一个列表
    pic_list=strsort(pic_list)
    gif_name = "result.gif"  # 生成gif文件的名称
    duration_time = 0.5
    # 生成gif
    create_gif(pic_list, gif_name, duration_time)




if __name__ == '__main__':
    parm_list = sys.argv
    if len(parm_list) != 2:
        print("请输入需要处理的文件夹！")
    else:
        main(parm_list[1])

