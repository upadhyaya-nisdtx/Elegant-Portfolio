# import & initialize
import pygame
pygame.init()

# create cursor function
def create():
    cursor = pygame.image.load("custom images/arrow.png")
    cursor = pygame.transform.scale(cursor, (180, 120))
    cursor = pygame.transform.rotate(cursor, 45)
    return cursor

# check for cursor click function

