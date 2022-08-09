# importing time and threading
# Beginning of Pygame Code
from pynput.keyboard import Listener, KeyCode
from pynput.mouse import Button, Controller
import os
from os import path
import sys
import pygame
import random
from pygame.locals import *
import time
import threading

pygame.init()
pygame.mixer.init()
ROOT_DIR = os.getcwd()


def run(runfile):
    with open(runfile, "r") as rnf:
        exec(rnf.read())


##Game Settings##
# Colours
BACKGROUND_COLOR = (0, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (130, 130, 0)
LIME_GREEN = (0, 255, 0)
FOREST_GREEN = (0, 150, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
GREY = (123, 123, 123)
RED = (255, 0, 0)
# Game Border/Margin Settings
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 600
GAME_SIZE = WINDOW_HEIGHT * WINDOW_WIDTH
GAME_SIDE_MARGIN = 20
GAME_TOP_MARGIN = 20
GAME_BOTTOM_MARGIN = 20
GAME_BORDER_WIDTH = 3
GAME_TOP_WALL = GAME_TOP_MARGIN + GAME_BORDER_WIDTH
GAME_RIGHT_WALL = WINDOW_WIDTH - GAME_SIDE_MARGIN - GAME_BORDER_WIDTH
GAME_BOTTOM_WALL = WINDOW_HEIGHT - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH
GAME_LEFT_WALL = GAME_SIDE_MARGIN + GAME_BORDER_WIDTH
GAME_FPS = 40
START_GAME = True
ACTUAL_GAME_IS_BEING_PLAYED = True

clock = pygame.time.Clock()
game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
level_font = pygame.font.SysFont('Eurostile Bold Extended', 20, True)
level_equals_font = pygame.font.SysFont('Eurostile Bold Extended', 10, True)
score_font = pygame.font.SysFont('Eurostile Bold Extended', 10, True)
score_equals_font = pygame.font.SysFont('Eurostile Bold Extended', 10, True)
hero_lives_font = pygame.font.SysFont('Eurostile Bold Extended', 10, True)
title_font = pygame.font.SysFont('Eurostile Bold Extended', 35, True)
title_press_start_font = pygame.font.SysFont(
    'Eurostile Bold Extended', 17, True)
title_copyright_font = pygame.font.SysFont('Eurostile Bold Extended', 12, True)
pygame.display.set_caption(' Mouse Autoclicker ')


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
# Main Menu
# Text Renderer


def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.SysFont(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


def main_menu_is_active():
    show_background()
    Show_Menu_Screen = True
    Selected_Option = "PLAY"
    while Show_Menu_Screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and Selected_Option == "QUIT":
                    Selected_Option = "CONTROLS"
                elif event.key == pygame.K_UP and Selected_Option == "PLAY":
                    Selected_Option = "QUIT"
                elif event.key == pygame.K_UP and Selected_Option == "CONTROLS":
                    Selected_Option = "PLAY"
                elif event.key == pygame.K_DOWN and Selected_Option == "PLAY":
                    Selected_Option = "CONTROLS"
                elif event.key == pygame.K_DOWN and Selected_Option == "CONTROLS":
                    Selected_Option = "QUIT"
                elif event.key == pygame.K_DOWN and Selected_Option == "QUIT":
                    Selected_Option = "PLAY"
                if event.key == pygame.K_RETURN:
                    if Selected_Option == "PLAY":
                        Show_Menu_Screen = False
                    if Selected_Option == "QUIT":
                        pygame.quit()
                        quit()

            # Main Menu UI
        game_display.blit(game_display, (0, 0))
        game_display.fill(BACKGROUND_COLOR)
        # title = text_format("   | STAR INVASION |", 'Eurostile Bold Extended', 70, WHITE)
        if Selected_Option == "PLAY":
            text_start = text_format(
                "PLAY", 'Eurostile Bold Extended', 40, WHITE)
        else:
            text_start = text_format(
                "PLAY", 'Eurostile Bold Extended', 40, GREY)
        if Selected_Option == "CONTROLS":
            text_controls = text_format(
                "CONTROLS", 'Eurostile Bold Extended', 40, YELLOW)
        else:
            text_controls = text_format(
                "CONTROLS", 'Eurostile Bold Extended', 40, ORANGE)
        if Selected_Option == "QUIT":
            text_quit = text_format(
                "QUIT", 'Eurostile Bold Extended', 40, WHITE)
        else:
            text_quit = text_format(
                "QUIT", 'Eurostile Bold Extended', 40, GREY)

        start_rect = text_start.get_rect()
        quit_rect = text_quit.get_rect()
        controls_rect = text_controls.get_rect()
        game_display.blit(
            text_start, (WINDOW_WIDTH/2 - (start_rect[2]/2), 300))
        game_display.blit(text_quit, (WINDOW_WIDTH/2 - (quit_rect[2]/2), 420))
        game_display.blit(text_controls, (WINDOW_WIDTH /
                          2 - (controls_rect[2]/2), 360))
        title_text = title_font.render('| STAR INVASION |', False, CYAN)
        title_press_start_text = title_press_start_font.render(
            'PRESS ENTER TO START', False, RED)
        title_copyright_text = title_copyright_font.render(
            '©2019 JOHN WILLIAM JONES III | TRUECODERS', False, BLUE)
        pygame.display.flip()
        clock.tick(GAME_FPS)


def show_background():
    game_display.blit(game_display, (0, 0))
    game_display.fill(BACKGROUND_COLOR)
    pygame.draw.rect(game_display, (BLACK), (GAME_SIDE_MARGIN, GAME_TOP_MARGIN,
                     WINDOW_WIDTH - GAME_SIDE_MARGIN * 2, WINDOW_HEIGHT - GAME_BOTTOM_MARGIN * 2))
    pygame.draw.rect(game_display, (BACKGROUND_COLOR), (GAME_LEFT_WALL, GAME_TOP_WALL, WINDOW_WIDTH - GAME_LEFT_WALL -
                     GAME_SIDE_MARGIN - GAME_BORDER_WIDTH, WINDOW_HEIGHT - GAME_TOP_WALL - GAME_BOTTOM_MARGIN - GAME_BORDER_WIDTH))


def pause_game():
    game_is_paused = True
    while game_is_paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_is_paused = False
                ACTUAL_GAME_IS_BEING_PLAYED = False
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    game_is_paused = False

        clock.tick(GAME_FPS)


# Main Menu Is Open, Game Should Return To Main Menu After Death
ACTUAL_GAME_IS_BEING_PLAYED = True
while ACTUAL_GAME_IS_BEING_PLAYED == True:
    main_menu_is_active()
    while START_GAME:
        handle_events()
        # Display Background and Game Objects
        show_background()
        # Display score and UI
        pygame.display.update()
        clock.tick(GAME_FPS)

# Beginning of Autoclicker Code
# pynput.keyboard is used to watch events of
# keyboard for start and stop of auto-clicker


# four variables are created to
# control the auto-clicker
delay = 0.001
button = Button.right
start_stop_key = KeyCode(char='a')
stop_key = KeyCode(char='b')

# threading.Thread is used
# to control clicks


class ClickMouse(threading.Thread):

  # delay and button is passed in class
  # to check execution of auto-clicker
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # method to check and run loop until
    # it is true another loop will check
    # if it is set to true or not,
    # for mouse click it set to button
    # and delay.
    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


# instance of mouse controller is created
mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


# on_press method takes
# key as argument
def on_press(key):

  # start_stop_key will stop clicking
  # if running flag is set to true
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()

    # here exit method is called and when
    # key is pressed it terminates auto clicker
    elif key == stop_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
