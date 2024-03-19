import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Classe para gerenciar as balas atiradas pela nave"""
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Criar um rect da bala em (0, 0) e então configurar a posição correta
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #Armazena a posição da bala como um float
        self.y = float(self.rect.y)
        
    def update(self):
        """Move a bala para o topo da tela"""
        #Atualiza a posição exata da bala
        self.y -= self.settings.bullet_speed
        #Atualiza a posição do rect
        self.rect.y = self.y
            
    def draw_bullet(self):
        """Desenha a bala na tela"""
        pygame.draw.rect(self.screen, self.color, self.rect)
            