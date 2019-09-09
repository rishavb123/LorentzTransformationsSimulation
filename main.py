import pygame
import time
import math

from lorentz_transformer import *

pygame.init()

display = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

v_0 = 0.9 * c
x_0 = 10
w_0 = 300

v = v_0

running = True
q = False

class Rectangle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self):
        pygame.draw.rect(display, (200, 200, 200), [self.x, self.y, self.w, self.h])
        pygame.draw.rect(display, (0, 0, 0), transform([self.x, self.y, self.w, self.h], v, t()) if v != 0 else [self.x, self.y, self.w, self.h])

r = Rectangle(x_0, 10, w_0, 10)

while not q:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                v = v_0 if v == 0 else 0
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                q = False
                quit()
            elif event.key == pygame.K_p:
                running = not running

    if running:
        display.fill((255, 255, 255))

        r.draw()

        pygame.display.update()

        print("Real Time: ", t(), "\tRelativistic Time: ", t_(x_0 + v * t(), v, t()))
        r.draw()
    else:
        pass