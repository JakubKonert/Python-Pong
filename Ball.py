import pygame

class Ball:
    def __init__(self,settings):
        self.x = settings.ball_x
        self.y = settings.ball_y
        self.width = settings.ball_width
        self.height = settings.ball_height

        self.ball_rect = pygame.Rect(settings.ball_width,settings.ball_height,self.x,self.y)
