import pygame

class Settings:
    def __init__(self):

        #Screen settings
        self.screen_width = 1000
        self.screen_height = 720
        self.bg_color = pygame.Color('grey10')
        
        #Ball settings
        self.ball_x = 30
        self.ball_y = 30
        self.ball_width = self.screen_width/2 -15
        self.ball_height = self.screen_height/2-15
        self.ball_color = (250,225,180)
        self.ball_speed_x = 8
        self.ball_speed_y = 8
        self.ball_speed_default = 8


        #Player settings
        self.player_color = (180,225,250)
        self.player_opponent_speed = 8
        self.player_human_speed = 10


        #Texts settings
        self.game_font = pygame.font.Font("freesansbold.ttf", 32)

        #Game settings
        self.time_to_start = 1500

        #Sounds
        self.pong_sound = pygame.mixer.Sound("pong.ogg")
        self.score_sound = pygame.mixer.Sound("score.ogg")