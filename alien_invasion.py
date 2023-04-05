import pygame
import sys
from settings import Settings
from ship import Ship



'''管理游戏资源以及相关行为的类'''
class AlienInvasion:

    '''初始化游戏并创建游戏资源'''
    def __init__(self):

        pygame.init()
        #导入设置类
        self.settings = Settings()
        # self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_width))
        #将游戏设置为全屏画面(可选)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")
        #导入飞船类,不能放在 'self.settings = Settings()  #导入设置类'  这句之后,会报错
        self.ship = Ship(self)



    '''监视键盘及鼠标事件'''
    def _check_events(self):

        for event in pygame.event.get():
            # 退出游戏
            if event.type == pygame.QUIT:
                sys.exit()
            #检测按下的键位并进行相关的操作
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            #检测松开的键位并进行相关的操作
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)



    '''响应按键按下'''
    def _check_keydown_events(self,event):

        # 右移
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d :
            self.ship.moving_right = True
        # 左移
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a :
            self.ship.moving_left = True
        #上移
        elif event.key == pygame.K_UP or event.key == pygame.K_w :
            self.ship.moving_up = True
        #下移
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s :
            self.ship.moving_down = True
        # 当同时按下左移和右移键时,优先右移(运行失败)
        elif event.key == (pygame.K_LEFT & pygame.K_RIGHT):
            self.ship.moving_right = True
        #按Q退出
        elif event.key == pygame.K_q :
            sys.exit()



    ''' 响应按键松开'''
    def _check_keyup_events(self,event):

        # 停止右移
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.ship.moving_right = False
        # 停止左移
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.ship.moving_left = False
        #停止上移
        elif event.key == pygame.K_w or event.key == pygame.K_UP:
            self.ship.moving_up = False
        #停止下移
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.ship.moving_down = False


    '''更新屏幕的代码'''
    def _update_screen(self):

        # 每次循环时都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()



    '''开始游戏的主循环'''
    def run_game(self):
        while True:
            self.ship.blitme()
            self._check_events()    #检查事件
            self.ship.update()      #控制飞船的位移
            self._update_screen()   #更新屏幕





if __name__ == '__main__':
    #创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
