
# import & initialize
import pygame
pygame.init()

# window setup
run = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Elegant Portfolio')
box = pygame.Rect((300, 250, 50, 50))

# main loop
while run:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), box)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
