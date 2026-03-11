# player.py
import pygame
from projectile import Projectile



class Player(pygame.sprite.Sprite):

    #la methode self permet de recupérer toutes les données liées a la classe définit pour le joueur

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.all_monsters = pygame.sprite.Group()
        self.health=100
        #permet de recuperer le nombre maximal de points de vie du joueur
        self.max_health=100
        self.attack=10
        self.velocity=3 # Initial player velocity
        self.all_projectiles=pygame.sprite.Group()
        self.image=pygame.image.load('remove.png')
        self.image=pygame.transform.scale(self.image,(200,250))
        self.rect = self.image.get_rect()
        self.rect.x=250
        self.rect.y=500

    def launch_projectile(self):
        self.all_projectiles.add(Projectile(self))

    def damage(self,amount):
        if amount  < self.health-amount:
         self.health -= amount

        else:
            self.game.game_over()

    def update_health_bar(self,surface):
        pygame.draw.rect(surface, (60,63,60), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def move_right(self):

        self.rect.x += self.velocity
        collided_monsters = self.game.check_collision(self, self.game.all_monsters)
        if collided_monsters:

            self.rect.x -= self.velocity

            for monster in collided_monsters:
                monster.velocity = 1


    def move_left(self):
        # Temporarily move the player to predict the next position
        self.rect.x -= self.velocity
        collided_monsters = self.game.check_collision(self, self.game.all_monsters)
        if collided_monsters:
            # If moving left causes a collision, revert the move
            self.rect.x += self.velocity
            for monster in collided_monsters:
                monster.velocity = 0
