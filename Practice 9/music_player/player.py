import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        base_path = os.path.dirname(__file__)
        music_path = os.path.join(base_path, "music")

        self.playlist = [
            os.path.join(music_path, "track1.mp3"),
            os.path.join(music_path, "track2.mp3"),
        ]

        self.current = 0
        self.is_playing = False

    def play(self):
        try:
            pygame.mixer.music.load(self.playlist[self.current])
            pygame.mixer.music.play()
            self.is_playing = True
        except Exception as e:
            print("❌ Ошибка загрузки музыки:", e)

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next(self):
        self.current = (self.current + 1) % len(self.playlist)
        self.play()

    def previous(self):
        self.current = (self.current - 1) % len(self.playlist)
        self.play()

    def get_current_track(self):
        return os.path.basename(self.playlist[self.current])