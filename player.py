import pygame
from projectile import Projectile

# creation d'un class qui represente le joueur
class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health =100
        self.max_health =100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/homer.png') # charge l'image du joueur
        self.rect = self.image.get_rect() # recupere la valeur de image
        self.rect.x = 400 # positione homer au centre de la page sur la valeur x
        self.rect.y = 405 # positione homer au centre de la page sur la valeur y

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si homer n'a plus de point de vie
            self.game.game_over()

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 300, self.rect.y - 20, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 300, self.rect.y - 20, self.health, 7])

    def launch_projectile(self):
        # nouvelle instance de la classe prokectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        # si homer n'est pas en collision avec un mosntre(bart)
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity