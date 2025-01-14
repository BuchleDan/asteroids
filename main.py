import sys
import os
import pygame
from constants import *
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init
    pygame.font.init()
    screen1 = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    score = 0
    one_up = 0
    score_increment = 1
    lives = 3
    font = pygame.font.Font(None, 36)
    
    
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = (updateable)
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, lives)

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Good Bye!")
                sys.exit()
            
        for obj in updateable:
            obj.update(dt)

        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        lives_text = font.render(f'Lives: {player.lives}', True, (255, 255, 255))
        
        
        for asteroid in asteroids:
            if asteroid.is_colliding(player):
                if player.lives <= 0:
                    print("Game Over!")
                    sys.exit()
                asteroid.kill()
                player.lose_life()                
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    score += score_increment
                    one_up += score_increment
                    if one_up == 100:
                        one_up = 0
                        player.lives += 1
                    asteroid.split()
                    shot.kill()

        screen1.fill("black")

        for obj in drawable:
            obj.draw(screen1)
        screen1.blit(score_text, (10, 10))
        screen1.blit(lives_text, (SCREEN_WIDTH - 110, 10))

        pygame.display.flip()

        #limt the framerate
        dt = clock.tick(60.0)/1000

if __name__ == "__main__":
    main()