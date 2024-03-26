class Settings:
    """Uma classe para armazenar todas as configurações da Invasão Alienígena"""
    
    def __init__(self):
        """Início das configurações do jogo"""
        #Configurações de tela
        self.screen_width = 1200
        self.screen_height = 750
        self.bg_color = (95, 158, 160)
        
        #Bullet settings
        self.bullet_width = 100
        self.bullet_height = 10
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #Configurações da nave
        self.ship_limit = 3
        
        #Alien settings
        self.fleet_drop_speed = 10
        
        self.speedup_scale = 1.1
        
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        self.ship_speed = 1.5
        self.bullet_speed = 4
        self.alien_speed = 1.0
        
        self.fleet_direction = 1
        
        self.aliens_points = 50
        
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        