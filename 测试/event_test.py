# -*- coding:utf-8 -*-
from   termcolor import *
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((640, 480))
#响应时间最低70ms
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    key=pygame.key.get_pressed()
    if key[K_ESCAPE]:
        pygame.quit()
        sys.exit()
    if key[pygame.K_RIGHT]:
        print('右键')
    pygame.display.update()

