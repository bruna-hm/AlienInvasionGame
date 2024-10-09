import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Uma classe para gerenciar a nave"""
    
    def __init__(self, ai_game):
       super().__init__() 
       self.screen = ai_game.screen
       self.settings = ai_game.settings
       self.screen_rect = ai_game.screen.get_rect()
       
       #Carrega imagem da nava e toma seu rect
       self.image = pygame.image.load('./images/SpaceShip.bmp')
       self.rect = self.image.get_rect()
       
       #Começa toda nova nave no centro da tela
       self.rect.midbottom = self.screen_rect.midbottom
       
       #Armazenar um float para a posição horizontal exata da nave
       self.x = float(self.rect.x)
       self.y = float(self.rect.y)
        
       #Flag de movimento; comece com uma nave que não está se movendo
       self.moving_right = False
       self.moving_left = False
       self.moving_up = False
       self.moving_down = False
        
    def update(self):
        """Atualize a posição da nave baseado na flag de movimento"""
        #Atualiza o valor de x da nave, não o rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom: 
            self.y += self.settings.ship_speed
        #atualiza objeto rect do self.x.
        self.rect.x = self.x
        self.rect.y = self.y
       
    def blitme(self):
        """Desenha a nave no seu local atual"""
        self.screen.blit(self.image, self.rect)
 
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)