import pygame
from pygame import rect 
from pygame.locals import *

from LabelText import LabelText
#import random
pygame.init()  
background = (255, 255, 255)  
black = (0, 0, 0)
window = pygame.display.set_mode((400, 400))  
pygame.display.set_caption('Game Testing')  
#load images
#image = pygame.image.load('resources/ocean.jpg')
clock = pygame.time.Clock()

corbel_font = pygame.font.SysFont('Corbel',35)
  
start_button = LabelText("Start", corbel_font, black, window.get_width() / 2, window.get_height() / 2 - 50 )
quit_button = LabelText("Quit", corbel_font, black, window.get_width() / 2, start_button.get_y() + start_button.get_height() )
player = rect.Rect((50, 40, 15, 15))
game_screen = False
# infinite loop  
run = True 
while run:
    for event in pygame.event.get():  
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
           player.move_ip(-1, 0)
        if key[pygame.K_RIGHT]:
           player.move_ip(1, 0)
        if key[pygame.K_UP]:
           player.move_ip(0, -1)
        if key[pygame.K_DOWN]:
           player.move_ip(0, 1)
        if event.type == pygame.QUIT:  
            run = False  
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor = pygame.mouse.get_pos()
            if start_button.collision(cursor):
                background = (0, 0, 0)
                game_screen = True
            elif quit_button.collision(cursor):
                run = False

    window.fill(background)
    window.blit(start_button.surface(), (start_button.get_x(), start_button.get_y()))
    window.blit(quit_button.surface(), (quit_button.get_x(), quit_button.get_y()))
    if game_screen:
        pygame.draw.rect(window, (0, 0, 128), player)
    clock.tick(60)
    pygame.display.update()
  
pygame.quit()          
#push 
