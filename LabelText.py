import pygame

class LabelText():
    def __init__(self, text, font, color, x, y):
        self.label = font.render(text, True, color)
        self.x = x
        self.y = y

    def get_height(self):
        return self.label.get_height()

    def get_width(self):
        return self.label.get_width()
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def surface(self):
        return self.label
    
    def collision(self, targetObject):
        if targetObject[0] >= self.x and targetObject[0] <= self.x + self.get_width() and targetObject[1] >= self.y and targetObject[1] <= self.y + self.get_height():
            return True
        return False
