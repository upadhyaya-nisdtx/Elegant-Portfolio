# import & initialize
import pygame
pygame.init()

# window setup
run = True
SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Elegant Portfolio')
pygame.mouse.set_visible(False)

# visible screen booleans
first_interface_visible = True
second_interface_visible = False
edit_interface_visible = False

# mouse cursor
user_cursor = pygame.image.load("custom images/arrow.png")
user_cursor = pygame.transform.scale(user_cursor, (180, 120))
user_cursor = pygame.transform.rotate(user_cursor, 45)

# general graphics
logo = pygame.image.load("custom images/ee logo.png")
logo = pygame.transform.scale(logo, (280, 200))

title = pygame.font.SysFont("Times New Roman", 150, italic=True)
title_txtsurf = title.render("Elegant Portfolio", True, (255, 255, 255))

# first interface graphics
new_project_button = pygame.Rect((200, 450, 600, 400))
new_project_title = pygame.font.SysFont("Times New Roman", 100)
new_project_txtsurf = new_project_title.render("New Project", True, (200, 200, 255, 255))

load_saves_button = pygame.Rect((1200, 450, 600, 400))
load_saves_title = pygame.font.SysFont("Times New Roman", 100)
load_saves_txtsurf = load_saves_title.render("Load Saves", True, (200, 200, 255, 255))

# second interface graphics
scroll_surface = pygame.Surface((1500, 700))

# edit interface graphics
edit_surface = pygame.Surface((500, 1000))

# main loop
while run:

    # run while first interface open
    if first_interface_visible:
        screen.fill((200, 200, 255, 255))
        pygame.draw.rect(screen, (255, 255, 255, 255), new_project_button, 400, 20)
        screen.blit(new_project_txtsurf, (500 - new_project_txtsurf.get_width() // 2,
                                          635 - new_project_txtsurf.get_height() // 2))
        pygame.draw.rect(screen, (255, 255, 255, 255), load_saves_button, 400, 20)
        screen.blit(load_saves_txtsurf, (1500 - load_saves_txtsurf.get_width() // 2,
                                         635 - load_saves_txtsurf.get_height() // 2))
        screen.blit(title_txtsurf, (1000 - title_txtsurf.get_width() // 2, 250 - title_txtsurf.get_height() // 2))
        screen.blit(logo, (1750, 0))

    # run while second interface open
    elif second_interface_visible:
        screen.fill((200, 200, 255, 255))
        screen.blit(logo, (1750, 0))
        screen.blit(title_txtsurf, (600 - title_txtsurf.get_width() // 2, 100 - title_txtsurf.get_height() // 2))
        scroll_surface.fill((255, 255, 255, 255))
        screen.blit(scroll_surface, (200, 200))

    # run while edit interface open
    elif edit_interface_visible:
        screen.fill((255, 255, 255, 255))
        edit_surface.fill((200, 200, 255, 255))
        screen.blit(edit_surface, (1500, 0))

    # cursor movement
    pos = pygame.mouse.get_pos()
    screen.blit(user_cursor, (pos[0] - 75, pos[-1] - 75))

    # event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            user_cursor = pygame.image.load("custom images/clickarrow.png")
            user_cursor = pygame.transform.scale(user_cursor, (180, 120))
            user_cursor = pygame.transform.rotate(user_cursor, 45)
            if load_saves_button.collidepoint(pos):
                first_interface_visible = False
                second_interface_visible = True
            if new_project_button.collidepoint(pos):
                first_interface_visible = False
                edit_interface_visible = True
        elif event.type == pygame.MOUSEBUTTONUP:
            user_cursor = pygame.image.load("custom images/arrow.png")
            user_cursor = pygame.transform.scale(user_cursor, (180, 120))
            user_cursor = pygame.transform.rotate(user_cursor, 45)

    pygame.display.update()

# quit
pygame.quit()
