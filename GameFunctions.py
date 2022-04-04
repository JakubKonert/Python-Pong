import pygame
import sys
import random
from Texts import Text


def checkEvent(player1,settings):
    for event in pygame.event.get():
        if  event.type == pygame.QUIT or event.type == pygame.K_QUOTE:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            keyDown(event,player1,settings)

        if event.type == pygame.KEYUP:
            keyUp(event,player1,settings)


def drawObjects(screen, ball, player1, player2,settings):
    screen.fill(settings.bg_color)
    pygame.draw.rect(screen, settings.player_color,player1.player_rect)
    pygame.draw.rect(screen, settings.player_color,player2.player_rect)
    pygame.draw.aaline(screen,settings.ball_color,(settings.screen_width/2,0),(settings.screen_width/2,settings.screen_height))
    pygame.draw.ellipse(screen,settings.ball_color,ball.ball_rect)


def ball_restart(ball, settings,timer):

    ball.ball_rect.center = (settings.screen_width/2,settings.screen_height/2)
    settings.ball_speed_y = 0
    settings.ball_speed_x = 0

    timer.timer = pygame.time.get_ticks()
    timer.R = True

def ball_start(settings,timer,screen):

    current_time = pygame.time.get_ticks()

    createText(settings,settings.player_color,screen,465,10, round((settings.time_to_start-(current_time-timer.timer))/1000,2))

    if current_time - timer.timer > settings.time_to_start:
        settings.ball_speed_y = settings.ball_speed_default * random.choice((-1,1))
        settings.ball_speed_x = settings.ball_speed_default * random.choice((-1,1))
        timer.R = False
        timer.timer = 0
        


def keyDown(event,player1,settings):
    if event.key == pygame.K_DOWN:
        player1.player_speed += settings.player_human_speed

    if event.key == pygame.K_UP:
        player1.player_speed -= settings.player_human_speed


def keyUp(event,player1,settings):
    if event.key == pygame.K_DOWN:
        player1.player_speed -= settings.player_human_speed

    if event.key == pygame.K_UP:
        player1.player_speed += settings.player_human_speed


def moveBall(ball, settings, scoreP1, scoreP2, timer):
    ball.ball_rect.x += settings.ball_speed_x
    ball.ball_rect.y += settings.ball_speed_y

    if ball.ball_rect.top <=0 or ball.ball_rect.bottom >= settings.screen_height:
        settings.ball_speed_y *= -1

        pygame.mixer.Sound.play(settings.pong_sound)

    if ball.ball_rect.left <=0:
        pygame.mixer.Sound.play(settings.score_sound)

        scoreP1.score += 1
        ball_restart(ball, settings,timer)

    if ball.ball_rect.right >= settings.screen_width:
        pygame.mixer.Sound.play(settings.score_sound)

        scoreP2.score += 1
        ball_restart(ball, settings,timer)


def checkPlayerHitBall(ball, player1, player2, settings):
    if ball.ball_rect.colliderect(player1.player_rect) and settings.ball_speed_x > 0:
        pygame.mixer.Sound.play(settings.pong_sound)

        if abs(ball.ball_rect.right - player1.player_rect.left) < 10:
            settings.ball_speed_x *= -1

        elif abs(ball.ball_rect.bottom - player1.player_rect.top) < 10 and (settings.ball_speed_y > 0):
            settings.ball_speed_y *= -1

        elif abs(ball.ball_rect.top - player1.player_rect.bottom) < 10 and (settings.ball_speed_y < 0):
            settings.ball_speed_y *= -1

    if ball.ball_rect.colliderect(player2.player_rect) and settings.ball_speed_x < 0:
        pygame.mixer.Sound.play(settings.pong_sound)

        if abs(ball.ball_rect.left - player2.player_rect.right) < 10:
            settings.ball_speed_x *= -1

        elif abs(ball.ball_rect.bottom - player2.player_rect.top) < 10 and (settings.ball_speed_y > 0):
            settings.ball_speed_y *= -1

        elif abs(ball.ball_rect.top - player2.player_rect.bottom) < 10 and (settings.ball_speed_y < 0):
            settings.ball_speed_y *= -1


def movePlayerHuman(player1, settings):
    player1.player_rect.y += player1.player_speed

    if player1.player_rect.top <= 0:
        player1.player_rect.top = 0

    if player1.player_rect.bottom >= settings.screen_height:
        player1.player_rect.bottom = settings.screen_height


def movePlayerComputer(player2, ball, settings):
    if player2.player_rect.top < ball.ball_rect.y:
        player2.player_rect.top += player2.player_speed

    if player2.player_rect.bottom > ball.ball_rect.y:
        player2.player_rect.bottom -= player2.player_speed

    if player2.player_rect.top <= 0:
        player2.player_rect.top = 0

    if player2.player_rect.bottom >= settings.screen_height:
        player2.player_rect.bottom = settings.screen_height


def createText(settings,color,screen,x,y,text_to_write):
    text = Text(settings.game_font)
    text.putText(text_to_write,color,screen,x,y)


def CheckWin(scoreP1, scoreP2):
    if scoreP1.score > 3 and ((scoreP1.score - scoreP2.score) >=2):
        return True

    if scoreP2.score > 3 and ((scoreP2.score - scoreP1.score) >=2):
        return True

    return False

