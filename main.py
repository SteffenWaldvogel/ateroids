import pygame
from asteroidfield import *
from constants import *
from player import Player
import sys
from shot import Shot

def main():
    # Initialize pygame Clock outside the loop
    clock = pygame.time.Clock()
    dt = 0  # Start with delta time as 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatable = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawables)
    Player.containers = (updatable, drawables)
    AsteroidField.containers = (updatable, )
    Shot.containers = (shots, updatable, drawables)
    player_one = Player(x,y)
    asteroidfield = AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        # Clear the screen
        screen.fill(0, rect=None, special_flags=0)

        # Check for quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects
        updatable.update(dt)

        for shot in shots:
            for asteroid in asteroids:
                if asteroid.collision_check(shot):
                    shot.kill()
                    asteroid.split(asteroids)

        # Collision detection between the player and asteroids
        for asteroid in asteroids:  # Iterate through all asteroids in the group
            if player_one.collision_check(asteroid):
                print("GAME OVER")
                pygame.quit()  # Clean up pygame
                sys.exit()  # Exit the program immediately

        # Draw all objects to the screen
        for object in drawables:
            object.draw(screen)

        # Update the screen
        pygame.display.flip()

        # Control the frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # 60 FPS, converting milliseconds to seconds

if __name__ == "__main__":
    main()