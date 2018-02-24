import pygame
from pygame.locals import *
import time
import random

pygame.init()
crash_sound = pygame.mixer.Sound("C:\\Users\\acer\\Desktop\\Game\\it\\crash.wav")
music = pygame.mixer.music.load("C:\\Users\\acer\\Desktop\\Game\\it\\music.wav")
display_width = 1920
display_height = 1080
car_width = 98
car_height = 135

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
Car_color =(10,210,255)
hred = (200,0,0)
hgreen = (0,200,0)
gameDisplay = pygame.display.set_mode((display_width,display_height))
def FullScr():
    gameDisplay = pygame.display.set_mode((display_width,display_height), FULLSCREEN)

def NFullScr():
    gameDisplay = pygame.display.set_mode((display_width,display_height))

    
pygame.display.set_caption("Need For Avoiding Objects")
clock = pygame.time.Clock()

carImg = pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\Car.png")
carIcon = pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarI.png")
scene = pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\scene.png")
pygame.display.set_icon(carIcon)
pause = False

def button(msg,x,y,w,h,i,a,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, i, (x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                gameDisplay.fill(white)
                largeText = pygame.font.Font("freesansbold.ttf",70)
                textSurf, textRect = text_objects("Avoid Upcoming Objects",largeText)
                textRect.center = ((display_width/2),(display_height/2)-60)
                gameDisplay.blit(textSurf,textRect)
                pygame.display.update()
                time.sleep(2)
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "continue":
                unpause()
            elif action == "retry":
                game_loop()
            elif action == "FS":
                FullScr()
            elif action == "SM":
                NFullScr()
    else:
        pygame.draw.rect(gameDisplay, a, (x,y,w,h))
    sargeText = pygame.font.Font("freesansbold.ttf",23)
    textSurf, textRect = text_objects(msg,sargeText)
    textRect.center = ((x+(w/2)) , (y+(h/2)))
    gameDisplay.blit(textSurf,textRect)
    
def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False


def paused():
    pygame.mixer.music.pause()
    largeText = pygame.font.Font("freesansbold.ttf",75)
    textSurf, textRect = text_objects("Paused",largeText)
    textRect.center = ((display_width/2),(display_height/2)-60)
    gameDisplay.blit(textSurf,textRect)
    lText = pygame.font.Font("freesansbold.ttf",28)
    textSurface, textRec = text_objects("Need For Avoding Objects",lText)
    textRec.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurface,textRec)
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                     unpause()
        
            
        
        button("Resume",(display_width/4),(((display_height/4)*2)+150),100,50,hgreen,green,"continue")
        button("Quit",(((display_width/4)*3)-100),(((display_height/4)*2)+150),100,50,hred,red,"quit")  
        pygame.display.update()
        clock.tick(15)
    
def game_intro():
    intro =True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        largeText = pygame.font.Font("freesansbold.ttf",72)
        textSurf, textRect = text_objects("Need For Avoiding Objects",largeText)
        textRect.center = ((display_width/2),(display_height/2)-60)
        gameDisplay.blit(textSurf,textRect)
        lText = pygame.font.Font("freesansbold.ttf",35)
        textSurface, textRec = text_objects("A Prasanta Productions Game",lText)
        textRec.center = ((display_width/2),(display_height/2)+20)
        gameDisplay.blit(textSurface,textRec)
        button("Start",(display_width/4),(((display_height/4)*2)+150),100,50,hgreen,green,"play")
        button("Quit",(((display_width/4)*3)-100),(((display_height/4)*2)+150),100,50,hred,red,"quit")
        button("FullScreen",((display_width/4)-25),(((display_height/4)*2)+250),150,50,hgreen,green,"FS")
        button("Windowed",((((display_width/4)*3)-100)-25),(((display_height/4)*2)+250),150,50,hred,red,"SM")
        pygame.display.update()
        clock.tick(15)


def displayPause():
    font = pygame.font.SysFont(None , 30)
    text = font.render("Press Esc to Pause or Quit", True, black)
    gameDisplay.blit(text,(display_width-280,50))

def things_dodged(count):
    font = pygame.font.SysFont(None , 40)
    text = font.render("Score : "+str(count), True, black)
    gameDisplay.blit(text,(display_width-200,20))
    displayPause()

def Car(thingx , thingy):
    i = random.randrange(1,5)
    if i == 1:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\Car.png")
    elif i == 2:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\Car2.png")
    elif i == 3:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\Car3.png")
    elif i == 4:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\Car4.png")
    elif i == 5:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\Car5.png")
    gameDisplay.blit(BFC,(thingx , thingy))

def CarUD(thingx , thingy):
    i = random.randrange(1,5)
    if i == 1:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarUD.png")
    elif i == 2:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarUD2.png")
    elif i == 3:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarUD3.png")
    elif i == 4:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarUD4.png")
    elif i == 5:
        BFC =  pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarUD5.png")
    gameDisplay.blit(BFC,(thingx , thingy))

def moving(thingx , thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx , thingy, thingw, thingh])

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def message_display(text):
    largeText = pygame.font.Font("freesansbold.ttf",115)
    textSurf, textRect = text_objects(text,largeText)
    textRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    
