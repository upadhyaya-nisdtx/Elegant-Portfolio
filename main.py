
# import & initialize
import pygame
pygame.init()

# window setup
run = True
SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Elegant Portfolio')

# screen booleans
first_interface_visible = True
second_interface_visible = False
edit_interface_visible = False

# first interface buttons
new_project_button = pygame.Rect((200, 450, 600, 400))
load_saves_button = pygame.Rect((1200, 450, 600, 400))

# main loop
while run:

    if first_interface_visible:
        screen.fill((238, 130, 238, 255))
        pygame.draw.rect(screen, (255, 255, 255, 255), new_project_button)
        pygame.draw.rect(screen, (255, 255, 255, 255), load_saves_button)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
