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
def click(cursor):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor = pygame.image.load("custom images/clickarrow.png")
            cursor = pygame.transform.scale(cursor, (180, 120))
            cursor = pygame.transform.rotate(cursor, 45)
        if event.type == pygame.MOUSEBUTTONUP:
            cursor = pygame.image.load("custom images/arrow.png")
            cursor = pygame.transform.scale(cursor, (180, 120))
            cursor = pygame.transform.rotate(cursor, 45)
