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

exit_button = pygame.image.load("custom images/exit_button.png")
exit_button = pygame.transform.scale(exit_button, (210, 180))

# first interface graphics
new_project_button = pygame.Rect((200, 450, 600, 400))
new_project_title = pygame.font.SysFont("Times New Roman", 100)
new_project_txtsurf = new_project_title.render("New Project", True, (100, 0, 150, 255))
load_saves_button = pygame.Rect((1200, 450, 600, 400))
load_saves_title = pygame.font.SysFont("Times New Roman", 100)
load_saves_txtsurf = load_saves_title.render("Load Saves", True, (100, 0, 150, 255))

def first_int_graphics():
    screen.fill((200, 200, 255, 255))
    pygame.draw.rect(screen, (255, 255, 255, 255), new_project_button, 400, 20)
    screen.blit(new_project_txtsurf, (500 - new_project_txtsurf.get_width() // 2,
                                      635 - new_project_txtsurf.get_height() // 2))
    pygame.draw.rect(screen, (255, 255, 255, 255), load_saves_button, 400, 20)
    screen.blit(load_saves_txtsurf, (1500 - load_saves_txtsurf.get_width() // 2,
                                     635 - load_saves_txtsurf.get_height() // 2))
    screen.blit(title_txtsurf, (1000 - title_txtsurf.get_width() // 2, 250 - title_txtsurf.get_height() // 2))
    screen.blit(logo, (1750, 0))

# second interface graphics
scroll_surface = pygame.Surface((1500, 700))

def second_int_graphics():
    screen.fill((200, 200, 255, 255))
    screen.blit(logo, (1750, 0))
    screen.blit(title_txtsurf, (600 - title_txtsurf.get_width() // 2, 100 - title_txtsurf.get_height() // 2))
    scroll_surface.fill((255, 255, 255, 255))
    screen.blit(exit_button, (1550, 0))
    screen.blit(scroll_surface, (200, 200))

# edit interface graphics
edit_surface = pygame.Surface((500, 1000))
undo_button = pygame.Rect((1550, 30, 100, 100))
redo_button = pygame.Rect((1710, 30, 100, 100))
undo_image = pygame.image.load("custom images/undo button.png")
redo_image = pygame.image.load("custom images/redo button.png")
undo_image = pygame.transform.scale(undo_image, (100, 100))
redo_image = pygame.transform.scale(redo_image, (100, 100))
text_button = pygame.Rect((1520, 150, 210, 200))
image_button = pygame.Rect((1750, 150, 210, 200))
bg_button = pygame.Rect((1520, 380, 210, 200))
sound_button = pygame.Rect((1750, 380, 210, 200))
text_button_title = pygame.font.SysFont("Arial", 45)
text_button_txtsurf = text_button_title.render("Add Text", True, (100, 0, 150, 255))
image_button_title = pygame.font.SysFont("Arial", 45)
image_button_txtsurf = image_button_title.render("Add Image", True, (100, 0, 150, 255))
bg_title = pygame.font.SysFont("Arial", 45)
bg_txtsurf = bg_title.render("BG Color", True, (100, 0, 150, 255))
sound_title = pygame.font.SysFont("Arial", 45)
sound_txtsurf = sound_title.render("Edit Sound", True, (100, 0, 150, 255))

def edit_int_graphics():
    screen.fill((255, 255, 255, 255))
    edit_surface.fill((200, 200, 255, 255))
    screen.blit(edit_surface, (1500, 0))
    screen.blit(exit_button, (1820, -20))
    pygame.draw.rect(screen, (255, 255, 255, 255), undo_button, 400, 10)
    screen.blit(undo_image, (1550, 30))
    pygame.draw.rect(screen, (255, 255, 255, 255), redo_button, 400, 10)
    screen.blit(redo_image, (1710, 30))
    pygame.draw.rect(screen, (255, 255, 255, 255), text_button, 400, 10)
    pygame.draw.rect(screen, (255, 255, 255, 255), image_button, 400, 10)
    screen.blit(text_button_txtsurf, (1620 - text_button_txtsurf.get_width() // 2, 250 - text_button_txtsurf.get_height() // 2))
    screen.blit(image_button_txtsurf, (1856 - image_button_txtsurf.get_width() // 2, 250 - image_button_txtsurf.get_height() // 2))
    pygame.draw.rect(screen, (255, 255, 255, 255), bg_button, 400, 10)
    screen.blit(bg_txtsurf, (1620 - bg_txtsurf.get_width() // 2, 480 - bg_txtsurf.get_height() // 2))
    pygame.draw.rect(screen, (255, 255, 255, 255), sound_button, 400, 10)
    screen.blit(sound_txtsurf, (1856 - sound_txtsurf.get_width() // 2, 480 - sound_txtsurf.get_height() // 2))

# main loop
while run:

    # run while first interface open
    if first_interface_visible:
        first_int_graphics()

    # run while second interface open
    elif second_interface_visible:
        second_int_graphics()

    # run while edit interface open
    elif edit_interface_visible:
        edit_int_graphics()

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
            if first_interface_visible:
                if load_saves_button.collidepoint(pos):
                    first_interface_visible = False
                    second_interface_visible = True
                elif new_project_button.collidepoint(pos):
                    first_interface_visible = False
                    edit_interface_visible = True
            elif second_interface_visible:
                if exit_button.get_rect(topleft=(1550, 0)).collidepoint(pos):
                    first_interface_visible = True
                    second_interface_visible = False
            elif edit_interface_visible:
                if exit_button.get_rect(topleft=(1820, 0)).collidepoint(pos):
                    first_interface_visible = True
                    edit_interface_visible = False

        elif event.type == pygame.MOUSEBUTTONUP:
            user_cursor = pygame.image.load("custom images/arrow.png")
            user_cursor = pygame.transform.scale(user_cursor, (180, 120))
            user_cursor = pygame.transform.rotate(user_cursor, 45)

    pygame.display.update()

# quit
pygame.quit()
