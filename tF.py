import pygame
import random
import time
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((300,100),0, 32)

arrayListBackGround = []
for i in range(0,300):
    arrayListBackGround.append(random.randint(0,1))

arrayListFront = []
for i in range(0,40):
    arrayListFront.append(random.randint(0,1))

LeftOrRight = True

position = 0
while True:
#游戏主循环
    for event in pygame.event.get():
        if event.type == QUIT:
            #接收到退出事件后退出程序
            exit()
        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                LeftOrRight = True
            if event.key == pygame.K_RIGHT:
                LeftOrRight = False



    screen.fill((0,0,0))
    color = (255,255,255)
    for i,j in zip(arrayListBackGround,range(0,300)):
        if i==1:
            pygame.draw.line(screen,color,(j,0),(j,100),1)

    # if LeftOrRight:
    #     arrayListBackGround.append(arrayListBackGround[0])
    #     del arrayListBackGround[0]
    # else:


    if position == 300:
        position = 0


    for i,j in zip(arrayListFront,range(position,position+30)):
        pygame.draw.line(screen,(0,0,0),(j,0),(j,100),1)
        if i==1:
            pygame.draw.line(screen,color,(j,0),(j,100),1)

    arrayListFront.insert(0,arrayListFront[-1])
    del arrayListFront[-1]


    position = position + 1
    time.sleep(0.03)
    pygame.display.update()
    #刷新一下画面
