import pygame, math, sys
from pygame.locals import *

if not pygame.font: print ('Warning, fonts disabled')

#initialize 
screen_width = 600
screen_height = 400
FPS = 60
WHITE = (255,255,255)

l_paddle_y = 0
r_paddle_y = 0
paddle_height = 100 #pixels
speed = 5 #pixels per update
ballspeed = 5.0
k_up = False
k_down = False

game_state = {"k_up":False ,"k_down":False,
              "k_w":False, "k_s":False,
              "l_paddle_y":0.0 , "r_paddle_y":0.0,
              "ballx":300, "bally":20,
              'balldx':'l','balldy':0,
              'rscore':0, 'lscore':0}

gs = game_state #short hand of game state is gs


#intialize pygame window
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('PONG!')
clock = pygame.time.Clock()



#Render
def render():
    screen.fill((0,0,0))
    pygame.draw.rect(screen, WHITE, (10, gs['l_paddle_y'], 10, paddle_height))

    pygame.draw.rect(screen, WHITE, (screen_width-20, gs['r_paddle_y'], 10, paddle_height))

    pygame.draw.rect(screen,WHITE, (gs['ballx'], gs['bally'], 10, 10))


        
    if pygame.font:
        font = pygame.font.Font(None, 42)
        text = font.render(str(gs['lscore'])+' - '+str(gs['rscore']), 1, (255, 255, 255))
        textpos = text.get_rect(centerx=screen_width/2)
        
        screen.blit(text, textpos)

    pygame.display.flip()

def userInput():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    gs['k_up'] = keys[K_UP]
    gs['k_down'] = keys[K_DOWN]
    gs['k_w'] = keys[K_w]
    gs['k_s'] = keys[K_s]
    

def doPhysics():
    #move things
    
    #R paddle input
    if (gs['k_w']):
        gs['l_paddle_y'] -= speed
    elif (gs['k_s']):
        gs['l_paddle_y'] += speed

    #L paddle input
    if (gs['k_up']):
        gs['r_paddle_y'] -= speed
    elif (gs['k_down']):
        gs['r_paddle_y'] += speed

    #check paddle boundaries
    if (gs['l_paddle_y'] < 0):
        gs['l_paddle_y'] = 0
    elif (gs['l_paddle_y'] > screen_height-paddle_height):
        gs['l_paddle_y'] = screen_height-paddle_height

    if (gs['r_paddle_y'] < 0):
        gs['r_paddle_y'] = 0
    elif (gs['r_paddle_y'] > screen_height-paddle_height):
        gs['r_paddle_y'] = screen_height-paddle_height

    #ball boundaries
    if (gs['bally'] < 0):
        gs['balldy'] *= -1
        gs['bally'] = 1
        
    elif (gs['bally'] > screen_height-10):
        gs['bally'] = screen_height-10
        gs['balldy'] *= -1

    #print(gs['bally'])
    


    #check for collisions

    #left paddle
    if (gs['ballx'] < 20):
        if (gs['bally']+10 > gs['l_paddle_y'] and gs['bally'] < gs['l_paddle_y']+paddle_height):
            gs['balldx'] = 'r'
            gs['ballx'] = 20
            gs['balldy'] = (gs['bally'] - gs['l_paddle_y'] - paddle_height/2)/paddle_height*ballspeed

    #right paddle
    if (gs['ballx'] > screen_width-30):
        if (gs['bally']+10 > gs['r_paddle_y'] and gs['bally'] < gs['r_paddle_y']+paddle_height):
            gs['balldx'] = 'l'
            gs['ballx'] = screen_width-30
            gs['balldy'] = (gs['bally'] - gs['r_paddle_y'] - paddle_height/2)/paddle_height*ballspeed

    if (gs['balldx'] == 'r'):
        gs['ballx'] += ballspeed
    else:
        gs['ballx'] -= ballspeed

    if (gs['ballx'] < 0):
        newBall()
        gs['rscore'] += 1

    if (gs['ballx']-10 > screen_width):
        newBall()
        gs['lscore'] += 1

    gs['bally'] += gs['balldy']
        

    return gs
        


def newBall():
    gs['ballx'] = screen_width/2
    gs['bally'] = screen_height/2
#main loop
def gameLoop(game_state):

    
    while (True):
        clock.tick(FPS)

        #user input
        userInput()
        
        #do physics stuff
        doPhysics()
              
        #re-draw things
        render()
    


        
#activate gameloop
gameLoop(game_state)
