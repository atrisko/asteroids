import pygame
import circleshape
from constants import LINE_WIDTH, SHOT_RADIUS

class Shot(circleshape.CircleShape):
    
    def __init__(self, x, y, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.radius = radius
        self.time_alive = 0.0  # Track how long the shot has been alive
    
    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt):
        self.time_alive += dt
        self.position += self.velocity * dt  
        if self.time_alive > 2.0:  # Remove the shot after 2 seconds
            self.kill()
           
