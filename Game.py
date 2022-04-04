import pygame
from Settings import Settings
import GameFunctions
from Ball import Ball
from Player import Player
from Scores import Score
from Timer import Timer
import sys

class Game:
    def __init__(self):
        
        pygame.mixer.pre_init(44100,-16,2,1024)
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Pong")
        self.ball = Ball(self.settings)
        self.player1 = Player(self.settings, 10, 140, self.settings.screen_width-20,self.settings.screen_height/2-70) #Human
        self.player2 = Player(self.settings, 10, 140, 10,self.settings.screen_height/2-70) #Computer

        self.scoreP1 = Score()
        self.scoreP2 = Score()

        self.player2.player_speed = self.settings.player_opponent_speed #change speed in settings to increase difficulty of computer

        self.timer = Timer()
        self.WIN = False


    def Play(self):
        while True:
            if self.WIN == False:
                #Move ball
                GameFunctions.moveBall(self.ball, self.settings,self.scoreP1, self.scoreP2, self.timer)
            
                #Check collisions ball and players
                GameFunctions.checkPlayerHitBall(self.ball, self.player1, self.player2, self.settings)

                #Move player
                GameFunctions.movePlayerHuman(self.player1, self.settings)

                #Move player computer depends of ball
                GameFunctions.movePlayerComputer(self.player2, self.ball, self.settings)

                #Visuals
                GameFunctions.drawObjects(self.screen, self.ball,self.player1,self.player2, self.settings)

                #Check if sb win
                self.WIN = GameFunctions.CheckWin(self.scoreP1, self.scoreP2)


                #Create text
                if self.timer.R:
                    GameFunctions.ball_start(self.settings,self.timer,self.screen)
            else:

                if self.scoreP1.score > self.scoreP2.score:
                    GameFunctions.createText(self.settings,self.settings.player_color,self.screen,470,150, "Win")
                elif self.scoreP2.score > self.scoreP1.score:
                    GameFunctions.createText(self.settings,self.settings.player_color,self.screen,470,150, "Lose")

                #Restart the game

                answer = input("One more time? [Y/N]")

                if answer.lower() == 'n':
                    pygame.quit()
                    sys.exit()
                else:
                    break


            GameFunctions.createText(self.settings,self.settings.player_color,self.screen,520,350, self.scoreP1.score)
            GameFunctions.createText(self.settings,self.settings.player_color,self.screen,465,350, self.scoreP2.score)

            GameFunctions.checkEvent(self.player1,self.settings)

            pygame.display.flip()
            self.clock.tick(60)



while True:

    game = Game()
    game.Play()