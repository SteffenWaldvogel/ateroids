import pygame
from constants import *  # Import specifically SHOT_RADIUS
from circleshape import CircleShape

print(f"SHOT_RADIUS from import: {SHOT_RADIUS}")  # Debug print

class Shot(CircleShape):
    containers = None
    
    def __init__(self, x, y):
        print(f"In Shot.__init__, SHOT_RADIUS: {SHOT_RADIUS}")  # Debug print
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        
        # Add to containers if defined
        if Shot.containers:
            for container in Shot.containers:
                container.add(self)
                
    def draw(self, screen):
    # Draw the shot as a small white circle
      pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        old_pos = self.position.copy()
        self.position += self.velocity * dt
        # Remove shots when they leave the screen
        if (self.position.x < -self.radius or 
            self.position.x > SCREEN_WIDTH + self.radius or
            self.position.y < -self.radius or 
            self.position.y > SCREEN_HEIGHT + self.radius):
            self.kill()  # Remove from all sprite groups