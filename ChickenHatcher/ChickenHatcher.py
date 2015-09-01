import pygame, sys, os
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 768))
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
        pos = (100, 100)
        #print("egg init")
        
    def hatch(self):
        """change image to chicken_image"""



def main():
    
    egg = Egg()
    egg.rect.x = 100
    egg.rect.y = 100
    eggs = pygame.sprite.Group()
    eggs.add(egg)
    
    #eggs.clear(screen)
    eggs.draw(screen)
    print("main")

    pygame.display.flip()  

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()
