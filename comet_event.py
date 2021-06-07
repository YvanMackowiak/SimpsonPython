import pygame
from comet import Comet

# créer une classe pour la gestion de evenemet
class CommetFallEvent:

    # au chargement on créer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 33
        self.game = game
        self.fall_mode = False

        # definir un groupe de sprite pour stocker les cometes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def rest_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            # appraitre un premier donut
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'event est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de cometes !!")
            self.meteor_fall()
            self.fall_mode = True # active l'evenement

    def update_bar(self, surface):

        # ajouter du % a la bar
        self.add_percent()

        # la barre noir en arriere plan
        pygame.draw.rect(surface, (0 ,0 ,0), [
            0, # axe des x
            surface.get_height() - 20, # axe des y
            surface.get_width(),# longueur de la fenetre
            10 # epaisseur de la barre
        ])
        # barre rouge (jauge d'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height()- 20,  # axe des y
            (surface.get_width() / 100) * self.percent ,  # longueur de la fenetre
            10  # epaisseur de la barre
        ])