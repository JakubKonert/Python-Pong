import pygame

class Player:
    def __init__(self,settings,player_x,player_y,player_width,player_height):
        self.settings = settings
        self.player_x = player_x
        self.player_y = player_y
        self.player_width = player_width
        self.player_height = player_height

        self.player_speed = 0

        self.player_rect = pygame.Rect(self.player_width,self.player_height,self.player_x,self.player_y)