import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理飞船发射的子弹的类'''
    def __init__(self,ai_game):
        '''在飞船当前位置创建一个子弹对象'''