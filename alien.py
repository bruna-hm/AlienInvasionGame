import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe para representar um alien e configurar sua posição inicial"""
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        
        self.image = pygame.image.load('AlienInvasionGame\images\Alien.BMP')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
        