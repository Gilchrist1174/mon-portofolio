# comet.py
import pygame
import random

class Comet(pygame.sprite.Sprite):
    def __init__(self, game, x_range=(0, 800)):
        super().__init__()
        self.image = pygame.image.load('meteo.png')
        self.image = pygame.transform.scale(self.image, (175, 175))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(4, 6)
        self.rect.x = random.randint(*x_range)
        self.rect.y = -random.randint(100, 800)
        self.comet_event = game.comet
        self.screen = game.screen
        self.all_comets = self.comet_event.all_comets  # ✅ correction

    def remove(self):
        self.comet_event.all_comets.remove(self)
        if len(self.comet_event.all_comets) == 0:
            print('the event is over')
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False
            # ✅ réapparition des monstres
            self.comet_event.game.spawn_monster() # Changed to spawn pairs
            self.comet_event.game.spawn_monster() # Changed to spawn pairs

    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y > self.screen.get_height():
            print('💥 Comète hors écran')
            self.remove()
