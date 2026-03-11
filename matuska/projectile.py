# projectile.py
import pygame
#definir la classe de notre projectile
class Projectile(pygame.sprite.Sprite):
    #definir le construteur de notre jeu
     def __init__(self,player):
         super().__init__()
         self.velocity=2
         self.player=player
         self.image= pygame.image.load("Modeur.png")
         self.image=pygame.transform.scale(self.image,(60,60))
         self.rect = self.image.get_rect()
         self.rect.x=player.rect.x+120
         self.rect.y=player.rect.y+80


     def move(self):
         self.rect.x += self.velocity
         for monster in  self.player.game.check_collision(self,self.player.game.all_monsters):
             self.remove()
             monster.damage(self.player.attack)

             self.player.all_projectiles.remove(self)
             print('Projectile Collision')
             # verifier si notre projectile n'est plus présent sur notre écran
