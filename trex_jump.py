import pygame, sys, time, random
from pygame.locals import *
#Importing modules from other files
from trex import trex
from cactus import cactus

#i added this for the lapras Image
lapras_image = pygame.image.load('lapras-pixilart.png')
background = pygame.image.load('background.png')

#Always call before utilizing pygame functions
pygame.init()

#Sets FPS and starts game clock/
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
#Sets title of GUI frame
pygame.display.set_caption("Lapras Jump")

#Sets background color
WHITE = (250, 250, 250)
BLUE = (0,0,250)

#Adds a new cactus sprite to the list of obstacles
enemy = pygame.sprite.Group()
def add_cacti():
    CACTUS = cactus(400)
    enemy.add(CACTUS)

#Updates each cactus sprite's location
#Removes the cactus from sprite group if it's off screen
#Scores removed cacti
#Redraws cactus image
def update_cacti():
    #CACTUS.update()
    for CACTUS in enemy:
        CACTUS.image = pygame.transform.scale(CACTUS.image,(50, 62))
        global score
        score = CACTUS.update(score)
        DISPLAYSURF.blit(CACTUS.image,CACTUS.rect)
        #CACTUS.move()

#Updates trex sprite's location and redraws trex image
#def update_rex():

#Starts game over actions
#Displays an end of game message in a text box
#Kills trex sprite
#Creates new game loop to display end game state
#def game_over():

#Creates a text box with the text provided in location x, y on screen
#def display_message(text, x, y):

#Displays current score in a text box
#def display_score():

#Displays current time in a text box
#def display_time():

#Determines whether the trex sprite collides with a cacti sprite
#If there is a collision, the game is over.
#def is_collision():

#Increases the FPS by 5 every 100 seconds
#This is a placeholder for a challenge exercise.
#def increase_FPS():

    #FPS += 5

LAPRAS = trex(370)
CACTUS = cactus(360)
x = 0
score = 0
BASICFONT = pygame.font.Font('freesansbold.ttf',16)
Surf = BASICFONT.render('Score:' + str(score),1,(0,0,0))
Rect = Surf.get_rect()
Rect.topleft = (10,10)
top_time = 0
spawn_it = 120

#Main game loop
while True:
    #Fill in background
    #DISPLAYSURF.fill(BLUE)

    lapras_character = LAPRAS.image
    lapras_rect = LAPRAS.rect
    lapras_character = pygame.transform.scale(lapras_character,(100, 90))
    background = pygame.transform.scale(background,(1000,500))
    #makes the background a thing
    DISPLAYSURF.blit(background,(0,0))

    #draws the lapras
    DISPLAYSURF.blit(lapras_character, lapras_rect)
    
    #DISPLAYSURF.blit(cactus_character, cactus_rect)

    #Event loop
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_SPACE and top_time == 0:
                LAPRAS.jump()

        #elif event.type == KEYUP:
            #if event.key == K_SPACE:
                #LAPRAS.down()



        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Add cacti for lapras to jump over and spawn them and changes speed if you progress far enough
    if score <= 9:
        if x == spawn_it:
            add_cacti()
            x = 0
            spawn_it = random.randint(70,120)
    elif score <= 14:
        if x == spawn_it:
            add_cacti()
            x = 0
            spawn_it = random.randint(65,110)
    elif score <= 19:
        if x == spawn_it:
            add_cacti()
            x = 0
            spawn_it = random.randint(60,100)
    elif score <= 24:
        if x == spawn_it:
            add_cacti()
            x = 0
            spawn_it = random.randint(55,90)
    elif score <= 29:
        if x == spawn_it:
            add_cacti()
            x = 0
            spawn_it = random.randint(50,80)
    elif score >= 30:
        if x == spawn_it:
            add_cacti()
            x = 0
            spawn_it = random.randint(45,70)
    #update_cacti()
    x += 1
    #global score
    update_cacti()

    if LAPRAS.height_num == 13:
        top_time += 1
        if top_time == 10:
            LAPRAS.jump()
            top_time = 0
    elif LAPRAS.height_num != 13 and LAPRAS.height_num != 0:
        LAPRAS.jump()

    if pygame.sprite.spritecollideany(LAPRAS, enemy):
        pygame.quit()
        sys.exit()

    Surf = BASICFONT.render('Score:' + str(score),1,(0,0,0))
    Rect = Surf.get_rect()
    Rect.topleft = (10,10)
    DISPLAYSURF.blit(Surf, Rect)

    #Update display
    pygame.display.update()
    fpsClock.tick(FPS)
