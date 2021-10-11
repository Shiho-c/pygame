import pygame
class Player():
    def __init__(self, x, y, speed):
        self.player = pygame.image.load('resources/player.png')
        self.player =  pygame.transform.scale(self.player, (x, y))
        self.moveMentSpeed = speed
        self.x = x
        self.y = y
    
    def get_width(self):
        return self.player.get_width()
    
    def get_height(self):
        return self.player.get_height()
    
    def get_player(self):
        return self.player
    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def handleInput(self, key):
        if key[pygame.K_LEFT]:
            self.x -= self.moveMentSpeed
        if key[pygame.K_RIGHT]:
            self.x += self.moveMentSpeed
        if key[pygame.K_UP]:
            self.y -= self.moveMentSpeed
        if key[pygame.K_DOWN]:
            self.y += self.moveMentSpeed
    
    def handleCollision(self, window_width, window_height):
        if self.x + self.player.get_width() >= window_width:
            self.x -= self.moveMentSpeed
        elif self.x < 1:
            self.x += self.moveMentSpeed
        elif self.y + self.player.get_height() >= window_height:
            self.y -= self.moveMentSpeed
        elif self.y < 1:
            self.y += self.moveMentSpeed
        else: 
            return False
        return True


