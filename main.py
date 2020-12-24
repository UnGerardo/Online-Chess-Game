import pygame
import grid

if __name__ == '__main__':
    running = True

    # Game loop
    while running:
        # if quit event is called stop loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        grid.showGrid()
