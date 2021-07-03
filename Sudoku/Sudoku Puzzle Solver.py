import pygame
import random

from pygame.locals import (
    K_1,
    K_2,
    K_3,
    K_4,
    K_5,
    K_6,
    K_7,
    K_8,
    K_9,
    K_RIGHT,
    K_LEFT,
    K_UP,
    K_DOWN,
    K_KP_ENTER,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

WHITE = (0,0,0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
]

# TODO : get user input to see how many numbers they want to start with given on the board and use that number in line 54 in a 'for' loop to interate through 'board' as many times as the user wants in their input

class Board():

    def __init__(self):
        pass

    def drawBackground(self): # use pygame.draw.line() to make lines for the board
        pass

    def initializeBoard(self): # set 0's in board to random numbers between one and 10 so that they can be solved
        rand_row = random.randint(0,8)
        rand_col = random.randint(0,8)
        board[rand_row][rand_col] = random.randint(1,9) # TODO : check if the spot that it randomly chooses already has a number in it (if board[rand_row][rand_col] != 0)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

running = True

while running:

    screen.fill((WHITE))

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
