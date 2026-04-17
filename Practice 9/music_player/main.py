import pygame
import sys
from player import MusicPlayer

pygame.init()

WIDTH, HEIGHT = 500, 300
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)

player = MusicPlayer()
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                player.play()

            if event.key == pygame.K_s:
                player.stop()

            if event.key == pygame.K_n:
                player.next()

            if event.key == pygame.K_b:
                player.previous()

            if event.key == pygame.K_q:
                running = False

    screen.fill((128, 128, 128))

    # текущий трек
    text = font.render("Track: " + player.get_current_track(), True, (128, 0, 32))
    screen.blit(text, (50, 120))

    # подсказки
    info = font.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (128, 0, 32))
    screen.blit(info, (20, 200))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()