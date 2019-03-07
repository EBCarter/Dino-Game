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
        self.rect = pygame.Rect(self_x, self_y, 100, 50)
        self.height_num = 0.0
        self.UorD = 0

    #makes the lapras jump up and down gradually
    def jump(self):
        if self.height_num <= 12.5 and self.UorD == 0 or self.height_num == 0:
            self.rect.y = 370 - self.height_num**2
            self.height_num += 0.5
            self.UorD = 0
            if self.rect.y == 201:
                self.UorD = 1
        elif self.height_num == 13.0 or self.UorD == 1 and self.height_num >= 0:
            self.height_num -= 0.5
            self.rect.y = 370 - self.height_num ** 2
            self.UorD = 1
            if self.rect.y == 370:
                UorD = 0
        elif self.rect.y == 370:
            self.height_num = 0

    #Change the trex's vertical position to above the ground
    def up(self):
        self.rect.y -= 150

    #Change the trex's vertical position gradually to fall down to the ground
    def down(self):
        self.rect.y += 150

    #Change the trex's position based on updates from the game.
    #How do you know if the trex should be falling, going up, or stationary?
    def move(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    trex.up()
            #elif event.type == KEYUP:
                #if event.key == K_SPACE:
                    #trex.down()

    #Update the trex's game status with regards to movement
    # and later animation (challenge)
    #def update(self):


    #Select which frame to display for your sprite
    #This is a placeholder for a challenge exercise.
    #def animate(self):
