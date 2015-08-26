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
width = 100
height = 100

#colors vary from 0-255
red = 255
green = 0
blue = 0


#this is where the magic happens
pygame.draw.rect(screen, (red, green, blue), (x, y, width, height))





#check for system exit (red X in corner of window)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
