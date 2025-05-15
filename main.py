#todo:  Add a scoring system
## Whenever an asteroid is destroyed, a counter at the corner of the screen is added to.
### First is to add a number to the corner of the screen; then adding to it should be easy.
# in order to display I'll:
## import pygame.freetype (as this module isn't included in the import pygame)
## create a pygame.freetype.Font('font location(or None)', fontSize)
## display test in game loop with test.render_to(screen, coordinates, 'test word', "color")

import sys
import pygame
import pygame.freetype

from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    test = pygame.freetype.Font(None, 30)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player_triangle = Player((SCREEN_WIDTH / 2), (SCREEN_HEIGHT / 2))
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for obj in asteroids:
            if obj.collision_check(player_triangle):
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision_check(asteroid):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")

        for to_draw in drawable:
            to_draw.draw(screen)

        pygame.freetype.Font('font location(or None)', fontSize)

        pygame.display.flip()

        dt = (clock.tick(60) / 1000)

if __name__ == "__main__":
    main()

