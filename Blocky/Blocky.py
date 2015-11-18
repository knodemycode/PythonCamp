import pygame, sys
from pygame.locals import *

#initialize pygame window
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Blocky Window')


####################### Draw Blocky! #####################
"""
Objective: change these integer values to see how it changes Blocky
"""
#blocky's position
x = 100
y = 100

#blocky's size
width = 10
height = 100

#colors vary from 0-255
#red, green, and blue values are added together
#to make one, final color
red = 0
green = 180
blue = 180


#this is where the magic happens - Blocky is created
pygame.draw.rect(screen, (red, green, blue), (x, y, width, height))






#checks for system exit (red X in corner of window)
while (True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

