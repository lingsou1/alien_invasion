import pygame



'''管理飞船的类'''
class Ship:

    def __init__(self,ai_game):
        '''初始化飞船并设置其初始的位置'''
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #设置移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #将每个飞船都放在屏幕底部的中央
        self.rect.midbottom = self.screen_rect.midbottom



    def update(self):
        '''根据移动标志来调整飞船的位置'''
        #更新飞船而不是rect对象的X值
        #实现了飞船不跑出屏幕
        if self.moving_right and (self.rect.right < self.screen_rect.right) :
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0 :
            self.x -= self.settings.ship_speed

        if self.moving_up and self.rect.y > 0 :
            self.y -= self.settings.ship_speed

        if self.moving_down and (self.rect.y < 800) :
            self.y += self.settings.ship_speed

        #根据self.x 更新rect对象
        self.rect.x = self.x
        self.rect.y = self.y #游戏中的XY轴和屏幕不是相同的,游戏中的原点在左上角

    def blitme(self):
        '''指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)
