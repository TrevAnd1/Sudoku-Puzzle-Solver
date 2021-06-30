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
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

WHITE = (255,255,255)

def drawBackground(self):
    for i in range(9):
        for j in range(9):
            self.square = pygame.Surface((60,60))
            self.square.fill(WHITE)

running = True

while running:

    drawBackground()

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False


SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1600

pygame.init()