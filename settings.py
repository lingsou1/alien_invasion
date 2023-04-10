'''存储游戏中所有设置的类'''
class Settings :

    '''初始化游戏的设置'''
    def __init__(self):
        #屏幕设置
        self.screen_width = 800             #屏幕宽度
        self.screen_height = 600            #屏幕高度
        self.bg_color = (111,222,255)       #屏幕背景颜色

        #飞船速度设置
        self.ship_speed = 0.5       #飞船的速度

        #子弹设置
        self.bullet_speed = 1.0     #子弹速度
        self.bullet_width = 3       #子弹宽
        self.bullet_height = 15     #子弹高
        self.bullet_color = (60,60,60)     #子弹颜色
        self.bullet_allowed = 3            #最大子弹数量
