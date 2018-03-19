import pygame
import random
import time
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((300,100),0, 32)

arrayList = []
for i in range(0,300):
    arrayList.append(random.randint(0,1))

LeftOrRight = True


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
    for i,j in zip(arrayList,range(len(arrayList))):
        if i==1:
            pygame.draw.line(screen,color,(j,0),(j,100),1)

    if LeftOrRight:
        arrayList.append(arrayList[0])
        del arrayList[0]
    else:
        arrayList.insert(0,arrayList[-1])
        del arrayList[-1]
    time.sleep(0.02)

    pygame.display.update()
    #刷新一下画面
