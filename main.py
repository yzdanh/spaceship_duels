## FIXING BUTTONS BRANCH
## TEST
import os
import pygame
import sys

from Buttons_Class import Pause
from Buttons_Class import Button_Pic

pygame.init()
pygame.font.init()
pygame.mixer.init()

## VARIABLES FOR GAME PAGE:

WINDOW_SIZE = (1280, 720)
WINDOW = pygame.display.set_mode(WINDOW_SIZE)

BORDER = pygame.Rect(1280 / 2 - 10 / 2, 0, 10, 720)

pygame.display.set_caption("Spaceship Duels")
PAUSE_TEXT_FONT = pygame.font.SysFont('arialblack', 50)
HEALTH_FONT = pygame.font.SysFont('arialblack', 30)
WINNER_FONT = pygame.font.SysFont('javanesetext', 80)

FONT_COLOR = (248, 248, 255)
BORDER_COLOR = (0, 0, 0)
RED_BULLET_COLOR = (248, 248, 255)
YELLOW_BULLET_COLOR = (248, 248, 255)
WINDOW_COLOR = (0, 0, 255)

FPS = 60

SPACESHIP_VELOCITY = 5
BULLET_VELOCITY = 8

MAX_BULLETS = 3
BULLET_WIDTH, BULLET_HEIGHT = 10, 5
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

YELLOW_SHOT = pygame.USEREVENT + 1
RED_SHOT = pygame.USEREVENT + 2
pause = pygame.USEREVENT + 3
pygame.event.post(pygame.event.Event(pause))

pause = False

YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join(
    'Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join(
    'Assets', 'spaceship_red.png'))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(
    RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'Space.jpeg')), (WINDOW_SIZE[0], WINDOW_SIZE[1]))

BACK_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'back_button.png')), (300, 150))

BACK_BUTTON = Button_Pic(
    image=BACK_BUTTON_IMAGE,
    pos=(900, 500),
    base_color=(238, 59, 59),
    hovering_color=(0, 0, 205)
)

RESUME_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'resume_button.png')), (300, 150))

RESUME_BUTTON = Button_Pic(
    image=RESUME_BUTTON_IMAGE,
    pos=(640, 460),
    base_color=(238, 59, 59),
    hovering_color=(0, 0, 205)
)

## VARIABLES FOR MAIN MENU PAGE:

MAIN_MENU_BACKGROUND = pygame.image.load((os.path.join('Assets', 'Background.jpeg')))

MENU_TEXT = PAUSE_TEXT_FONT.render("MAIN MENU", 1, FONT_COLOR)

MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

PLAY_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'play_button.png')), (300, 100))

PLAY_BUTTON = Button_Pic(
    image=PLAY_BUTTON_IMAGE,
    pos=(640, 250),
    base_color=(238, 59, 59),
    hovering_color=(0, 0, 205)
)

SETTINGS_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'settings_image.png')), (300, 100))

SETTINGS_BUTTON = Button_Pic(
    image=SETTINGS_BUTTON_IMAGE,
    pos=(640, 400),
    base_color=(238, 59, 59),
    hovering_color=(0, 0, 205)
)

QUIT_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'quit_image.png')), (300, 100))

QUIT_BUTTON = Button_Pic(
    image=QUIT_BUTTON_IMAGE,
    pos=(640, 550),
    base_color=(238, 59, 59),
    hovering_color=(0, 0, 205)
)

## VARIABLES FOR SETTINGS PAGE:

SETTINGS_TEXT = PAUSE_TEXT_FONT.render("This is the SETTINGS screen.", 1, FONT_COLOR)

SETTINGS_RECT = SETTINGS_TEXT.get_rect(center=(640, 260))

SETTINGS_BACK_BUTTON_IMAGE = pygame.transform.scale(pygame.image.load(
    os.path.join('Assets', 'back_button.png')), (300, 150))

SETTINGS_BACK_BUTTON = Button_Pic(
    image=BACK_BUTTON_IMAGE,
    pos=(640, 460),
    base_color=(238, 59, 59),
    hovering_color=(0, 0, 205)
)

## FUNCTIONS FOR GAME PAGE

