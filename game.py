from monster import Monster
from player import Player
from comet_event import CommetFallEvent
import pygame


# creation d'un class qui represente le jeu
class Game:

    def __init__(self):
        # definir si le jeu a commencé
        self.is_playing = False
        # genere le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # generer l'evenement
        self.comet_event = CommetFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}  # dictionnaire vide va servire a recuperer les touche du joueur

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # remet le jeu a zero
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.rest_percent()
        self.is_playing = False

    def update(self, screen):
        # applique image du joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la bart de vie de homer
        self.player.update_health_bar(screen)

        # actualiser la barre d'evenement du jeu
        self.comet_event.update_bar(screen)

        # recupere les projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupere bart (le monstre) du jeux
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        # recuperer les donuts du jeu
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images de mon groupe projectiles
        self.player.all_projectiles.draw(screen)  # dessine le contenue du groupe all_projectiles grace a draw

        # appliquer l'ensemble des images du group de "monstre"
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des image du group de comt (donut)
        self.comet_event.all_comets.draw(screen)

        # verifie si le joueur va a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < 1140:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > -250:  # and empeche de sortir de ecrant a gauche
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)
