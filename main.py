import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Bullet
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    
    updateable = pygame.sprite.Group()

    drawable = pygame.sprite.Group()

    asteroids = pygame.sprite.Group()

    bullets = pygame.sprite.Group()

    Player.containers = (updateable, drawable)

    Asteroid.containers = (asteroids, updateable, drawable)

    AsteroidField.containers = updateable

    Bullet.containers = (updateable, drawable, bullets)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        updateable.update(dt)
        for asteroid in asteroids:
            if player.collision_check(asteroid):
                print("Game over!")
                sys.exit()

            for item in bullets:
                if asteroid.collision_check(item):
                    item.kill()
                    asteroid.split()

        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
