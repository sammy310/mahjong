#mahjong.py

import pygame, sys
from pygame.locals import*
import mahjong_main as mj_main
import mahjong_rule as mj_rule
import mahjong_game as mj_game



pygame.init()

disSize_w, disSize_h = 1280, 720
SCREEN = pygame.display.set_mode((disSize_w, disSize_h))

pygame.display.set_caption('Mahjong')



mainSelectVal = ''

while True:
    
    if mainSelectVal == '':
        mj_main.ScreenUpdate(SCREEN)
        mainSelectVal = mj_main.MenuSelect()
        
    elif mainSelectVal == 'start':
        mj_game.MahjongGame(SCREEN)
        mainSelectVal = ''
        
        
    elif mainSelectVal == 'continue':
        mj_game.ContinueGame(SCREEN)
        mainSelectVal = 'start'
        
    elif mainSelectVal == 'rule':
        mj_rule.PrintRule(SCREEN)
        mainSelectVal = ''
    elif mainSelectVal == 'exit':
        pygame.quit()
        sys.exit()


