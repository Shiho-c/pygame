import pygame
from pygame import rect 
from pygame.locals import *

from LabelText import LabelText
#import random
pygame.init()  
background = (255, 255, 255)  
black = (0, 0, 0)
window_height = 400
window_width = 400
window = pygame.display.set_mode((window_height, window_width))  
pygame.display.set_caption('Game Testing')  
#load images
game_screenBackground = pygame.image.load('resources/ground.jpg')
clock = pygame.time.Clock()

corbel_font = pygame.font.SysFont('Corbel',35)
  
start_button = LabelText("Start", corbel_font, black, window.get_width() / 2, window.get_height() / 2 - 50 )
quit_button = LabelText("Quit", corbel_font, black, window.get_width() / 2, start_button.get_y() + start_button.get_height() )
player = pygame.image.load('resources/player.png')
playerX, playerY = 0, 0
movementSpeed = 5
game_screen = False
# infinite loop  
run = True 
while run:
    for event in pygame.event.get():  
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor = pygame.mouse.get_pos()
            if start_button.collision(cursor):
                background = (0, 0, 0)
                game_screen = True
            elif quit_button.collision(cursor):
                run = False
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        playerX -= movementSpeed
    if key[pygame.K_RIGHT]:
        playerX += movementSpeed
    if key[pygame.K_UP]:
        playerY -= movementSpeed
    if key[pygame.K_DOWN]:
        playerY += movementSpeed
    if event.type == pygame.QUIT:  
        run = False  
    if playerY >= 400:
        playerY -= 1
    elif playerY < 0:
        playerY += 1
    elif playerX >= 400:
        playerX -= 1
    elif playerX < 0:
        playerX += 1

    if game_screen:
        window.blit(game_screenBackground, game_screenBackground.get_rect())
        window.blit(player, (playerX, playerY))
        #pygame.draw.rect(window, (255, 0, 0), (playerX, playerY, 50, 50))
    else:
        window.fill(background)
        window.blit(start_button.surface(), (start_button.get_x(), start_button.get_y()))
        window.blit(quit_button.surface(), (quit_button.get_x(), quit_button.get_y()))
    clock.tick(60)
    pygame.display.update()
  
pygame.quit()          
#push 
