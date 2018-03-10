#mahjong_main.py

import pygame, sys
from pygame.locals import*

pygame.init()

disSize_w, disSize_h = 1280, 720

TARGET_FPS = 30
clock = pygame.time.Clock()


mainSelect = ['start', 'continue', 'rule', 'exit']
mainSelectNum = 0



imgMain = pygame.image.load('img/mahjong_main.png')


startButton = Rect(((disSize_w//4)*3, disSize_h//2), (disSize_w//6, disSize_h//12))
continueButton = Rect(((disSize_w//4)*3, disSize_h//2 + (disSize_h//12 + disSize_h//32)), (disSize_w//6, disSize_h//12))
ruleButton = Rect(((disSize_w//4)*3, disSize_h//2 + (disSize_h//12 + disSize_h//32)*2), (disSize_w//6, disSize_h//12))
exitButton = Rect(((disSize_w//4)*3, disSize_h//2 + (disSize_h//12 + disSize_h//32)*3), (disSize_w//6, disSize_h//12))

buttonColor = Color('light blue')
buttonOutline = Color('blue')

mouseInButton = False



textColor = Color('black')
textColor_s = Color('dark gray')

buttonFont = pygame.font.Font('font/HoonWhitecatR.ttf', 60)
buttonFont_s = pygame.font.Font('font/HoonWhitecatR.ttf', 52)

textStart = buttonFont.render('새 게임', True, textColor)
textStart_s = buttonFont.render('새 게임', True, textColor_s)
textContinue = buttonFont.render('이어하기', True, textColor)
textContinue_s = buttonFont.render('이어하기', True, textColor_s)
textRule = buttonFont_s.render('룰', True, textColor)
textRule_s = buttonFont_s.render('룰', True, textColor_s)
textExit = buttonFont.render('종료', True, textColor)
textExit_s = buttonFont.render('종료', True, textColor_s)


#메인화면 출력
def ScreenUpdate(SCREEN):
    SCREEN.blit(pygame.transform.scale(imgMain, (disSize_w, disSize_h)), (0, 0))

    pygame.draw.rect(SCREEN, buttonOutline, startButton.inflate(6, 6))
    pygame.draw.rect(SCREEN, buttonColor, startButton)
    SCREEN.blit(textStart, (startButton.x + 32, startButton.y))

    pygame.draw.rect(SCREEN, buttonOutline, continueButton.inflate(6, 6))
    pygame.draw.rect(SCREEN, buttonColor, continueButton)
    SCREEN.blit(textContinue, (continueButton.x + 32, continueButton.y + 2))

    pygame.draw.rect(SCREEN, buttonOutline, ruleButton.inflate(6, 6))
    pygame.draw.rect(SCREEN, buttonColor, ruleButton)
    SCREEN.blit(textRule, (ruleButton.x + 88, ruleButton.y + 4))

    pygame.draw.rect(SCREEN, buttonOutline, exitButton.inflate(6, 6))
    pygame.draw.rect(SCREEN, buttonColor, exitButton)
    SCREEN.blit(textExit, (exitButton.x + 76, exitButton.y + 2))
    
    if mainSelect[mainSelectNum] == 'start':
        SCREEN.blit(textStart_s, (startButton.x + 32, startButton.y))
    elif mainSelect[mainSelectNum] == 'continue':
        SCREEN.blit(textContinue_s, (continueButton.x + 32, continueButton.y + 2))
    elif mainSelect[mainSelectNum] == 'rule':
        SCREEN.blit(textRule_s, (ruleButton.x + 88, ruleButton.y + 4))
    elif mainSelect[mainSelectNum] == 'exit':
        SCREEN.blit(textExit_s, (exitButton.x + 76, exitButton.y + 2))

    pygame.display.flip()
    clock.tick(TARGET_FPS)


#입력
def MenuSelect():
    global mainSelect, mainSelectNum, mouseInButton
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if mainSelectNum > 0:
                    mainSelectNum -= 1
            if event.key == K_DOWN:
                if mainSelectNum < len(mainSelect)-1:
                    mainSelectNum += 1
            if event.key == K_RETURN:
                return mainSelect[mainSelectNum]
        if pygame.mouse.get_focused():
            mX, mY = pygame.mouse.get_pos()
            if startButton.collidepoint(mX, mY):
                mainSelectNum = 0
                mouseInButton = True
            elif continueButton.collidepoint(mX, mY):
                mainSelectNum = 1
                mouseInButton = True
            elif ruleButton.collidepoint(mX, mY):
                mainSelectNum = 2
                mouseInButton = True
            elif exitButton.collidepoint(mX, mY):
                mainSelectNum = 3
                mouseInButton = True
            if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                return mainSelect[mainSelectNum]
            mouseInButton = False
    return ''


