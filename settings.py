class Settings:
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""
    
    def __init__(self):
        """Início das configurações do jogo"""
        #Configurações de tela
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (95, 158, 160)
        
        #Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #Configurações da nave
        self.ship_speed = 1.5
        