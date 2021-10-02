import pygame  
pygame.init()  
white = (255, 255, 255)  
window = pygame.display.set_mode((400, 400))  
  
pygame.display.set_caption('Gmame Testing')  
  
image = pygame.image.load(r'resources\test.png')  
  
# infinite loop   
while True:  
    window.fill((255, 255, 255))
    window.blit(image, (0, 0))  
  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()  
            quit()  
        pygame.display.update()   
