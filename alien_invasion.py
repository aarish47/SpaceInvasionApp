import pygame
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button
from game_functions import *
from scoreboard import Scoreboard

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invasion - Creators: Aarish & Asif Ali")
    
    background_image = pygame.image.load('images/bg.jpg')
    background_image = pygame.transform.scale(background_image, (ai_settings.screen_width, ai_settings.screen_height))
    
    play_button = Button(ai_settings, screen, "Play Game")
    stats = GameStats(ai_settings)
    ship = Ship(ai_settings, screen)
    bullets = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    sb = Scoreboard(ai_settings, screen, stats)
    
    create_fleet(ai_settings, screen, ship, aliens)
    
    while True:
        check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
        
        update_screen(ai_settings, screen, stats, ship, sb, aliens, bullets, play_button, background_image)

run_game()
