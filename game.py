# -*- coding:utf-8 -*-
import time
import pygame, sys
import os
from PIL import Image




pygame.init()
pygame.display.set_caption('holle')
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_dog = pygame.image.load("地板.png")
# my_background=pygame.image.load('疾跑/0.png')   #人物图片
names = locals()  # locals() 函数会以字典类型返回当前位置的全部局部变量
balls = []
for i in range(0, 8):
    names['%s' % i] = pygame.image.load("疾跑/%s.png" % i)
    balls.append(names['%s' % i])

for j in range(1,630,63):
    for k in range(200,456,32):
        screen.blit(my_dog, [j,k])


for i in range(0, 8):
    balls[i].set_colorkey((255, 255, 255))  # 背景透明
    screen.blit(balls[i], (1, 200))
    time.sleep(0.05)

pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

