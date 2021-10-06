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
#bgm
game_bgm = pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.load('resources/Town 3.mp3')
pygame.mixer.music.play()
corbel_font = pygame.font.SysFont('Corbel',35)
  
start_button = LabelText("Start", corbel_font, black, window.get_width() / 2, window.get_height() / 2 - 50 )
option_button = LabelText("Option", corbel_font, black, window.get_width() / 2, start_button.get_y() + start_button.get_height() + 50 )
quit_button = LabelText("Quit", corbel_font, black, window.get_width() / 2, option_button.get_y() + option_button.get_height() + 50 )
player = pygame.image.load('resources/player.png')
player = pygame.transform.scale(player, (50, 50))
playerX, playerY = 0, 0
optionX = 0
optionY = 0
option_screenBackground = pygame.draw.rect(window, (255, 0, 0),(optionX, optionY, 0, 0))
movementSpeed = 5
game_screen = False
option_screen = False
# infinite loop  
run = True 
while run:
    cursor = pygame.mouse.get_pos()
    for event in pygame.event.get():  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collision(cursor):
                background = (0, 0, 0)
                
                pygame.mixer.music.stop()
                game_screen = True
            elif quit_button.collision(cursor):
                pygame.mixer.music.stop()
                run = False
            elif option_button.collision(cursor):
                option_screen = False
                
            
                


    if playerX + player.get_width() >= window_width:
         playerX -= movementSpeed
    elif playerX < 1:
        playerX =+ movementSpeed
    elif playerY + player.get_height() >= window_height:
        playerY -= movementSpeed
    elif playerY < 1:
        playerY += movementSpeed
    else:
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

   
    if game_screen == True:
        window.blit(game_screenBackground, game_screenBackground.get_rect())
        window.blit(player, (playerX, playerY))
        
        #pygame.draw.rect(window, (255, 0, 0), (playerX, playerY, 50, 50))
    elif option_screen == True:
        window.blit(option_screenBackground,option_screenBackground.get_rect())
        pygame.draw.rect(window, (255, 0, 0), (optionX, optionY, 50, 50))
        #print('test')
    else:
        if start_button.collision(cursor):
            start_button.change_color((255,0, 0))
        elif quit_button.collision(cursor):
            quit_button.change_color((255,0, 0))
        elif option_button.collision(cursor):
            option_button.change_color((255,0, 0))
        
        else:
            start_button.change_color((0,0, 0))
            option_button.change_color((0,0, 0))
            quit_button.change_color((0,0, 0))
        window.fill(background)
        window.blit(start_button.surface(), (start_button.get_x(), start_button.get_y()))
        window.blit(option_button.surface(), (option_button.get_x(), option_button.get_y()))
        window.blit(quit_button.surface(), (quit_button.get_x(), quit_button.get_y()))
    clock.tick(60)
    pygame.display.update()
  
pygame.quit()          
