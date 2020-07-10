# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *


class MySprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.master_image = None
        # self.image=None
        self.frame = 0  # 帧
        self.old_frame = -1  # 上一帧
        self.frame_width = 1  # 框架高度
        self.frame_height = 1  # 框架宽度
        self.first_frame = 0  # 最后一帧
        self.last_frame = 0  # 下一帧
        self.columns = 1  # 列
        self.last_time = 0
        self.direction = 0  # 方向
        self.velocity = Point(0.0, 0.0)  # 速度

    #X坐标属性
    def _getx(self):
        return self.rect.x
    def _setx(self, value):
        self.rect.x = value
    X = property(_getx, _setx)

    # Y坐标 property
    def _gety(self):return self.rect.y
    def _sety(self, value):self.rect.y = value
    Y = property(_gety, _sety)

    # 位置属性 property
    def _getpos(self):return self.rect.topleft
    def _setpos(self, pos):self.rect.topleft = pos
    position = property(_getpos, _setpos)


    def load(self, filename, width, height, columns):  # 加载精灵图
        self.master_image = pygame.image.load(filename).convert_alpha()
        self.frame_width = width  # 每张图片的大小
        self.frame_height = height  # 高度
        self.rect = Rect(0, 0, width, height)  # 每张图片的高，宽
        self.columns = columns      # 列数
        rect = self.master_image.get_rect()     #尝试自动计算总帧数
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, rate=30):  # 控制播放速度，可以用来控制技能释放速度 或者 攻击速度
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        #仅当当前框架更改时才构建
        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = Rect(frame_x, frame_y, self.frame_width, self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame

    def __str__(self):
        return str(self.frame) + "," + str(self.first_frame) + \
                "," + str(self.last_frame) + "," + str(self.frame_width) + \
                "," + str(self.frame_height) + "," + str(self.columns) + \
                "," + str(self.rect)


class Point(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    # X property
    def getx(self): return self.__x
    def setx(self, x): self.__x = x
    x = property(getx, setx)

    # Y property
    def gety(self): return self.__y
    def sety(self, y): self.__y = y
    y = property(gety, sety)

    def __str__(self):
        return "{X:" + "{:.0f}".format(self.__x) + \
               ",Y:" + "{:.0f}".format(self.__y) + "}"
