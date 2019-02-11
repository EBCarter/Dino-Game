import pygame, sys, time, random
from pygame.locals import *

#comment added for repository
#Image for cactus sprite
CACTUS = pygame.image.load('resources/cactus.png')

#Extends functionality from the Sprite class
class cactus(pygame.sprite.Sprite):

    #Initialize the attributes related to the cactus's position, image, hitbox, and jumping status
    def __init__(self, ground):
        #Calls the Sprite class constructor.
        #It must be the first line in constructor.
        super().__init__()
        #Don't forget to add rect and image attributes!
        self_x = 400
        self_y = ground
        self.image = CACTUS
        self.rect = pygame.RECT(self_x, self_y, 35, 25)

    #Changes the cactus's horizontal location
    def move(self):
        for x in range(40):
            self.rect.x -= 10

    #Updates the cactus's horizonal location.
    #If it's in the window, it will move.
    #If it's outside the window, the sprite will be killed.
    def update(self):
        if self.rect.x 
