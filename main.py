import pygame
from pygame import rect 
from pygame.locals import *

from resources.LabelText import LabelText
#import random
pygame.init()  
white = (255, 255, 255)  
black = (0, 0, 0)  
window = pygame.display.set_mode((400, 400))  
pygame.display.set_caption('Game Testing')  
#load images
#image = pygame.image.load('resources/test.png')  

corbel_font = pygame.font.SysFont('Corbel',35) 
  
start_button = LabelText("Start", corbel_font, black, window.get_width() / 2, window.get_height() / 2 - 50 )
quit_button = LabelText("Quit", corbel_font, black, window.get_width() / 2, start_button.get_y() + start_button.get_height() )
# infinite loop  
run = True 
while run:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False  
        if event.type == pygame.MOUSEBUTTONDOWN:
            cursor = pygame.mouse.get_pos()
            if start_button.collision(cursor):
                pass
            elif quit_button.collision(cursor):
                run = False

    pygame.display.update()  
    window.fill((255, 255, 255))
    window.blit(start_button.surface(), (start_button.get_x(), start_button.get_y()))
    window.blit(quit_button.surface(), (quit_button.get_x(), quit_button.get_y()))
   
pygame.quit()          

