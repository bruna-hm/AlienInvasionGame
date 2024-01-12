import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Classe overall para gerenciar assets e comportamento"""

    def __init__(self):
        """Inicializar o jogo e criar recursos de jogo"""
        
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Invasão Alienígena!!!")
    
        self.ship = Ship(self)
    
    def run_game(self):
        """Inicia o loop principal, main para o jogo"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        # Aguarda por eventos de teclado ou mouse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                    
    def _check_keydown_events(self, event):
        """Responde ao pressionamento de tecla"""
        if event.key == pygame.K_RIGHT:
        # Mover a nave para a direita
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        
    def _check_keyup_events(self, event):
        """Responde ao soltar de teclas"""    
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
            
    def _update_screen(self):
        #Atualiza imagens da tela, e flip para nova tela
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        
        pygame.display.flip()
            
if __name__ == '__main__':
    #Faça uma instância do jogo e run.
    ai = AlienInvasion()
    ai.run_game()