def draw_window(red, yellow, yellow_bullets, red_bullets, red_health, yellow_health):
    WINDOW.blit(SPACE, (0, 0))
    pygame.draw.rect(WINDOW, BORDER_COLOR, BORDER)
    red_health_text = HEALTH_FONT.render(
        "Health: " + str(red_health), 1, FONT_COLOR)
    yellow_health_text = HEALTH_FONT.render(
        "Health: " + str(yellow_health), 1, FONT_COLOR)
    WINDOW.blit(red_health_text, (WINDOW_SIZE[0] - red_health_text.get_width() - 10, 10))
    WINDOW.blit(yellow_health_text, (10, 10))

    WINDOW.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WINDOW.blit(RED_SPACESHIP, (red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WINDOW, RED_BULLET_COLOR, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WINDOW, YELLOW_BULLET_COLOR, bullet)

    pygame.display.update()


def yellow_spaceship_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - SPACESHIP_VELOCITY > 0:  # left
        yellow.x = yellow.x + (-SPACESHIP_VELOCITY)
    if keys_pressed[pygame.K_d] and yellow.x + SPACESHIP_VELOCITY + SPACESHIP_WIDTH / 1.5 < BORDER.x:  # right
        yellow.x = yellow.x + SPACESHIP_VELOCITY
    if keys_pressed[pygame.K_w] and yellow.y - SPACESHIP_VELOCITY > 0:  # up
        yellow.y = yellow.y + (-SPACESHIP_VELOCITY)
    if keys_pressed[pygame.K_s] and yellow.y + SPACESHIP_VELOCITY + SPACESHIP_HEIGHT < WINDOW_SIZE[1] - 15:  # down
        yellow.y = yellow.y + SPACESHIP_VELOCITY

def red_spaceship_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - SPACESHIP_VELOCITY > BORDER.x + BORDER.width:
        red.x = red.x + (-SPACESHIP_VELOCITY)
    if keys_pressed[pygame.K_RIGHT] and red.x + SPACESHIP_VELOCITY + SPACESHIP_WIDTH / 1.5 < WINDOW_SIZE[0]:
        red.x = red.x + SPACESHIP_VELOCITY
    if keys_pressed[pygame.K_UP] and red.y - SPACESHIP_VELOCITY > 0:
        red.y = red.y + (-SPACESHIP_VELOCITY)
    if keys_pressed[pygame.K_DOWN] and red.y + SPACESHIP_VELOCITY + SPACESHIP_HEIGHT < WINDOW_SIZE[1] - 15:
        red.y = red.y + SPACESHIP_VELOCITY


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x = bullet.x + BULLET_VELOCITY
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_SHOT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WINDOW_SIZE[0]:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x = bullet.x + (-BULLET_VELOCITY)
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_SHOT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def make_pause_true():
    global pause
    pause = True


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, FONT_COLOR)
    WINDOW.blit(draw_text, (WINDOW_SIZE[0] / 2 - draw_text.get_width() /
                            2, WINDOW_SIZE[1] / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(50000)


## GAME PAGE FUNCTION

def game_function():
    global pause
    pause_text_object = Pause("PAUSED", 500, 500)
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets = []

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        game_mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.check_for_input(game_mouse_pos):
                    main_menu_function()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x + SPACESHIP_WIDTH, yellow.y + SPACESHIP_HEIGHT / 2 - BULLET_HEIGHT / 2, BULLET_WIDTH,
                        BULLET_HEIGHT)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RSHIFT and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x, red.y + SPACESHIP_HEIGHT / 2 - 2, BULLET_WIDTH, BULLET_HEIGHT)
                    red_bullets.append(bullet)

                if event.key == pygame.K_RETURN:
                    make_pause_true()

            if event.type == RED_SHOT:
                red_health = red_health - 1

            if event.type == YELLOW_SHOT:
                yellow_health = yellow_health - 1

        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            break

        if pause:
            Button_Pic.blit(RESUME_BUTTON, WINDOW)
            Pause.draw_pause_text(pause_text_object)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if RESUME_BUTTON.check_for_input(game_mouse_pos) and pause:
                        pause = False

        else:

            keys_pressed = pygame.key.get_pressed()

            yellow_spaceship_movement(keys_pressed, yellow)
            red_spaceship_movement(keys_pressed, red)

            handle_bullets(yellow_bullets, red_bullets, yellow, red)

            draw_window(red, yellow, red_bullets, yellow_bullets,
                        red_health, yellow_health)

            Button_Pic.blit(BACK_BUTTON, WINDOW)

            pygame.display.update()

            pygame.event.pump()

    pygame.quit()

## SETTINGS PAGE FUNCTION

def settings_function():
    run = True
    while run:

        settings_mouse_pos = pygame.mouse.get_pos()

        WINDOW.fill((0, 0, 0))

        WINDOW.blit(SETTINGS_TEXT, SETTINGS_RECT)

        Button_Pic.blit(SETTINGS_BACK_BUTTON, WINDOW)
        SETTINGS_BACK_BUTTON.blit(WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if SETTINGS_BACK_BUTTON.check_for_input(settings_mouse_pos):
                    main_menu_function()

        pygame.display.update()

## MAIN MENU PAGE FUNCTION

def main_menu_function():
    run = True
    while run:

        WINDOW.blit(MAIN_MENU_BACKGROUND, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        WINDOW.blit(MAIN_MENU_BACKGROUND, (0, 0))

        WINDOW.blit(MENU_TEXT, MENU_RECT)

        Button_Pic.blit(PLAY_BUTTON, WINDOW)

        Button_Pic.blit(SETTINGS_BUTTON, WINDOW)

        Button_Pic.blit(QUIT_BUTTON, WINDOW)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.check_for_input(menu_mouse_pos):
                    game_function()
                elif SETTINGS_BUTTON.check_for_input(menu_mouse_pos):
                    settings_function()
                elif QUIT_BUTTON.check_for_input(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu_function()

if __name__ == "__main__":
    game_function()
