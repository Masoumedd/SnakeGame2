import pygame
import time
import random
from pygame.locals import *
from random import randint
import os, sys




ARRAY_SIZE = 50

DIRECTIONS = {
    "LEFT": (-1, 0),
    "RIGHT": (1, 0),
    "UP": (0, 1),
    "DOWN": (0, -1),
}

snake, fruit = None, None

def init():
    global snake
    snake = [ (0, 2), (0, 1), (0, 0)]

    place_fruit((ARRAY_SIZE // 2, ARRAY_SIZE // 2))

def place_fruit(coord=None):
    global fruit
    if coord:
        fruit = coord
        return

    while True:
        x = randint(0, ARRAY_SIZE-1)
        y = randint(0, ARRAY_SIZE-1)
        if (x, y) not in snake:
           fruit = x, y
           return




DIRS = ['UP', 'RIGHT', 'DOWN', 'LEFT']




pygame.init()
display_width=800
display_height=600

black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
light_red=(255,0,0)
green=(0,200,0)
light_green=(0,255,0)




gameDisplay=pygame.display.set_mode((display_width,display_height))


pygame.display.set_caption('Snake')
clock=pygame.time.Clock()


def text_object(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()



def Button(msg,x,y,w,h,ic,ac,action=None):
    mouse=pygame.mouse.get_pos()
    Click=pygame.mouse.get_pressed()

    if x + w >mouse[0]> x and y + h > mouse[1]>y :
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if Click[0]==1 and action!=None:
            if action=="play":
                game_loop()
            elif action=="quit":
                pygame.quit()
                quit()
            
    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))
    smallText=pygame.font.Font('freesansbold.ttf',20)  
    TextSurfe,TextRect=text_object(msg ,smallText)
    TextRect.center=((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(TextSurfe,TextRect)

  

def game_intro():
    intro=True
    while intro :
        for event in  pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)  
        largeText=pygame.font.Font('freesansbold.ttf',90)
        TextSurfe,TextRect=text_object("Let's play game" ,largeText)
        TextRect.center=((display_width/2),(display_height)/2)
        gameDisplay.blit(TextSurfe,TextRect)
        Button("play",150,450,100,50,green,light_green,"play")
        Button("quit",550,450,100,50,red,light_red,"quit")

        pygame.display.update()


        


def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',90)
    TextSurfe,TextRect=text_object(text,largeText)
    TextRect.center=((display_width)/2,(display_height)/2)
    gameDisplay.blit(TextSurfe,TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()

    
def crash():

    largeText=pygame.font.Font('freesansbold.ttf',60)
    TextSurfe,TextRect=text_object("YOU CRASHED",largeText)
    TextRect.center=((display_width)/3,(display_height)/2)
    gameDisplay.blit(TextSurfe,TextRect)

    
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                
        Button("Try again",100,350,100,50,green,light_green,"play")
        Button("Quit",300,350,100,50,red,light_red,"quit")
        pygame.display.update()
        
def  Score(dodged):
    font=pygame.font.SysFont(None , 25)
    text=font.render("score : "+str(dodged),True,red)
    gameDisplay.blit(text,(0,0))
    


def step(direction):
    old_head = snake[0]
    dodged=0
    movement = DIRECTIONS[direction]
    new_head = (old_head[0]+movement[0], old_head[1]+movement[1])

    if (
            new_head[0] < 0 or
            new_head[0] >= ARRAY_SIZE or
            new_head[1] < 0 or
            new_head[1] >= ARRAY_SIZE or
            new_head in snake
            
        ):
        return False
         
    if new_head == fruit:
        place_fruit()
        Score(dodged)
        dodged+1
        
    else:
        tail = snake[-1]
        del snake[-1]

    snake.insert(0, new_head)

    
    
    return True





def game_loop():
    init()

    direction = 0
   

    pygame.init()
    s = pygame.display.set_mode((ARRAY_SIZE * 10, ARRAY_SIZE * 10))
    appleimage = pygame.Surface((10, 10))
    appleimage.fill((22, 24,199))
    img = pygame.Surface((10, 10))
    img.fill((247, 19, 140))
    clock = pygame.time.Clock()

    pygame.time.set_timer(1, 100)
    while True:
        e = pygame.event.wait()                             
        if e.type == QUIT:                                                                  
            pygame.quit()                               
        
        elif e.type == KEYDOWN:
            key=pygame.key.get_pressed()
            
            
            if      key[pygame.K_UP]:     direction = 0
            elif    key[pygame.K_RIGHT]:    direction = 1
            elif    key[pygame.K_DOWN]:       direction = 2
            elif    key[pygame.K_LEFT]:     direction = 3
               

        elif e.type == MOUSEBUTTONDOWN:                     
            if e.button == 3:                           
                direction = (direction+1) % 4
                
            elif e.button == 1:                         
              direction = (direction+3) % 4
              
        elif not step(DIRS[direction]):
           
            crash()

            
            pygame.quit()                          
            sys.exit()
        
        
            
        
        
        
        s.fill((211, 209, 245))	
        for bit in snake:
            s.blit(img, (bit[0] * 10, (ARRAY_SIZE - bit[1] - 1) * 10))
            
        s.blit(appleimage, (fruit[0] * 10, (ARRAY_SIZE - fruit[1]-1) * 10))
        
        pygame.display.flip()
        
        

       

game_intro()
game_loop()
pygame.quit()
quit()


    


