import pygame

class Ball:
    def __init__(self, width, height):
        self.x = width // 2
        self.y = height // 2
        self.radius = 25
        self.step = 20
        self.width = width
        self.height = height

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.radius - self.step >= 0:
            self.x -= self.step
        if keys[pygame.K_RIGHT] and self.x + self.radius + self.step <= self.width:
            self.x += self.step
        if keys[pygame.K_UP] and self.y - self.radius - self.step >= 0:
            self.y -= self.step
        if keys[pygame.K_DOWN] and self.y + self.radius + self.step <= self.height:
            self.y += self.step

    def draw(self, screen):
        pygame.draw.circle(screen, (181, 136, 40), (self.x, self.y), self.radius)