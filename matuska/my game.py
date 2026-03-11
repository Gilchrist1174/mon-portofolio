# my_game.py
import pygame
from comet_event import CometFallEvent
from player import Player
from monster import Monster
from comet import Comet
import random
from monster_projectile import MonsterProjectile


class Game():
    def __init__(self,screen_surface):
        self.screen = screen_surface  # Store the screen surface
        self.screen_width = screen_surface.get_width()  # Stocker les dimensions de l'écran
        self.screen_height = screen_surface.get_height()
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)  # Passer l'instance Game
        self.all_players.add(self.player)
        self.comet = CometFallEvent(self)  # Instanciation corrigée
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}

    def start_game(self):
        self.is_playing = True
        self.spawn_monster() # Modified to spawn only two initial monsters

    def game_over(self):
        self.all_monsters = pygame.sprite.Group() # Effacer tous les monstres
        self.comet.all_comets=pygame.sprite.Group() # Corrected from comet_event to comet
        self.player.health = self.player.max_health  # Réinitialiser la santé du joueur
        self.comet.reset_percent()
        self.is_playing = False

        self.player.all_projectiles = pygame.sprite.Group()  # Effacer les projectiles

    def update(self, screen):
        # Appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)
        self.player.update_health_bar(screen)

        self.comet.update_bar(screen) # Mettre à jour la barre d'événement de chute de comète

        # Mettre à jour et dessiner les comètes
        for comet in self.comet.all_comets:
            comet.fall()  # Appel de la méthode fall
            # Check for collision between comet and player
            if self.check_collision(comet, self.all_players):
                self.player.damage(20) # Inflict damage to player
                comet.remove() # Remove comet after collision


        self.comet.all_comets.draw(screen)

        # Mettre à jour et dessiner les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(screen)

        # Mettre à jour et dessiner les monstres
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        self.all_monsters.draw(screen)


        # Check if all monsters are defeated and spawn new ones
        # Only spawn new monsters if comet fall mode is NOT active AND no comets are falling
        # This ensures comet event has priority
        if len(self.all_monsters) == 0 and self.is_playing and not self.comet.fall_mode and len(self.comet.all_comets) == 0:
            self.spawn_initial_monsters()


        # Vérifier l'entrée de mouvement du joueur
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self): # This method is now less used, replaced by spawn_initial_monsters
        monster = Monster(self)
        self.all_monsters.add(monster)

    def spawn_initial_monsters(self): # Modified to spawn exactly two monsters
        if len(self.all_monsters) == 0: # Ensure no monsters are currently active
            monster1 = Monster(self)
            monster2 = Monster(self)
            monster1.velocity = 1 # Vitesses différentes
            monster2.velocity = 2
            self.all_monsters.add(monster1, monster2)
