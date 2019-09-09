import pygame
import time
import math

from lorentz_transformer import *

pygame.init()

display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

v_set = 0.9 * c

v = v_set

running = True

class Rectangle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(display, (0, 0, 0), transform([self.x, self.y, self.w, self.h], v, t()) if v != 0 else [self.x, self.y, self.w, self.h])

r = Rectangle(10, 10, 50, 10)

while running:
    display.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                v = v_set if v == 0 else 0
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                running = False
                quit()

    r.draw()

    pygame.display.update()

    time.sleep(1.0 / 60)


    print("Real Time: ", t(), "\tRelativistic Time: ", t_(10 + v * t(), v, t()))
    r.draw()
    