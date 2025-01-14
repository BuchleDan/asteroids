import pygame
from constants import *
from player import Player

def main():
    pygame.init
    screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    x = (SCREEN_WIDTH/2)
    y = (SCREEN_HEIGHT/2)
    player = Player(x, y)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen1.fill("black")

        player.draw(screen1)
        player.update(dt)

        pygame.display.flip()

        #limt the framerate
        dt = clock.tick(60.0)/1000

if __name__ == "__main__":
    main()