# monster.py
import pygame
import random
from comet_event import CometFallEvent

class Monster(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack=0.3
        self.attack_cooldown = 0  # NEW: Cooldown for shooting
        self.last_shot_time = pygame.time.get_ticks()  # NEW: To manage cooldown
        self.image=pygame.image.load('monster.gif')
        self.image=pygame.transform.scale(self.image,(120,120))
        self.rect = self.image.get_rect()
        self.rect.x=950+random.randint(0,300)
        self.rect.y=550
        self.velocity=random.randint(1,2) # This remains, but can be overridden when spawning pairs

    def damage(self,amount):
        self.health -= amount
        if self.health <= 0:
              self.rect.x=1000+random.randint(0,1000)
              self.velocity=random.randint(1,2)
              self.health=self.max_health

        if self.game.comet.is_full_loaded():
            self.game.all_monsters.remove(self)



    def update_health_bar(self,surface):
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        # Check for collision with players before moving
        collided_players = self.game.check_collision(self,self.game.all_players)
        if not collided_players: # If no collision, move normally
            self.rect.x-=self.velocity
        else:
            self.game.player.damage(self.attack)

