# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 21:51:58 2025

@author: Asane
"""

import pygame
class Role:
    def __init__(self,ai_game):
        '''
        向函数中输入整个游戏所用的窗口（屏幕）
        设置其初始位置
        '''
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()
        '''
        导入图片素材,并获取其外接矩形
        '''
        self.image=pygame.image.load('material/logo.bmp')
        self.image_rect=self.image.get_rect()
        self.image_rect.midbottom=self.screen_rect.midbottom
    def blitme(self):
        self.screen.blit(self.image,self.image_rect)
        