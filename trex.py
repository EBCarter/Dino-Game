import pygame, sys, time, random
from pygame.locals import *

#Images for trex sprite
LAPRAS = pygame.image.load('lapras-pixilart.png')

#Extends functionality from the Sprite class
class trex(pygame.sprite.Sprite):

    #Initialize the attributes related to the lapras's position (x and y coords), image, and rectangle hitbox
    def __init__(self, ground):
        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        self_x = 25
        self_y = ground
        self.image = LAPRAS
        self.rect = pygame.RECT(self_x, self_y, 35, 25)

    #Change the trex's vertical position to above the ground
    def up(self):
        for x in range(5):
            self.rect.y -= 10
            time.sleep(0.1)

    #Change the trex's vertical position gradually to fall down to the ground
    def down(self):
        for x in range(5):
            self.rect.y += 10
            time.sleep(0.1)

    #Change the trex's position based on updates from the game.
    #How do you know if the trex should be falling, going up, or stationary?
    def move(self):
        

    #Update the trex's game status with regards to movement
    # and later animation (challenge)
    def update(self):


    #Select which frame to display for your sprite
    #This is a placeholder for a challenge exercise.
    #def animate(self):
