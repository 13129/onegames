# -*- coding:utf-8 -*-
import pygame
from sys import exit  # 用到exit() 省的每次退出都有红字提示
from pygame.locals import *

class Keycontral(object):
    def __init__(self):
        pygame.init()
        self.scene = pygame.display.set_mode((400, 600))
        pygame.display.set_caption('按键测试')
        self.back = pygame.image.load('ss.png').convert_alpha()
        self.key_a_count = 0  # 记录 a 键 按下的次数
        self.interval = 200  # 毫秒# 双击键最大间隔
        self.firsttime=None
        self.lasttime=None
        self.key_down_list = []  # 储存键盘的'上下左右'键，控制飞机移动
        self.rightcount = 1
        self.leftcount = 1

    def move(self, direction):
        if direction == "RIGHT":
            self.rightcount += 1
        elif direction == "LEFT":
            self.leftcount += 1
    # 储存按键到列表
    def key_down(self, key):
        self.firsttime=pygame.time.get_ticks()#按下时间
        self.key_down_list.append(key)
    def key_up(self, key):
       self.lasttime=pygame.time.get_ticks()#弹起时间


    def press_move(self):
        if len(self.key_down_list) != 0:#有按键才会进入
            if self.key_down_list[0] == pygame.K_LEFT:
                self.move('LEFT')
            elif self.key_down_list[0] == pygame.K_RIGHT:
                self.move('RIGHT')


    def keyTest(self):
        while True:
            for event in pygame.event.get():
                # 退出程序
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                # 按键测试开始，按键被按下
                # 判断事件类型是否是键盘按下事件
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.key_down(pygame.K_LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.key_down(pygame.K_RIGHT)
                        # 判断事件类型是否是键盘松开事件
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.key_up(pygame.K_LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.key_up(pygame.K_RIGHT)

            self.scene.fill((255, 255, 255))
            self.press_move()
            pygame.display.update()


if __name__ == "__main__":
    demo1 = Keycontral()
    demo1.keyTest()
