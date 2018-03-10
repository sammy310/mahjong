#mahjong_rule.py

import pygame, sys
from pygame.locals import*

pygame.init()

disSize_w, disSize_h = 1280, 720

TARGET_FPS = 30
clock = pygame.time.Clock()


textColor = Color('black')
buttonColor = Color('light blue')

textFont = pygame.font.Font('font/HoonWhitecatR.ttf', 60)


textRulePos = (disSize_w // 4, 50)
textRule_1 = textFont.render('헤아림 역만 : 있음', True, textColor)
textRule_2 = textFont.render('형식 텐파이 : 있음', True, textColor)
textRule_3 = textFont.render('더블 론 : 있음', True, textColor)
textRule_4 = textFont.render('트리플 론 : 유국', True, textColor)
textRule_5 = textFont.render('사풍연타 : 유국', True, textColor)
textRule_6 = textFont.render('4인리치 : 유국', True, textColor)
textRule_7 = textFont.render('적도라 : 5만 - 1, 5통 - 2, 5삭 - 1', True, textColor)

textEnter = textFont.render('확인', True, textColor)
enterButton = Rect(disSize_w // 2 - 55, disSize_h // 8 * 7 - 80, 110, 70)


mouseInButton = False

def PrintRule(SCREEN):
    global mouseInButton
    
    isInputDone = False
    while True:
        if isInputDone == True:
            pygame.time.wait(100)
            return


        ##########Key Input##########
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                    
            ##########mouse##########
            if pygame.mouse.get_focused():
                mX, mY = pygame.mouse.get_pos()
                        
                if enterButton.collidepoint(mX, mY):
                    mouseInButton = True

                if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                    isInputDone = True
                mouseInButton = False
                    
            ##########keyboard##########
            if not hasattr(event, 'key'):
                continue
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    isInputDone = True



        SCREEN.fill((150, 150, 150))

        for i in range(1, 8):
            SCREEN.blit(eval('textRule_' + str(i)), (textRulePos[0], textRulePos[1] + (65 * (i - 1))))
        
        pygame.draw.rect(SCREEN, buttonColor, enterButton)
        SCREEN.blit(textEnter, (enterButton.x + 15, enterButton.y + 8))



        pygame.display.flip()
        clock.tick(TARGET_FPS)
