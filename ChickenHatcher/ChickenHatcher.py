import pygame, sys, os, random
from pygame.locals import *

pygame.init()
screen_width =  1024
screen_height = 768
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('HELLO WORLD!')


def load_image(name, colorkey=None):
    
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(name) #replaced fullname with name
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()
    


class Egg(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image("egg.png", -1)
        self.rect.x = random.randrange(0, screen_width-50)
        self.rect.y = random.randrange(0, screen_height-50)
        #print("egg init")
        
    def hatch(self):
        """change image to chicken_image"""



def main():
    eggs = pygame.sprite.Group()

    #use a for loop to place 10 eggs on the screen
    egg = Egg()
    eggs.add(egg)



    
    eggs.draw(screen)

    pygame.display.flip()  

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
