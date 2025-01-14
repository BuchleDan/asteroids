import sys
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, shots)

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for obj in updateable:
            obj.update(dt)
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                print("Game Over!")
                sys.exit()
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()

        screen1.fill("black")

        for obj in drawable:
            obj.draw(screen1)

        pygame.display.flip()

        #limt the framerate
        dt = clock.tick(60.0)/1000

if __name__ == "__main__":
    main()