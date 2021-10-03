import pygame 
from pygame.locals import *
#import random
pygame.init()  
white = (255, 255, 255)  
window = pygame.display.set_mode((400, 400))  
pygame.display.set_caption('Game Testing')  
#load images
image = pygame.image.load('resources/test.png')  
  
# infinite loop  
run = True 
while run:  
     
    window.fill((255, 255, 255))
    window.blit(image, (0, 0)) 
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            run = False  
        pygame.display.update()     
pygame.quit()             
