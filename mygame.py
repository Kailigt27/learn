import sys
import pygame
from settings import Settings
from role1 import Role
class Alien_Invasion:
    def __init__(self):
        pygame.init()
        self.Setting=Settings()
        self.screen=pygame.display.set_mode((self.Setting.size_width,self.Setting.size_height))
        self.clock=pygame.time.Clock()
        self.role=Role(self)
        pygame.display.set_caption('Alien Invasion')
    def run_game(self):
        while True:
           self.__check_events__()
           self.__update_screen_()
           self.clock.tick(self.Setting.time)
           
    def __update_screen_(self):
        self.screen.fill(self.Setting.bg_color)
        self.role.blitme()
        pygame.display.flip()
            
    def __check_events__(self):
        for events in pygame.event.get():
            if events.type==pygame.QUIT:
                sys.exit()
if __name__=='__main__':
    ai=Alien_Invasion()
    ai.run_game()