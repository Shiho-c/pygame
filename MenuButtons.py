from LabelText import LabelText
import pygame
class MenuButtons:
    def __init__(self, window, black, run):
        self.corbel_font = pygame.font.SysFont('Corbel',35)
        self.start_button = LabelText("Start", self.corbel_font, black, window.get_width() / 2, window.get_height() / 2 - 50 )
        self.option_button = LabelText("Option", self.corbel_font, black, window.get_width() / 2, self.start_button.get_y() + self.start_button.get_height() + 50 )
        self.quit_button = LabelText("Quit", self.corbel_font, black, window.get_width() / 2, self.option_button.get_y() + self.option_button.get_height() + 50 )
        self.menu_buttons = [self.start_button, self.option_button, self.quit_button]
        self.window = window
        self.background = (255, 255, 255)
        self.run = run
        
    def menu_blit(self):
        self.window.fill(self.background)
        for button in self.menu_buttons:
            self.window.blit(button.surface(), (button.get_x(), button.get_y()))

    def menu_color(self):
        for button in self.menu_buttons:
            button.change_color((0,0, 0))
    
    def handle_buttonClicked(self, cursor):
        if self.start_button.collision(cursor):
            print("glitch")
            self.background = (0, 0, 0)
            pygame.mixer.music.stop()
            print("Shit2")
            return True
        elif self.option_button.collision(cursor):
            option_screen = False
            return False

    def handle_menu(self, cursor):
        if self.start_button.collision(cursor):
            self.start_button.change_color((255,0, 0))
        elif self.quit_button.collision(cursor):
            self.quit_button.change_color((255,0, 0))
        elif self.option_button.collision(cursor):
            self.option_button.change_color((255,0, 0))
        else: 
            self.menu_color()
        self.menu_blit()
    
    def handleQuit(self, cursor):
        if self.quit_button.collision(cursor):
            pygame.mixer.music.stop()
            return True