import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)
    
    def draw(self, screen):
        width = 2
        pygame.draw.circle(screen, "red", self.position, self.radius, width)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self, asteroids):
        new_angle = random.uniform(20, 50)
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return 
        else:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            rotated_vector_1 = self.velocity.rotate(new_angle) * 1.2
            rotated_vector_2 = self.velocity.rotate(-new_angle) * 1.2

            # Create two smaller asteroids with the same position as the current asteroid
            asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_1.velocity = rotated_vector_1

            asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_2.velocity = rotated_vector_2
            asteroids.add(asteroid_1)
            asteroids.add(asteroid_2)

# Create two new Asteroid objects with these attributes