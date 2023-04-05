'''存储游戏中所有设置的类'''
class Settings :

    '''初始化游戏的设置'''
    def __init__(self):
        #屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (111,222,255)
        #飞船速度设置
        self.ship_speed = 0.5
        #子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
