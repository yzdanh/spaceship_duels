import pygame

pygame.init()
pygame.font.init()

PAUSE_TEXT_FONT = pygame.font.SysFont('arialblack', 50)
WINDOW_SIZE = (1280, 720)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)
FONT_COLOR = (248, 248, 255)


class Pause:
    def __init__(self, text, x_pos, y_pos, enabled=True):
        self.text = text
        self.enabled = enabled
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw_pause_text(self):
        pause_text = PAUSE_TEXT_FONT.render(self.text, True, FONT_COLOR)
        WINDOW.blit(pause_text, (self.x_pos, self.y_pos))


class Button_Pic:
    def __init__(self, image, pos, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def blit(self, window):
        window.blit(self.image, self.rect)

    def check_for_input(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True

        else:
            return False
