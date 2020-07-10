# -*- coding:utf-8 -*-
import itertools, sys, time, random, math, pygame
from pygame.locals import *
from main.mylibrary import MySprite,Point

#走路方向
def calc_velocity(direction, vel=1.0):
    velocity = Point(0, 0)
    # if direction == 0:  # 上
    #     velocity.y = -vel
    if direction == 1:  # 右
        velocity.x = vel
    # elif direction == 1:  # 下
    #     velocity.y = vel
    elif direction == 0:  # 左
        velocity.x = -vel
    return velocity


pygame.init()
screen = pygame.display.set_mode((800, 640))
pygame.display.set_caption("？？？")   #标题
font = pygame.font.Font(None, 18)   #字体
timer = pygame.time.Clock()     #时钟

#创建精灵组
player_group = pygame.sprite.Group()    #行走
floor_group = pygame.sprite.Group()     #地面

#初始化？？精灵组
player = MySprite()
player.load("0011.png", 62, 116, 8)
player.position = 80, 80    #初始坐标
player.direction = 0    #初始方向--右侧
player_group.add(player)    #添加精灵组

game_over = False       #结束
player_moving = False   #停止按键
player_health = 0       #？hp



while True:
    timer.tick(30)
    ticks = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[K_ESCAPE]:
        sys.exit()
    # elif keys[K_UP] :
    #     player.direction=0
    #     player_moving=True
    elif keys[K_RIGHT] :
        player.direction = 1
        player_moving = True
    # elif keys[K_DOWN] :
    #     player.direction = 1
    #     player_moving = True
    elif keys[K_LEFT]:
        player.direction=0
        player_moving=True
    else:
        player_moving = False

    if not game_over:
        # 根据角色的不同方向，使用不同的动画帧--列数*行数
        player.first_frame = player.direction * player.columns
        player.last_frame = player.first_frame + player.columns - 1
        if player.frame < player.first_frame:
            player.frame = player.first_frame

        if not player_moving:
            # 当停止按键（即人物停止移动的时候），停止更新动画帧
            player.frame = player.first_frame = player.last_frame
        else:
            player.velocity = calc_velocity(player.direction, 1.5)
            player.velocity.x *= 1.5
            player.velocity.y *= 1.5
        #更新
        player_group.update(ticks,50)
        #移动
        if player_moving:
            player.X += player.velocity.x
            player.Y += player.velocity.y
            if player.X <-100:
                player.X = -100
            elif player.X > 700:
                player.X = 700
            if player.Y < 100:
                player.Y =100
            elif player.Y > 500:
                player.Y = 500

    screen.fill((255, 255, 255))
    my_dog = pygame.image.load("地板.png")
    for j in range(1, 800, 63):
        for k in range(300, 600, 32):
            screen.blit(my_dog, [j, k])

    player_group.draw(screen)
    pygame.display.update()