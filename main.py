import pygame
from pygame import rect 
from pygame.locals import *

from LabelText import LabelText
from MenuButtons import MenuButtons
from Player import Player

#import random
pygame.init()  
#Variables
black = (0, 0, 0)
window_height = 400
window_width = 400
optionX = 0
optionY = 0
run = True 
game_screen = False
option_screen = False

window = pygame.display.set_mode((window_height, window_width))  
pygame.display.set_caption('Game Testing')  
game_screenBackground = pygame.image.load('resources/ground.jpg')
clock = pygame.time.Clock()
#bgm
game_bgm = pygame.mixer.music.set_volume(0.05)
pygame.mixer.music.load('resources/Town 3.mp3')
pygame.mixer.music.play()
corbel_font = pygame.font.SysFont('Corbel',35)
  
MainMenu = MenuButtons(window, black, run)
player = Player(50, 50, 5)

option_screenBackground = pygame.draw.rect(window, (255, 0, 0),(optionX, optionY, 0, 0))

# infinite loop  
while run:
    cursor = pygame.mouse.get_pos()
    for event in pygame.event.get():  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if MainMenu.handleQuit(cursor):
                run = False
            else:
                if MainMenu.handle_buttonClicked(cursor):
                    game_screen = True
                elif not MainMenu.handle_buttonClicked(cursor):
                    option_screen = True

    if not player.handleCollision(window.get_width(), window.get_height()):
        key = pygame.key.get_pressed()
        player.handleInput(key)
        if event.type == pygame.QUIT:  
            run = False  
    
    if game_screen == True:
        window.blit(game_screenBackground, game_screenBackground.get_rect())
        window.blit(player.get_player(), (player.getX(), player.getY()))
        
    elif option_screen == True:
        window.blit(option_screenBackground,option_screenBackground.get_rect())
        pygame.draw.rect(window, (255, 0, 0), (optionX, optionY, 50, 50))
    else:
       MainMenu.handle_menu(cursor)
    clock.tick(60)
    pygame.display.update()
  
pygame.quit()          

