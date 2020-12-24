import pygame
import grid

if __name__ == '__main__':
    chessGrid = grid.Grid()
    chessGrid.setScreen()
    chessGrid.drawGrid()

    running = True
    pawn = pygame.image.load('images/pawn.png')

    # Game loop
    while running:
        # if quit event is called stop loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        chessGrid.showGrid()
        chessGrid.screen.blit(pawn, (0, 0))
