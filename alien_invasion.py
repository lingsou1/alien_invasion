import pygame
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet



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
        #创建存储子弹的编组
        self.bullets = pygame.sprite.Group()



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
        #按下空格键开火
        elif event.key == pygame.K_SPACE :
            self._fire_bullet()



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



    '''开火的设置,按下空格键将会执行的操作'''
    def _fire_bullet(self):
        '''创建一颗子弹并将其加入编组'''
        if len(self.bullets) < self.settings.bullet_allowed :   #这句循环会控制子弹的数量在设置的数量
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        # 子弹的位置更新
        self.bullets.update()

        # 删除消失的子弹,否则会继续占用CPU的运算
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)





    '''更新屏幕的代码'''
    def _update_screen(self):

        # 每次循环时都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 让最近绘制的屏幕可见
        pygame.display.flip()



    '''开始游戏的主循环'''
    def run_game(self):
        while True:
            self._check_events()    #检查事件
            self.ship.update()      #控制飞船的位移
            self._update_bullets()  #更新子弹,一是删除过界的子弹,二是限制子弹数量
            self._update_screen()  # 更新屏幕





if __name__ == '__main__':
    #创建游戏实例并运行
    ai = AlienInvasion()
    ai.run_game()
