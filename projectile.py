import pygame


# class qui gere le projectile du joueur
class Projectile(pygame.sprite.Sprite):  # projectile est une classe enfant qui hérite de sprite

    # constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.image = pygame.image.load('assets/biere.png')
        self.image = pygame.transform.scale(self.image, (50, 50))  # permet de redimensionner l'image du projectile
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 450  # positione le projectile au niveau du joueur
        self.rect.y = player.rect.y + 210
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # fait tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)  # permet de faire la rotation par rapport au centre

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity  # pour faire avance le projectile
        self.rotate()

        # verifier si le projectile entre en collision avec bart
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            # supprime le projectile
            self.remove()
            # infliger des dégats
            monster.damage(self.player.attack)  # je recupere les points d'attaque du joueur

        # verifier si le projectile n'est plus present sur l'ecran
        if self.rect.x > 1540:
            # supprimer le projectile vue qu'il est sortie de ecran
            self.remove()
            print("projectile sup")
