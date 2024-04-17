import pygame
class ClickableSprite(pygame.sprite.Sprite):
    def __init__(self, image, x, y, callback):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.callback = callback
    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.callback()
def on_click():
    color = (255, 0, 0) if sprite.image.get_at(
        (0, 0)) != (255, 0, 0) else (0, 255, 0)
    sprite.image.fill(color)