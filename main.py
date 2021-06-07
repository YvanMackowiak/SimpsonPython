import pygame
import math
from game import Game

pygame.init()

# generer la fenetre du jeu
pygame.display.set_caption("simpson")  # titre de la fenetre
screen = pygame.display.set_mode((1600, 820))  # taile de la fenetre

# l'arriere plan du jeu
background = pygame.image.load('assets/fond.jpg')

# charger la banniere
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (250, 250))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 2 - 100)
banner_rect.y = math.ceil(screen.get_height() / 2 - 200)

# charger le bouton pour lancer le jeu
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 160))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 2 - 155)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger le jeux
game = Game()

running = True

# boucle tant que running vrai ( permet de laisser la fenetre ouvert )
while running:

    # appliquer l'arriere plan du jeux
    screen.blit(background, (0, -200))

    # verifier si le jeux a commencer ou non
    if game.is_playing:
        # declenche les instruction de la partie
        game.update(screen)
    # verifier si le jeu n'a pas commencé
    else:
        # ajoute mon ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre a jour l'ecran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # verifier evenemebt et fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detecte la touche grace au dictionaire vide pressed
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # detecte si la touche espace est enclenché pour lancer le projectile
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                # le jeu passe en monde " lancé "
                game.start()