def  crash(x,y):
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    CarCrash = pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarCrash.png")
    gameDisplay.blit(CarCrash,(x,y))
    pygame.display.flip()
    time.sleep(1)
    CarCrash2 = pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarCrash2.png")
    gameDisplay.blit(CarCrash2,(x,y))
    pygame.display.flip()
    time.sleep(1)
    CarCrash3 = pygame.image.load("C:\\Users\\acer\\Desktop\\Game\\it\\CarCrash3.png")
    gameDisplay.blit(CarCrash3,(x,y))
    pygame.display.flip()

    largeText = pygame.font.Font("freesansbold.ttf",75)
    textSurf, textRect = text_objects("You Crashed",largeText)
    textRect.center = ((display_width/2),(display_height/2)-60)
    gameDisplay.blit(textSurf,textRect)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button("Retry",(display_width/4),(((display_height/4)*2)+150),100,50,hgreen,green,"retry")
        button("Quit",(((display_width/4)*3)-100),(((display_height/4)*2)+150),100,50,hred,red,"quit")  
        pygame.display.update()
        clock.tick(15)

def text_objects(text , font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_loop():
    global pause
    pygame.mixer.music.play(-1)

    x = (display_width * 0.45)
    y = (display_height * 0.85)
    x_change = 0
    left = -5
    right = 5
    IDK = display_width-585
   
    Car_width = 98
    Car_height = 135
    Car_starty = -300
    CarUD_width = 98
    CarUD_height = 135
    CarUD_starty = -600
    moving_startx = display_width/2
    moving_starty = 0
    moving_speed = 5
    Car_startx = random.randrange(585,moving_startx-Car_width)
    Car_speed = 3
    CarUD_startx = random.randrange(display_width/2,IDK-CarUD_width)
    CarUD_speed = 6
    dodged = 0
    call = 0

    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = left
                if event.key == pygame.K_RIGHT:
                    x_change = right
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        

            

        gameDisplay.blit(scene,(0,0))
        Car(Car_startx, Car_starty)
        CarUD(CarUD_startx, CarUD_starty)
        Car_starty += Car_speed
        CarUD_starty += CarUD_speed


        
        car(x,y)
        things_dodged(dodged)
        if x > (display_width-car_width) or x < 0:
            crash(x,y)
            
        if Car_starty > display_height:
            Car_starty = 0-Car_height
            Car_startx = random.randrange(585,moving_startx-Car_width)
            dodged += 1
            Car_speed +=0.5
            left += -0.4
            right += 0.4
        if CarUD_starty > display_height:
            CarUD_starty = 0-CarUD_height
            CarUD_startx = random.randrange(display_width/2,IDK-CarUD_width)
            dodged += 1
            CarUD_speed +=0.6
            left += -0.4
            right += 0.4


        if y < Car_starty+Car_height:
            if x > Car_startx and x < Car_startx + Car_width or x +car_width > Car_startx and x+car_width<Car_startx+Car_width:
                crash(x,y)
        if y < CarUD_starty+CarUD_height:
            if x > CarUD_startx and x < CarUD_startx + CarUD_width or x +car_width > CarUD_startx and x+car_width<CarUD_startx+CarUD_width:
                crash(x,y)
        
        pygame.display.update()
        clock.tick(150)

game_intro()
