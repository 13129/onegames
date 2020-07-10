# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *


class MySprite(pygame.sprite.Sprite):
    def __init__(self, target):
        pygame.sprite.Sprite.__init__(self)
        self.target_surface = target
        self.image = None
        self.master_image = None
        self.rect = None
        self.topleft = 0, 0
        self.frame = 1
        self.old_frame = -1
        self.frame_width = 1
        self.frame_height = 1
        self.first_frame = 0
        self.last_frame = 0
        self.columns = 1
        self.last_time = 0
        self.speed=3
        self.num=0

    def load(self, filename, width, height, columns):#加载精灵图
        self.master_image = pygame.image.load(filename).convert_alpha()
        print(self.master_image)
        self.frame_width = width    #每张图片的大小
        self.frame_height = height  #高度
        self.rect = 0, 0, width, height #每张图片的高，宽
        self.columns = columns  #列数
        rect = self.master_image.get_rect()
        self.last_frame = (rect.width // width) * (rect.height // height) - 1

    def update(self, current_time, press_keys,rate=500):#控制播放速度，可以用来控制技能释放速度 或者 攻击速度
        if current_time > self.last_time + rate:
            self.frame += 1
            if self.frame > self.last_frame:
                self.frame = self.first_frame
            self.last_time = current_time

        if self.frame != self.old_frame:
            frame_x = (self.frame % self.columns) * self.frame_width
            frame_y = (self.frame // self.columns) * self.frame_height
            rect = (frame_x, frame_y, self.frame_width, self.frame_height)
            print('sads',self.frame,self.columns,self.frame_height)
            self.image = self.master_image.subsurface(rect)
            self.old_frame = self.frame


        self.rect=list(self.rect)
        if press_keys[K_LEFT]:
            self.rect[0] -= self.speed
            if self.rect[0] <= -100:

                self.rect[0] = -100
        if press_keys[K_RIGHT]:
            self.rect[0] += self.speed
            if self.rect[0] >= 480:
                self.rect[0] = 480

        if press_keys[K_UP]:
            self.rect[1] -= self.speed

            if self.rect[1] <= -90:
                self.rect[1] = -90
        if press_keys[K_DOWN]:
            self.rect[1] += self.speed
            if self.rect[1] >= 240:
                self.rect[1] = 240

        screen.blit(self.image, self.rect)


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("精灵类测试")
font = pygame.font.Font(None, 18)
framerate = pygame.time.Clock()

cat = MySprite(screen)
cat.load('普通行走1.png',330,244,5)
group = pygame.sprite.Group()
group.add(cat)

while True:

    framerate.tick(60)
    ticks = pygame.time.get_ticks()
    print(ticks)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    press_keys = pygame.key.get_pressed()
    if press_keys[pygame.K_ESCAPE]:
        exit()
    screen.fill((255,255,255))#
    my_dog=pygame.image.load("地板.png")
    for j in range(1, 630, 63):
        for k in range(200, 456, 32):
            screen.blit(my_dog, [j, k])

    group.update(ticks,press_keys)
    group.draw(screen)
    pygame.display.update()