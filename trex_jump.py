import pygame, sys, time, random
from pygame.locals import *
#Importing modules from other files
from trex import trex
from cactus import cactus

#i added this for the lapras Image
lapras_image = pygame.image.load('lapras-pixilart.png')

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
        CACTUS.update()
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

LAPRAS = trex(360)
CACTUS = cactus(360)
x = 0

#Main game loop
while True:
    #Fill in background
    DISPLAYSURF.fill(WHITE)

    lapras_character = LAPRAS.image
    lapras_rect = LAPRAS.rect
    lapras_character = pygame.transform.scale(lapras_character,(100, 90))
    DISPLAYSURF.blit(lapras_character, lapras_rect)
    #DISPLAYSURF.blit(cactus_character, cactus_rect)

    #Event loop
    for event in pygame.event.get():

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                LAPRAS.up()

        elif event.type == KEYUP:
            if event.key == K_SPACE:
                LAPRAS.down()

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #Add cacti for lapras to jump over and spawn them
    if x == 120:
        add_cacti()
        x = 0
    update_cacti()
    x += 1

    if pygame.sprite.spritecollideany(LAPRAS, enemy):
        pygame.quit()
        sys.exit()

    #Update display
    pygame.display.update()
    fpsClock.tick(FPS)
