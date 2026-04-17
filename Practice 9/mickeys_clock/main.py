import pygame
import sys
from clock import MickeyClock

pygame.init()

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock = pygame.time.Clock()
mickey = MickeyClock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # выход по кнопке Q
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False

    mickey.draw(screen)

    pygame.display.flip()
    clock.tick(1)

pygame.quit()
sys.exit()