# Simple Car game using python
# Author : Shrenik Shikhare engineershrenik@gmail.com

import pygame
from pygame.locals import *
import time
import random
 
pygame.init()
track = pygame.image.load("track.png")
player = pygame.image.load("car.png")
opp_player = pygame.image.load("opp_cars.png")
opp_player_1 = pygame.image.load("opp_cars.png")
screen = pygame.display.set_mode((571,575))
xpos = 200
ypos = 200
y = 0
o_y = 0
keys=[False,False,False,False]
linecolor = 255, 255, 255 
random_val = 0
running = 1
while running:
    pygame.display.set_caption('driving')
    screen.fill(0)
    #time.sleep(0.02)
    if o_y < 10:random_val = random.randrange(1,400, 50)
    screen.blit(track,(0,0))
    pygame.draw.line(screen, linecolor, (287, y), (287, y+50), 5)
    pygame.draw.line(screen, linecolor, (287, y + 100), (287, y+150), 5)
    pygame.draw.line(screen, linecolor, (287, y + 200), (287, y+250), 5)
    pygame.draw.line(screen, linecolor, (287, y + 300), (287, y+350), 5)
    pygame.draw.line(screen, linecolor, (287, y + 400), (287, y+450), 5)
    pygame.draw.line(screen, linecolor, (287, y + 500), (287, y+550), 5)
    screen.blit(player,(xpos,ypos))
    screen.blit(opp_player,(150, o_y - random_val ))
    screen.blit(opp_player_1,(350, o_y + random_val ))
    y += 10
    o_y += 5
    #if (ypos > o_y - 10 or ypos < o_y + 10) and ( xpos > 140 or xpos < 160 ): 
    if ypos == o_y and ( xpos == 150 or  xpos == 350):
        break
    if o_y >= 550: o_y = 0
    if y + 500 == 550: y = 0#dir *= -1
    print  random_val
    pygame.display.flip()
 
    if keys[0]==True:
        if xpos <= 100:
	    xpos = 100    
	xpos-= 15
    if keys[1]==True:
        if xpos >= 450:
	    xpos = 450    
        xpos+= 15
    if keys[2]==True:
        if ypos <= 20:
	    ypos = 20    
        ypos-= 15
    if keys[3]==True:
        if ypos >= 500:
	    ypos = 500    
        ypos+= 15
    
 
 
    for event in pygame.event.get():
    # check if the event is the X button 
        if event.type==pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
 
        if event.type == pygame.KEYDOWN:
            if event.key==K_LEFT:
                keys[0]=True
            elif event.key==K_RIGHT:
                keys[1]=True
            elif event.key==K_UP:
                keys[2]=True
            elif event.key==K_DOWN:
                keys[3]=True
 
 
        if event.type == pygame.KEYUP:
            if event.key==K_LEFT:
                keys[0]=False
            elif event.key==K_RIGHT:
                keys[1]=False
            elif event.key==K_UP:
                keys[2]=False
            elif event.key==K_DOWN:
                keys[3]=False
