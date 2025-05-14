import pygame

from constants import *
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
from player import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        player_triangle = Player(
            (SCREEN_WIDTH / 2),
            (SCREEN_HEIGHT / 2)
        )
        player_triangle.draw(screen)

        pygame.display.flip()

        clock.tick(60)
        dt = clock.tick()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()

