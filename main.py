# import & initialize
import pygame
pygame.init()
import json
import os

# window setup
run = True
SCREEN_WIDTH = 2000
SCREEN_HEIGHT = 1000
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Elegant Portfolio')
pygame.mouse.set_visible(False)
selected_item = None
my_sound = pygame.mixer.Sound("sounds/click_tone")

# visible screen booleans
first_interface_visible = True
second_interface_visible = False
edit_interface_visible = False

# mouse cursor
user_cursor = pygame.image.load("custom images/arrow.png")
user_cursor = pygame.transform.scale(user_cursor, (180, 120))
user_cursor = pygame.transform.rotate(user_cursor, 45)

# universal graphics
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
    """
    displays universal + first interface graphics
    -----
    returns: None
    """
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
file_list = os.listdir("save files")
load_items = []
load_y = 0
for item in file_list:
    load_button = pygame.Rect((200, load_y + 200, 1400, 100))
    load_items.append(load_button)

def second_int_graphics():
    """
    displays universal + second interface graphics
    -----
    returns: None
    """
    screen.fill((200, 200, 255, 255))
    screen.blit(logo, (1750, 0))
    screen.blit(title_txtsurf, (600 - title_txtsurf.get_width() // 2, 100 - title_txtsurf.get_height() // 2))
    scroll_surface.fill((255, 255, 255, 255))
    screen.blit(exit_button, (1550, 0))
    screen.blit(scroll_surface, (200, 200))
    for item in load_items:
        pygame.draw.rect(screen, (0, 0, 0, 0), item)


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
edit_bg_color_list = [(255, 255, 255), (127, 127, 127), (255, 100, 100), (100, 255, 100), (100, 100, 255),
                      (255, 255, 100), (100, 255, 255), (255, 100, 255), (0, 0, 0)]
edit_bg_color_index = 0
save_button = pygame.Rect((1750, 600, 210, 200))
save_title = pygame.font.SysFont("Arial", 45)
save_txtsurf = bg_title.render("Save", True, (100, 0, 150, 255))

def edit_int_graphics():
    """
    displays universal + edit interface graphics
    -----
    returns: None
    """
    screen.fill(edit_bg_color_list[edit_bg_color_index])
    edit_surface.fill((200, 200, 255, 255))
    screen.blit(edit_surface, (1500, 0))
    screen.blit(exit_button, (1820, -20))
    pygame.draw.rect(screen, (255, 255, 255, 255), undo_button, 400, 10)
    screen.blit(undo_image, (1550, 30))
    pygame.draw.rect(screen, (255, 255, 255, 255), redo_button, 400, 10)
    screen.blit(redo_image, (1710, 30))
    pygame.draw.rect(screen, (255, 255, 255, 255), text_button, 400, 10)
    pygame.draw.rect(screen, (255, 255, 255, 255), image_button, 400, 10)
    screen.blit(text_button_txtsurf, (1620 - text_button_txtsurf.get_width() // 2,
                                      250 - text_button_txtsurf.get_height() // 2))
    screen.blit(image_button_txtsurf, (1856 - image_button_txtsurf.get_width() // 2,
                                       250 - image_button_txtsurf.get_height() // 2))
    pygame.draw.rect(screen, (255, 255, 255, 255), bg_button, 400, 10)
    screen.blit(bg_txtsurf, (1620 - bg_txtsurf.get_width() // 2, 480 - bg_txtsurf.get_height() // 2))
    pygame.draw.rect(screen, (255, 255, 255, 255), sound_button, 400, 10)
    screen.blit(sound_txtsurf, (1856 - sound_txtsurf.get_width() // 2, 480 - sound_txtsurf.get_height() // 2))
    pygame.draw.rect(screen, (255, 255, 255, 255), save_button, 400, 10)
    screen.blit(save_txtsurf, (1856 - save_txtsurf.get_width() // 2, 700 - save_txtsurf.get_height() // 2))


# edit interface functions
images_list = ["stock1.jpg", "stock2.jpg", "stock3.jpg", "stock4.jpg", "stock5.jpg", "preview16.jpg"]
images_index = 0
custom_list = []
songs_list = ["song1.mp3", "song2.mp3", "song3.mp3", "song4.mp3", "song5.mp3"]
songs_index = 0
text_type = False
sound = None
files = len(os.listdir("save files"))

def edit_text(text, text_key):
    """
    gets user input for the text on the text object
    -----
    returns: text string
    """
    global text_type
    if text_key == pygame.K_RETURN:
        text_type = False
        return text
    elif text_key == pygame.K_BACKSPACE:
        text = text[:-1]
    else:
        text += event.unicode
    return text


def add_text():
    """
    creates and adds text object to the window
    -----
    returns: list of attributes for the text object
    """
    custom_text = "Edit Text"
    custom_x = 300
    custom_y = 200
    custom_title = pygame.font.SysFont("Arial", 45)
    custom_txtsurf = custom_title.render(custom_text, True, (100, 0, 150, 255))
    return [custom_txtsurf, custom_x, custom_y, custom_text, custom_title, False]


def add_image():
    """
    creates and adds image object to the window
    -----
    returns: list of attributes for the image object
    """
    img_temp = images_list[images_index]
    custom_image = pygame.image.load("custom images/" + img_temp)
    custom_image = pygame.transform.scale(custom_image, (300, 200))
    image_x = 100
    image_y = 100
    return [custom_image, image_x, image_y, False]


def add_sound():
    """
    creates and plays a sound
    -----
    returns: sound
    """
    song_temp = songs_list[songs_index]
    custom_sound = pygame.mixer.Sound("sounds/" + song_temp)
    return custom_sound


def user_edit_int_graphics():
    """
    displays all items in custom list
    items in custom list are the objects created in add_text() and add_image() functions
    -----
    returns: None
    """
    for custom_item in custom_list:
        screen.blit(custom_item[0], (custom_item[2] - custom_item[0].get_width() // 2,
                                     custom_item[1] - custom_item[0].get_height() // 2))


def save(filename, bg_color, item_list, music=None):
    """
    saves all custom object + background information into file
    -----
    returns: None
    """
    dictionary_save = {
        "filename": filename,
        "bg color": bg_color,
        "custom list": str(item_list),
        "music": str(music)
    }
    json_object = json.dumps(dictionary_save, indent = 4)
    with open(filename, "w") as file:
       file.write(json_object)


def load_saves(filename):
    """
    loads saved object
    -----
    returns: data
    """
    global edit_interface_visible, second_interface_visible, custom_list, edit_bg_color_list, edit_bg_color_index
    try:
        with open(filename) as file:
            data = json.load(file)
            print("File loaded:", data)
    except Exception as e:
        print("Error loading file:", e)
        return None
    edit_interface_visible = True
    second_interface_visible = False
    custom_list = data["custom list"]
    if tuple(data["bg color"]) in edit_bg_color_list:
        edit_bg_color_index = edit_bg_color_list[tuple(data["bg color"])]
    if data["music"] is not None:
        sound = data["music"]
    return data


# main loop
while run:

    # run while first interface open
    if first_interface_visible:
        first_int_graphics()
        custom_list = []
        images_index = 0
        songs_index = 0

    # run while second interface open
    elif second_interface_visible:
        second_int_graphics()

    # run while edit interface open
    elif edit_interface_visible:
        edit_int_graphics()
        user_edit_int_graphics()

    # cursor movement
    pos = pygame.mouse.get_pos()
    screen.blit(user_cursor, (pos[0] - 75, pos[-1] - 75))

    # object movement
    if selected_item is not None:
        selected_item[1] = pos[1]
        selected_item[2] = pos[0]
        selected_item[0].get_rect(topleft=(selected_item[1], selected_item[2]))

    # event check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # what to do when mouse is down
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # cursor/sound changes
            my_sound.play()
            user_cursor = pygame.image.load("custom images/clickarrow.png")
            user_cursor = pygame.transform.scale(user_cursor, (180, 120))
            user_cursor = pygame.transform.rotate(user_cursor, 45)

            # when the first interface is visible
            if first_interface_visible:
                edit_bg_color_index = 0
                if load_saves_button.collidepoint(pos):
                    first_interface_visible = False
                    second_interface_visible = True
                elif new_project_button.collidepoint(pos):
                    first_interface_visible = False
                    edit_interface_visible = True

            # when the second interface is visible
            elif second_interface_visible:
                edit_bg_color_index = 0
                if exit_button.get_rect(topleft=(1550, 0)).collidepoint(pos):
                    first_interface_visible = True
                    second_interface_visible = False

            # when the edit interface is visible
            elif edit_interface_visible:
                if exit_button.get_rect(topleft=(1820, 0)).collidepoint(pos):
                    first_interface_visible = True
                    edit_interface_visible = False
                elif bg_button.collidepoint(pos):
                    if edit_bg_color_index > 7:
                        edit_bg_color_index = 0
                    else:
                        edit_bg_color_index += 1
                elif text_button.collidepoint(pos):
                    temp = add_text()
                    custom_list.append(temp)
                    text_type = True
                elif image_button.collidepoint(pos):
                    image = add_image()
                    custom_list.append(image)
                    images_index += 1
                    if images_index > len(images_list) - 1:
                        images_index = 0
                    text_type = False
                elif sound_button.collidepoint(pos):
                    if sound is not None:
                        sound.stop()
                    sound = add_sound()
                    songs_index += 1
                    if songs_index > len(songs_list) - 1:
                        songs_index = 0
                    sound.play()
                elif save_button.collidepoint(pos):
                    save_file_name = "save files/Portfolio" + str(files) + ".json"
                    save_bg_color = edit_bg_color_list[edit_bg_color_index]
                    save(save_file_name, save_bg_color, custom_list, sound)
                    files = len(os.listdir("save files"))
                    file_list = os.listdir("save files")
                for item in custom_list:
                    if item[0].get_rect(topleft=(item[2], item[1])).collidepoint(pos):
                        selected_item = item
                        break

        # what to do when mouse is released
        elif event.type == pygame.MOUSEBUTTONUP:
            user_cursor = pygame.image.load("custom images/arrow.png")
            user_cursor = pygame.transform.scale(user_cursor, (180, 120))
            user_cursor = pygame.transform.rotate(user_cursor, 45)
            selected_item = None

        if event.type == pygame.KEYDOWN:
            if text_type:
                t_key = event.key
                temp_text = edit_text(custom_list[-1][3], t_key)
                custom_list[-1][3] = temp_text
                custom_list[-1][0] = custom_list[-1][4].render(custom_list[-1][3], True, (100, 0, 150, 255))

    pygame.display.update()

# quit
pygame.quit()
