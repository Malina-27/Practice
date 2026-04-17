import pygame
import datetime
import math
import os

class MickeyClock:
    def __init__(self):
        self.center = (300, 300)

        # правильный путь к картинке (РАБОТАЕТ ВСЕГДА)
        base_path = os.path.dirname(__file__)
        image_path = os.path.join(base_path, "images", "mickey_hand.png")

        self.bg = pygame.image.load(image_path).convert_alpha()
        self.bg = pygame.transform.scale(self.bg, (600, 600))

    def draw_hand(self, screen, angle, length, color, width):
        x = self.center[0] + length * math.cos(math.radians(angle))
        y = self.center[1] + length * math.sin(math.radians(angle))

        pygame.draw.line(screen, color, self.center, (x, y), width)

        # "перчатка" (чтобы было похоже на руку)
        pygame.draw.circle(screen, (0, 0, 0), (int(x), int(y)), 10)

    def draw(self, screen):
        screen.blit(self.bg, (0, 0))

        now = datetime.datetime.now()
        sec = now.second
        minute = now.minute

        # углы (12 часов вверх)
        sec_angle = sec * 6 - 90
        min_angle = minute * 6 - 90

        # секунды (левая рука)
        self.draw_hand(screen, sec_angle, 150, (255, 0, 0), 5)

        # минуты (правая рука)
        self.draw_hand(screen, min_angle, 100, (255, 255, 0), 8)

        # центр
        pygame.draw.circle(screen, (0, 0, 0), self.center, 6)