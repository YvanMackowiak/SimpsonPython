import pygame
import random


# creation de la class monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/bart.png')
        self.image = pygame.transform.scale(self.image, (200, 200)) # change la taile du monstre (bart)
        self.rect = self.image.get_rect()
        self.rect.x = 1600 + random.randint(0, 300)
        self.rect.y = 620
        self.velocity = random.randint(1, 4)

    def damage(self, amount):
        # infliger les degats
        self.health -= amount

        # Verifier si le nbr de points de vie est inferieur ou egale a 0
        if self.health <= 0:
            # reapparaitre comme un nouveau monstre (bart)
            self.rect.x = 1600 + random.randint(0, 300)
            self.velocity = random.randint(1, 4)
            self.health = self.max_health

            # si la barre d'evenement est chargé a son maximum
            if self.game.comet_event.is_full_loaded():
                # retirer du jeu
                self.game.all_monsters.remove(self)

                # appel de la méthode pour declencher la pluie
                self.game.comet_event.attempt_fall()

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 40, self.rect.y - 20, self.max_health, 5])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 40, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le deplacement ne se fait que si il n'y a pas de collision
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity # deplacement de bart
        # si le monstre (bart) est en colisiont avec le joueur (homer)
        else:
            # infliger des degats
            self.game.player.damage(self.attack)