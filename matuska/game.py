import pygame
from my_game import Game

screen = pygame.display.set_mode((1080,720))
background = pygame.image.load('bg.jpg')
background = pygame.transform.scale(background, (1080,720))
play_button = pygame.image.load('play_back.png').convert()
play_button = pygame.transform.scale(play_button, (400,250))

play_button_rect = play_button.get_rect()
play_button_rect.x = 400
play_button_rect.y =325
game = Game(screen)

running=True
while running:

    # Affichage de l'arrière-plan sur la fenêtre
    screen.blit(background, (0,0))

    if game.is_playing:
        game.update(screen)
    else:
        screen.blit(play_button, play_button_rect)

    pygame.display.flip()
       # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
             running = False
 #mettre en place les évenements du lavier sur notre joueur
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key==pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type==pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Corrected line: event.pos is an attribute, not a method.
            if play_button_rect.collidepoint(event.pos): # Correct usage
                game.start_game()


pygame.quit()
