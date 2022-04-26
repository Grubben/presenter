import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode([1000,800])
clock = pygame.time.Clock()

clickable_area = pygame.Rect((0, 0), (1000, 630))
# Define a list to which we add the pygame.Rects.
rects = []

GREEN = (84,173,65)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == QUIT:
            done = True
        if event.type == MOUSEBUTTONDOWN:
            if clickable_area.collidepoint(event.pos):
                # Append a new rect to the rects list.
                rects.append(Rect(event.pos, (70, 70)))

    #menu rectangle
    pygame.draw.rect(window, BLUE, Rect((0, 700), (1000, 10)))
    #server rectangle
    pygame.draw.rect(window, GREEN, Rect((100, 720), (70, 70)))
    pygame.draw.rect(window, GREEN, clickable_area, 3)

    # Draw the rects.
    for rect in rects:
        pygame.draw.rect(window, GREEN, rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
