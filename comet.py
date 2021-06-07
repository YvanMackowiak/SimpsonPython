import pygame
import random

# creer la classe comete
class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        # definir l'image associé
        self.image = pygame.image.load('assets/donut.png')
        self.image = pygame.transform.scale(self.image, (65, 65)) # change la taile du donut
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 1600)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # verifier si le nombre de donut et de 0
        if len(self.comet_event.all_comets) == 0:
            print(" evenement fini")
            # remettre la barre a 0
            self.comet_event.rest_percent()
            # apparaitre bart
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # ne tombe pas sur le sol
        if self.rect.y >= 650:
            print("sol")
            # retirer la donut
            self.remove()

        # verifie si la boule touche le joueur
        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_players
        ):
            print("joueur toucher")
            # retirer la boule de feu
            self.remove()
            # redonne 20 point de vie
            self.comet_event.game.player.damage(-20)