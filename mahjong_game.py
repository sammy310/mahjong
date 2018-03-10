#mahjong_game.py

import pygame, sys
from pygame.locals import*
import os.path
import random, time

disSize_w, disSize_h = 1280, 720

pygame.init()

TARGET_FPS = 30
clock = pygame.time.Clock()



handList = [0]*13
handSelect = 0

actionList = []
actionSelect = 0

inputType = 0


gameInfo = {'ba':'east', 'kyoku':'east1', 'renchan':0, 'turn':'', 'kan':0, 'suukantsu':False, 'redDora':True, 'kuitan':True, 'daisharin':True, 'count':0, 'rest':70}
p1Info = {'score':25000, 'wind':'', 'shanten':8, 'riichi':0, 'doubleriichi':0, 'ippatsu':0, 'rinshan':False, 'hou':True, 'chankan':False, 'huro':[], 'canHuro':[], 'canAction':[]}
p2Info = {'score':25000, 'wind':'', 'shanten':8, 'riichi':0, 'doubleriichi':0, 'ippatsu':0, 'rinshan':False, 'hou':True, 'chankan':False, 'huro':[], 'canHuro':[], 'canAction':[]}
p3Info = {'score':25000, 'wind':'', 'shanten':8, 'riichi':0, 'doubleriichi':0, 'ippatsu':0, 'rinshan':False, 'hou':True, 'chankan':False, 'huro':[], 'canHuro':[], 'canAction':[]}
p4Info = {'score':25000, 'wind':'', 'shanten':8, 'riichi':0, 'doubleriichi':0, 'ippatsu':0, 'rinshan':False, 'hou':True, 'chankan':False, 'huro':[], 'canHuro':[], 'canAction':[]}

cardList = []

p1Hand = []
p2Hand = []
p3Hand = []
p4Hand = []

p1Discard = []
p2Discard = []
p3Discard = []
p4Discard = []


gameStart = False
gameRestart = False
playerTurnPre = False

turnEnd = False

p1Select = ''
p2Select = ''
p3Select = ''
p4Select = ''




############################## image ##############################

p1 = pygame.image.load('img/mahjong_icons/pin/pin1.png')
p2 = pygame.image.load('img/mahjong_icons/pin/pin2.png')
p3 = pygame.image.load('img/mahjong_icons/pin/pin3.png')
p4 = pygame.image.load('img/mahjong_icons/pin/pin4.png')
p5 = pygame.image.load('img/mahjong_icons/pin/pin5.png')
p6 = pygame.image.load('img/mahjong_icons/pin/pin6.png')
p7 = pygame.image.load('img/mahjong_icons/pin/pin7.png')
p8 = pygame.image.load('img/mahjong_icons/pin/pin8.png')
p9 = pygame.image.load('img/mahjong_icons/pin/pin9.png')

s1 = pygame.image.load('img/mahjong_icons/bamboo/bamboo1.png')
s2 = pygame.image.load('img/mahjong_icons/bamboo/bamboo2.png')
s3 = pygame.image.load('img/mahjong_icons/bamboo/bamboo3.png')
s4 = pygame.image.load('img/mahjong_icons/bamboo/bamboo4.png')
s5 = pygame.image.load('img/mahjong_icons/bamboo/bamboo5.png')
s6 = pygame.image.load('img/mahjong_icons/bamboo/bamboo6.png')
s7 = pygame.image.load('img/mahjong_icons/bamboo/bamboo7.png')
s8 = pygame.image.load('img/mahjong_icons/bamboo/bamboo8.png')
s9 = pygame.image.load('img/mahjong_icons/bamboo/bamboo9.png')

m1 = pygame.image.load('img/mahjong_icons/man/man1.png')
m2 = pygame.image.load('img/mahjong_icons/man/man2.png')
m3 = pygame.image.load('img/mahjong_icons/man/man3.png')
m4 = pygame.image.load('img/mahjong_icons/man/man4.png')
m5 = pygame.image.load('img/mahjong_icons/man/man5.png')
m6 = pygame.image.load('img/mahjong_icons/man/man6.png')
m7 = pygame.image.load('img/mahjong_icons/man/man7.png')
m8 = pygame.image.load('img/mahjong_icons/man/man8.png')
m9 = pygame.image.load('img/mahjong_icons/man/man9.png')

p5r = pygame.image.load('img/mahjong_icons/red/red_pin5.png')
s5r = pygame.image.load('img/mahjong_icons/red/red_bamboo5.png')
m5r = pygame.image.load('img/mahjong_icons/red/red_man5.png')

chun = pygame.image.load('img/mahjong_icons/dragons/chun.png')
green = pygame.image.load('img/mahjong_icons/dragons/green.png')
haku = pygame.image.load('img/mahjong_icons/dragons/haku.png')

east = pygame.image.load('img/mahjong_icons/winds/east.png')
south = pygame.image.load('img/mahjong_icons/winds/south.png')
west = pygame.image.load('img/mahjong_icons/winds/west.png')
north = pygame.image.load('img/mahjong_icons/winds/north.png')

back = pygame.image.load('img/mahjong_icons/back.png')
up = pygame.image.load('img/mahjong_icons/up.png')

#################################################################

############################## TEXT ##############################

textColor = Color('black')
textColor_s = Color('dark gray')

textFont = pygame.font.Font('font/NanumPen.ttf', 40)
textFont_small = pygame.font.Font('font/NanumPen.ttf', 30)
textFont_big = pygame.font.Font('font/NanumPen.ttf', 60)

text0 = textFont.render('0', True, textColor)
text1 = textFont.render('1', True, textColor)
text2 = textFont.render('2', True, textColor)
text3 = textFont.render('3', True, textColor)
text4 = textFont.render('4', True, textColor)
text5 = textFont.render('5', True, textColor)
text6 = textFont.render('6', True, textColor)
text7 = textFont.render('7', True, textColor)
text8 = textFont.render('8', True, textColor)
text9 = textFont.render('9', True, textColor)
text10 = textFont.render('0', True, textColor)
text11 = textFont.render('-', True, textColor)
text12 = textFont.render('=', True, textColor)
text13 = textFont.render('\\', True, textColor)
text14 = textFont.render('BS', True, textColor)

textF1 = textFont.render('F1', True, textColor)
textF2 = textFont.render('F2', True, textColor)
textF3 = textFont.render('F3', True, textColor)
textF4 = textFont.render('F4', True, textColor)
textF5 = textFont.render('F5', True, textColor)
textF6 = textFont.render('F6', True, textColor)
textF7 = textFont.render('F7', True, textColor)
textF8 = textFont.render('F8', True, textColor)
textF9 = textFont.render('F9', True, textColor)

textBa = textFont_big.render('국', True, textColor)
textBa_1 = textFont_big.render('동풍전', True, textColor)
textBa_1_s = textFont_big.render('동풍전', True, Color('red'))
textBa_2 = textFont_big.render('반장전', True, textColor)
textBa_2_s = textFont_big.render('반장전', True, Color('red'))
textBa_3 = textFont_big.render('일장전', True, textColor)
textBa_3_s = textFont_big.render('일장전', True, Color('red'))
textRedDora = textFont_big.render('적도라', True, textColor)
textKuitan = textFont_big.render('쿠이탕', True, textColor)
textDaisharin = textFont_big.render('대차륜', True, textColor)
text_Yes = textFont_big.render('있음', True, textColor)
text_Yes_s = textFont_big.render('있음', True, Color('red'))
text_No = textFont_big.render('없음', True, textColor)
text_No_s = textFont_big.render('없음', True, Color('red'))

textEnter = textFont.render('확인', True, textColor)
textEnter_s = textFont.render('확인', True, textColor_s)

textChi = textFont.render('치', True, textColor)
textChi_s = textFont.render('치', True, textColor_s)
textPon = textFont.render('퐁', True, textColor)
textPon_s = textFont.render('퐁', True, textColor_s)
textKan = textFont.render('캉', True, textColor)
textKan_s = textFont.render('캉', True, textColor_s)
textRon = textFont.render('론', True, Color('red'))
textRon_s = textFont.render('론', True, Color('dark red'))
textTsumo = textFont.render('쯔모', True, Color('red'))
textTsumo_s = textFont.render('쯔모', True, Color('dark red'))
textNo = textFont.render('넘어가기', True, textColor)
textNo_s = textFont.render('넘어가기', True, textColor_s)
textRiichi = textFont.render('리치', True, textColor)
textRiichi_s = textFont.render('리치', True, textColor_s)

text0Shan = textFont.render('텐파이', True, Color('red'))
text1Shan = textFont.render('이샹텐', True, textColor)
text2Shan = textFont.render('량샹텐', True, textColor)
text3Shan = textFont.render('산샹텐', True, textColor)
text4Shan = textFont.render('스샹텐', True, textColor)
text5Shan = textFont.render('우샹텐', True, textColor)
text6Shan = textFont.render('로샹텐', True, textColor)
text7Shan = textFont.render('치샹텐', True, textColor)
text8Shan = textFont.render('파샹텐', True, textColor)

text_riichi = textFont.render('리치', True, textColor)
text_doubleriichi = textFont.render('더블리치', True, textColor)
text_ippatsu = textFont.render('일발', True, textColor)
text_tsumo = textFont.render('쯔모', True, textColor)
text_pinfu = textFont.render('핑후', True, textColor)
text_chiitoitsu = textFont.render('치또이츠', True, textColor)
text_iipeikou = textFont.render('이페코', True, textColor)
text_ryanpeikou = textFont.render('량페코', True, textColor)
text_tanyao = textFont.render('탕야오', True, textColor)
text_yakuhai = textFont.render('역패', True, textColor)
text_rinshankaihou = textFont.render('영상개화', True, textColor)
text_chankan = textFont.render('챵깡', True, textColor)
text_haiteiraoyue = textFont.render('해저로월', True, textColor)
text_houteiraoyui = textFont.render('하저로어', True, textColor)
text_sanshokudoujun = textFont.render('삼색동순', True, textColor)
text_sanshokudoukou = textFont.render('삼색동각', True, textColor)
text_ikkitsukan = textFont.render('일기통관', True, textColor)
text_chanta = textFont.render('챤타', True, textColor)
text_junchan = textFont.render('준짱', True, textColor)
text_toitoi = textFont.render('또이또이', True, textColor)
text_sanankou = textFont.render('산앙코', True, textColor)
text_suuankou = textFont.render('스앙코', True, textColor)
text_honroutou = textFont.render('혼노두', True, textColor)
text_chinroutou = textFont.render('청노두', True, textColor)
text_sankantsu = textFont.render('산깡쯔', True, textColor)
text_suukantsu = textFont.render('스깡쯔', True, textColor)
text_shousangen = textFont.render('소삼원', True, textColor)
text_daisangen = textFont.render('대삼원', True, textColor)
text_honiisou = textFont.render('혼일색', True, textColor)
text_chiniisou = textFont.render('청일색', True, textColor)
text_kokushimusou = textFont.render('국사무쌍', True, textColor)
text_chuurenpoutou = textFont.render('구련보등', True, textColor)
text_tsuuiisou = textFont.render('자일색', True, textColor)
text_ryuuiisou = textFont.render('녹일색', True, textColor)
text_daisuushii = textFont.render('대사희', True, textColor)
text_shousuushii = textFont.render('소사희', True, textColor)
text_daisharin = textFont.render('대차륜', True, textColor)
text_tenhou = textFont.render('천화', True, textColor)
text_chiihou = textFont.render('지화', True, textColor)
text_renhou = textFont.render('인화', True, textColor)
text_dora = textFont.render('도라', True, textColor)

text_east = textFont.render('동', True, Color('red'))
text_south = textFont.render('남', True, textColor)
text_west = textFont.render('서', True, textColor)
text_north = textFont.render('북', True, textColor)

text_east_s = textFont.render('동', True, textColor)
text_kyoku = textFont.render('국', True, textColor)
text_allLast = textFont.render('오라스', True, Color('red'))
text_renchan = textFont.render('본장', True, textColor)

text_fan = textFont.render('판', True, textColor)
text_fu = textFont.render('부', True, textColor)

text_mangan = textFont_big.render('만관', True, textColor)
text_haneman = textFont_big.render('하네만', True, textColor)
text_baiman = textFont_big.render('배만', True, textColor)
text_sanbaiman = textFont_big.render('삼배만', True, textColor)
text_kazoeyakuman = textFont_big.render('카조에 역만', True, Color('red'))
text_yakuman = textFont_big.render('역만', True, Color('red'))
text_doubleyakuman = textFont_big.render('더블 역만', True, Color('red'))
text_tripleyakuman = textFont_big.render('트리플 역만', True, Color('red'))

text_Ten = textFont.render('텐파이', True, Color('blue'))
text_NoTen = textFont.render('노텐', True, Color('red'))

text_kyukyoku = textFont_big.render('유국', True, Color('red'))
text_gameEnd = textFont_big.render('게임 종료', True, Color('red'))

################################ Card Size ################################

p1Degree = 0
p2Degree = 90
p3Degree = 180
p4Degree = 270


cardSize = Rect(23, 0, 82, 128)
#cardSize_s = Rect(12, 0, 41, 64) #아마 안쓸듯

cardSize_p1 = Rect(12, 9, 41, 55)
cardSize_p2 = Rect(9, 11, 55, 41)
cardSize_p3 = Rect(11, 0, 41, 55)
cardSize_p4 = Rect(0, 12, 55, 41)

cardSize_up = Rect(0, 0, 32, 26)
cardSize_up_s = Rect(0, 0, 26, 32)

cardSize_p1_huro = Rect((cardSize.x / 4) * 3 + 1, 13, (cardSize.w / 4) * 3, (cardSize.h / 4) * 3 - 13)
cardSize_p1_huro_s = Rect(13, (cardSize.x / 4) * 3, (cardSize.h / 4) * 3 - 13, (cardSize.w / 4) * 3)
#cardSize_p2_huro = Rect(9, 11, 55, 41)
#cardSize_p3_huro = Rect(11, 0, 41, 55)
#cardSize_p4_huro = Rect(0, 12, 55, 41)

middleChangeSize = (96, 96)
smallChangeSize = (64, 64)

cutSize = 10

############################# Tile Pos ###############################

p1HandPos = (44, disSize_h - 127)
p2HandPos = (disSize_w // 8 * 7, disSize_h // 8 * 5 + 42)
p3HandPos = (870, 40)
p4HandPos = (disSize_w // 8, 60)

p1HuroPos = (disSize_w, disSize_h - (cardSize_p1_huro.h - 1))
p2HuroPos = (disSize_w - (cardSize_p2.w - 1), 0)
p3HuroPos = (cardSize_p1.w * 2, 0)
p4HuroPos = (0, p1HandPos[1] - 50)

p1DisPos = (disSize_w//2 - cardSize_p1.w*(cutSize//2), 402)
p2DisPos = (706 + 165, disSize_h//2 + cardSize_p2.h*((cutSize//2)-1) - 41)
p3DisPos = (disSize_w//2 + cardSize_p3.w*((cutSize//2)-1), 270 - 110)
p4DisPos = (574 - 165 - 55, disSize_h//2 - cardSize_p2.h*(cutSize//2) - 41)

############################## Button ##############################

mouseInButton = False
mouseInButton_a = False

cardPos1 = Rect(44, disSize_h - 127, 82, 128)
cardPos2 = Rect(126, disSize_h - 127, 82, 128)
cardPos3 = Rect(208, disSize_h - 127, 82, 128)
cardPos4 = Rect(290, disSize_h - 127, 82, 128)
cardPos5 = Rect(372, disSize_h - 127, 82, 128)
cardPos6 = Rect(454, disSize_h - 127, 82, 128)
cardPos7 = Rect(536, disSize_h - 127, 82, 128)
cardPos8 = Rect(618, disSize_h - 127, 82, 128)
cardPos9 = Rect(700, disSize_h - 127, 82, 128)
cardPos10 = Rect(782, disSize_h - 127, 82, 128)
cardPos11 = Rect(864, disSize_h - 127, 82, 128)
cardPos12 = Rect(946, disSize_h - 127, 82, 128)
cardPos13 = Rect(1028, disSize_h - 127, 82, 128)
cardPos14 = Rect(1154, disSize_h - 127, 82, 128)


buttonColor = Color('light blue')
buttonColor_s = Color('white')

#치
f5Button = Rect(470, disSize_h - 180, 120, 40)
f5Button_s = Rect(465, disSize_h - 185, 130, 50)
#퐁
f6Button = Rect(600, disSize_h - 180, 120, 40)
f6Button_s = Rect(595, disSize_h - 185, 130, 50)
#깡
f7Button = Rect(730, disSize_h - 180, 120, 40)
f7Button_s = Rect(725, disSize_h - 185, 130, 50)
#론 + 쯔모
f8Button = Rect(860, disSize_h - 180, 120, 40)
f8Button_s = Rect(855, disSize_h - 185, 130, 50)
#넘어가기 + 리치
f9Button = Rect(990, disSize_h - 180, 120, 40)
f9Button_s = Rect(985, disSize_h - 185, 130, 50)


enterButton = Rect(disSize_w // 2 - 30, disSize_h // 8 * 7 - 70, 60, 50)
enterButton_s = Rect(disSize_w // 2 - 35, disSize_h // 8 * 7 - 75, 70, 60)


baButton = Rect(disSize_w // 4 - 100, 100, 200, 80)
baButton_1 = Rect(baButton.x + 300, baButton.y, baButton.w, baButton.h)
baButton_1_s = Rect(baButton.x + 295, baButton.y - 5, baButton.w + 10, baButton.h + 10)
baButton_2 = Rect(baButton.x + 530, baButton.y, baButton.w, baButton.h)
baButton_2_s = Rect(baButton.x + 525, baButton.y - 5, baButton.w + 10, baButton.h + 10)
baButton_3 = Rect(baButton.x + 760, baButton.y, baButton.w, baButton.h)
baButton_3_s = Rect(baButton.x + 755, baButton.y - 5, baButton.w + 10, baButton.h + 10)

redDoraButton = Rect(baButton.x, baButton.y + 100, baButton.w, baButton.h)
redDoraButton_yes = Rect(baButton_1.x, redDoraButton.y, baButton.w, baButton.h)
redDoraButton_yes_s = Rect(baButton_1.x - 5, redDoraButton.y - 5, baButton.w + 10, baButton.h + 10)
redDoraButton_no = Rect(baButton_2.x, redDoraButton.y, baButton.w, baButton.h)
redDoraButton_no_s = Rect(baButton_2.x - 5, redDoraButton.y - 5, baButton.w + 10, baButton.h + 10)

kuitanButton = Rect(baButton.x, redDoraButton.y + 100, baButton.w, baButton.h)
kuitanButton_yes = Rect(baButton_1.x, kuitanButton.y, baButton.w, baButton.h)
kuitanButton_yes_s = Rect(baButton_1.x - 5, kuitanButton.y - 5, baButton.w + 10, baButton.h + 10)
kuitanButton_no = Rect(baButton_2.x, kuitanButton.y, baButton.w, baButton.h)
kuitanButton_no_s = Rect(baButton_2.x - 5, kuitanButton.y - 5, baButton.w + 10, baButton.h + 10)

daisharinButton = Rect(baButton.x, kuitanButton.y + 100, baButton.w, baButton.h)
daisharinButton_yes = Rect(baButton_1.x, daisharinButton.y, baButton.w, baButton.h)
daisharinButton_yes_s = Rect(baButton_1.x - 5, daisharinButton.y - 5, baButton.w + 10, baButton.h + 10)
daisharinButton_no = Rect(baButton_2.x, daisharinButton.y, baButton.w, baButton.h)
daisharinButton_no_s = Rect(baButton_2.x - 5, daisharinButton.y - 5, baButton.w + 10, baButton.h + 10)

############################## END ##############################




############################## MAIN ##############################

def MahjongGame(SCREEN):
    global gameStart, gameRestart, playerTurnPre
    global handList
    global p1Hand

    while True:
        ##########Prepare##########
        if gameStart == False:
            gameStart = True
            ListInit('clear')
            CardInit()
            GameInfoInit()
            GameRuleSelect(SCREEN)
            TurnDecision()
            CardDivide()
            pygame.time.wait(200)

        if gameRestart == True:
            gameRestart = False
            GameRestartInit()
            ListInit('clear')
            CardInit()
            CardDivide()
            pygame.time.wait(200)
            


        GameScreen(SCREEN)
    

        if playTurn(SCREEN, gameInfo['turn']) == 'exit':
            return

    
        if IsGameEnd(SCREEN) == True:
            return

        
        pygame.display.flip()
        clock.tick(TARGET_FPS)

    

    
def ContinueGame(SCREEN):
    global gameStart
    
    if gameStart == False:
        if os.path.isfile('save.mj'):
            if LoadData() != False:
                gameStart = True
                p1Info['shanten'] = HandCheck(p1Hand, p1Info, 'shanten')
                CanAction('p1')

    return

############################################################



############################## Prepare ##############################

def GameInfoInit():
    global gameInfo, p1Info, p2Info, p3Info, p4Info

    gameInfo = {'ba':'east', 'kyoku':'east1', 'renchan':0, 'turn':'', 'kan':0, 'suukantsu':False, 'redDora':True, 'kuitan':True, 'daisharin':True, 'count':0, 'rest':70}
    p1Info = {'score':25000, 'wind':'', 'shanten':8, 'riichi':0, 'doubleriichi':0, 'ippatsu':0, 'rinshan':False, 'hou':True, 'chankan':False, 'huro':[], 'canHuro':[], 'canAction':[]}
    p2Info = {'score':25000, 'wind':'', 'shanten':8, 'riichi':0, 'doubleriichi':0, 'ippatsu':0, 'rinshan':False, 'hou':True, 'chankan':False, 'huro':[], 'canHuro':[], 'canAction':[]}
    p3Info = {'score':25000, 'wind':'', 'shanten':8, 'riichi':0, 'doubleriichi':0, 'ippatsu':0, 'rinshan':False, 'hou':True, 'chankan':False, 'huro':[], 'canHuro':[], 'canAction':[]}
    p4Info = {'score':25000, 'wind':'', 'shanten':8, 'riichi':0, 'doubleriichi':0, 'ippatsu':0, 'rinshan':False, 'hou':True, 'chankan':False, 'huro':[], 'canHuro':[], 'canAction':[]}



def CardInit():
    global cardList
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Discard, p2Discard, p3Discard, p4Discard
    
    cardList = ['p1', 'p2', 'p3', 'p4', 'p6', 'p7', 'p8', 'p9', 's1', 's2', 's3', 's4', 's6', 's7', 's8', 's9', 'm1', 'm2', 'm3', 'm4', 'm6', 'm7', 'm8', 'm9', 'chun', 'green', 'haku', 'east', 'south', 'west', 'north']*4
    p1Hand = []
    p2Hand = []
    p3Hand = []
    p4Hand = []
    p1Discard = []
    p2Discard = []
    p3Discard = []
    p4Discard = []




def CardDivide():
    global gameInfo, cardList
    global p1Hand, p2Hand, p3Hand, p4Hand
    
    if gameInfo['redDora']:
        cardList += ['p5', 'p5', 'p5r', 'p5r', 's5', 's5', 's5', 's5r', 'm5', 'm5', 'm5', 'm5r']
    else:
        cardList += ['p5', 's5', 'm5']*4


    random.shuffle(cardList)
    sequenceNum = int(gameInfo['turn'][1])
    while True:
        if sequenceNum == 1:
            if len(p1Hand) < 12:
                for i in range(4):
                    p1Hand.append(cardList.pop(0))
            else:
                p1Hand.append(cardList.pop(0))
        elif sequenceNum == 2:
            if len(p2Hand) < 12:
                for i in range(4):
                    p2Hand.append(cardList.pop(0))
            else:
                p2Hand.append(cardList.pop(0))
        elif sequenceNum == 3:
            if len(p3Hand) < 12:
                for i in range(4):
                    p3Hand.append(cardList.pop(0))
            else:
                p3Hand.append(cardList.pop(0))
        elif sequenceNum == 4:
            if len(p4Hand) < 12:
                for i in range(4):
                    p4Hand.append(cardList.pop(0))
            else:
                p4Hand.append(cardList.pop(0))
                
        if len(p1Hand) == len(p2Hand) == len(p3Hand) == len(p4Hand) == 13:
            break

        sequenceNum += 1
        if sequenceNum == 5:
            sequenceNum = 1

    p1Hand = CardSort(p1Hand).copy()
    p2Hand = CardSort(p2Hand).copy()
    p3Hand = CardSort(p3Hand).copy()
    p4Hand = CardSort(p4Hand).copy()




def CardSort(playerHand):
    
    sortedList = []
    playerHand.sort()
    for i in range(len(playerHand)):
        if 'm1' <= playerHand[i] and playerHand[i] <='m9':
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 'p1' <= playerHand[i] and playerHand[i] <='p9':
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 's1' <= playerHand[i] and playerHand[i] <='s9':
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 'east' == playerHand[i]:
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 'south' == playerHand[i]:
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 'west' == playerHand[i]:
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 'north' == playerHand[i]:
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 'haku' == playerHand[i]:
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 'green' == playerHand[i]:
            sortedList.append(playerHand[i])
    for i in range(len(playerHand)):
        if 'chun' == playerHand[i]:
            sortedList.append(playerHand[i])

    return sortedList



def TurnDecision():
    global gameInfo, p1Info, p2Info, p3Info, p4Info

    windList = ['east','south','west','north']
    windNum = random.randint(1, 4)

    gameInfo['turn'] = 'p' + str(windNum)

    windListNum = 0
    while True:
        if windNum == 1:
            p1Info['wind'] = windList[windListNum]
        elif windNum == 2:
            p2Info['wind'] = windList[windListNum]
        elif windNum == 3:
            p3Info['wind'] = windList[windListNum]
        elif windNum == 4:
            p4Info['wind'] = windList[windListNum]
        windListNum += 1
        if windListNum == 4:
            break
        
        windNum += 1
        if windNum == 5:
            windNum = 1





def ListInit(*exceptNum):
    global handList, handSelect
    
    if len(exceptNum) == 0:
        for i in range(len(handList)):
            handList[i] = 0
        handSelect = 0
    else:
        if exceptNum[0] == 'clear':
            handList = [0]*13
        else:
            for i in range(len(handList)):
                if i != exceptNum[0]-1:
                    handList[i] = 0



def GameRestartInit():
    global gameInfo
    global p1Info, p2Info, p3Info, p4Info

    gameInfo['kan'] = 0
    gameInfo['suukantsu'] = False
    gameInfo['count'] = 0
    gameInfo['rest'] = 70

    for i in range(1, 5):
        eval('p' + str(i) + 'Info')['shanten'] = 8
        eval('p' + str(i) + 'Info')['riichi'] = 0
        eval('p' + str(i) + 'Info')['doubleriichi'] = 0
        eval('p' + str(i) + 'Info')['ippatsu'] = 0
        eval('p' + str(i) + 'Info')['rinshan'] = False
        eval('p' + str(i) + 'Info')['hou'] = True
        eval('p' + str(i) + 'Info')['chankan'] = False
        eval('p' + str(i) + 'Info')['huro'] = []
        eval('p' + str(i) + 'Info')['canHuro'] = []

    for i in range(1, 5):
        ResetAction('p' + str(i), 'end')




def GameRuleSelect(SCREEN):
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global mouseInButton
    

    ba = 'east'
    redDora = False
    kuitan = True
    daisharin = True
    startScore = 25000


    ruleSelectList = [[1, 0, 0], [1, 0], [1, 0], [1, 0]]
    ruleSelectNum_1 = 0
    ruleSelectNum_2 = 0

    isInputDone = False
    while True:
        if isInputDone == True:
            isInputDone = False
            if ruleSelectNum_1 == -1:
                if ruleSelectList[0][0] == 1:
                    ba = 'east'
                elif ruleSelectList[0][1] == 1:
                    ba = 'south'
                elif ruleSelectList[0][2] == 1:
                    ba = 'north'

                if ruleSelectList[1][0] == 1:
                    redDora = True
                elif ruleSelectList[1][1] == 1:
                    redDora = False

                if ruleSelectList[2][0] == 1:
                    kuitan = True
                elif ruleSelectList[2][1] == 1:
                    kuitan = False

                if ruleSelectList[3][0] == 1:
                    daisharin = True
                elif ruleSelectList[3][1] == 1:
                    daisharin = False
                    
                pygame.time.wait(500)
                break
            else:
                for i in range(len(ruleSelectList[ruleSelectNum_1])):
                    ruleSelectList[ruleSelectNum_1][i] = 0
                ruleSelectList[ruleSelectNum_1][ruleSelectNum_2] = 1

        ##########Key Input##########
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                    
            ##########mouse##########
            if pygame.mouse.get_focused():
                mX, mY = pygame.mouse.get_pos()

                        
                if enterButton.collidepoint(mX, mY):
                    ruleSelectNum_1 = -1
                    mouseInButton = True

                elif baButton_1.collidepoint(mX, mY):
                    ruleSelectNum_1 = 0
                    ruleSelectNum_2 = 0
                    mouseInButton = True
                elif baButton_2.collidepoint(mX, mY):
                    ruleSelectNum_1 = 0
                    ruleSelectNum_2 = 1
                    mouseInButton = True
                elif baButton_3.collidepoint(mX, mY):
                    ruleSelectNum_1 = 0
                    ruleSelectNum_2 = 2
                    mouseInButton = True

                elif redDoraButton_yes.collidepoint(mX, mY):
                    ruleSelectNum_1 = 1
                    ruleSelectNum_2 = 0
                    mouseInButton = True
                elif redDoraButton_no.collidepoint(mX, mY):
                    ruleSelectNum_1 = 1
                    ruleSelectNum_2 = 1
                    mouseInButton = True

                elif kuitanButton_yes.collidepoint(mX, mY):
                    ruleSelectNum_1 = 2
                    ruleSelectNum_2 = 0
                    mouseInButton = True
                elif kuitanButton_no.collidepoint(mX, mY):
                    ruleSelectNum_1 = 2
                    ruleSelectNum_2 = 1
                    mouseInButton = True

                elif daisharinButton_yes.collidepoint(mX, mY):
                    ruleSelectNum_1 = 3
                    ruleSelectNum_2 = 0
                    mouseInButton = True
                elif daisharinButton_no.collidepoint(mX, mY):
                    ruleSelectNum_1 = 3
                    ruleSelectNum_2 = 1
                    mouseInButton = True

                if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                    isInputDone = True
                mouseInButton = False
                    
            ##########keyboard##########
            if not hasattr(event, 'key'):
                continue
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if ruleSelectNum_1 == -1:
                        ruleSelectNum_1 = 3
                    elif ruleSelectNum_1 > 0:
                        ruleSelectNum_1 -= 1
                    ruleSelectNum_2 = ruleSelectList[ruleSelectNum_1].index(1)
                elif event.key == K_DOWN:
                    if ruleSelectNum_1 == 3:
                        ruleSelectNum_1 = -1
                    elif ruleSelectNum_1 < 3 and ruleSelectNum_1 != -1:
                        ruleSelectNum_1 += 1
                    ruleSelectNum_2 = ruleSelectList[ruleSelectNum_1].index(1)
                elif event.key == K_LEFT:
                    if ruleSelectNum_1 != -1:
                        if ruleSelectNum_2 > 0:
                            ruleSelectNum_2 -= 1
                elif event.key == K_RIGHT:
                    if ruleSelectNum_1 == 0:
                        if ruleSelectNum_2 < 2:
                            ruleSelectNum_2 += 1
                    elif ruleSelectNum_1 != -1:
                        if ruleSelectNum_2 < 1:
                            ruleSelectNum_2 += 1
                elif event.key == K_RETURN:
                    isInputDone = True


        
        SCREEN.fill((150, 150, 150))


        if ruleSelectNum_1 == -1:
            pygame.draw.rect(SCREEN, Color('white'), enterButton_s)
            
        elif ruleSelectNum_1 == 0:
            if ruleSelectNum_2 == 0:
                pygame.draw.rect(SCREEN, Color('white'), baButton_1_s)
            elif ruleSelectNum_2 == 1:
                pygame.draw.rect(SCREEN, Color('white'), baButton_2_s)
            elif ruleSelectNum_2 == 2:
                pygame.draw.rect(SCREEN, Color('white'), baButton_3_s)
                
        elif ruleSelectNum_1 == 1:
            if ruleSelectNum_2 == 0:
                pygame.draw.rect(SCREEN, Color('white'), redDoraButton_yes_s)
            elif ruleSelectNum_2 == 1:
                pygame.draw.rect(SCREEN, Color('white'), redDoraButton_no_s)

        elif ruleSelectNum_1 == 2:
            if ruleSelectNum_2 == 0:
                pygame.draw.rect(SCREEN, Color('white'), kuitanButton_yes_s)
            elif ruleSelectNum_2 == 1:
                pygame.draw.rect(SCREEN, Color('white'), kuitanButton_no_s)

        elif ruleSelectNum_1 == 3:
            if ruleSelectNum_2 == 0:
                pygame.draw.rect(SCREEN, Color('white'), daisharinButton_yes_s)
            elif ruleSelectNum_2 == 1:
                pygame.draw.rect(SCREEN, Color('white'), daisharinButton_no_s)
        

        pygame.draw.rect(SCREEN, buttonColor, baButton)
        SCREEN.blit(textBa, (baButton.x + 80, baButton.y))
        pygame.draw.rect(SCREEN, buttonColor, baButton_1)
        if ruleSelectList[0][0] == 1:
            SCREEN.blit(textBa_1_s, (baButton_1.x + 55, baButton_1.y))
        else:
            SCREEN.blit(textBa_1, (baButton_1.x + 55, baButton_1.y))
        pygame.draw.rect(SCREEN, buttonColor, baButton_2)
        if ruleSelectList[0][1] == 1:
            SCREEN.blit(textBa_2_s, (baButton_2.x + 40, baButton_2.y))
        else:
            SCREEN.blit(textBa_2, (baButton_2.x + 40, baButton_2.y))
        pygame.draw.rect(SCREEN, buttonColor, baButton_3)
        if ruleSelectList[0][2] == 1:
            SCREEN.blit(textBa_3_s, (baButton_3.x + 45, baButton_3.y))
        else:
            SCREEN.blit(textBa_3, (baButton_3.x + 45, baButton_3.y))

        pygame.draw.rect(SCREEN, buttonColor, redDoraButton)
        SCREEN.blit(textRedDora, (redDoraButton.x + 45, redDoraButton.y))
        pygame.draw.rect(SCREEN, buttonColor, redDoraButton_yes)
        if ruleSelectList[1][0] == 1:
            SCREEN.blit(text_Yes_s, (redDoraButton_yes.x + 65, redDoraButton_yes.y))
        else:
            SCREEN.blit(text_Yes, (redDoraButton_yes.x + 65, redDoraButton_yes.y))
        pygame.draw.rect(SCREEN, buttonColor, redDoraButton_no)
        if ruleSelectList[1][1] == 1:
            SCREEN.blit(text_No_s, (redDoraButton_no.x + 65, redDoraButton_no.y))
        else:
            SCREEN.blit(text_No, (redDoraButton_no.x + 65, redDoraButton_no.y))

        pygame.draw.rect(SCREEN, buttonColor, kuitanButton)
        SCREEN.blit(textKuitan, (kuitanButton.x + 50, kuitanButton.y))
        pygame.draw.rect(SCREEN, buttonColor, kuitanButton_yes)
        if ruleSelectList[2][0] == 1:
            SCREEN.blit(text_Yes_s, (kuitanButton_yes.x + 65, kuitanButton_yes.y))
        else:
            SCREEN.blit(text_Yes, (kuitanButton_yes.x + 65, kuitanButton_yes.y))
        pygame.draw.rect(SCREEN, buttonColor, kuitanButton_no)
        if ruleSelectList[2][1] == 1:
            SCREEN.blit(text_No_s, (kuitanButton_no.x + 65, kuitanButton_no.y))
        else:
            SCREEN.blit(text_No, (kuitanButton_no.x + 65, kuitanButton_no.y))

        pygame.draw.rect(SCREEN, buttonColor, daisharinButton)
        SCREEN.blit(textDaisharin, (daisharinButton.x + 45, daisharinButton.y))
        pygame.draw.rect(SCREEN, buttonColor, daisharinButton_yes)
        if ruleSelectList[3][0] == 1:
            SCREEN.blit(text_Yes_s, (daisharinButton_yes.x + 65, daisharinButton_yes.y))
        else:
            SCREEN.blit(text_Yes, (daisharinButton_yes.x + 65, daisharinButton_yes.y))
        pygame.draw.rect(SCREEN, buttonColor, daisharinButton_no)
        if ruleSelectList[3][1] == 1:
            SCREEN.blit(text_No_s, (daisharinButton_no.x + 65, daisharinButton_no.y))
        else:
            SCREEN.blit(text_No, (daisharinButton_no.x + 65, daisharinButton_no.y))


        pygame.draw.rect(SCREEN, buttonColor, enterButton)
        SCREEN.blit(textEnter, (enterButton.x, enterButton.y))


        

        pygame.display.flip()
        clock.tick(TARGET_FPS)
        


    gameInfo['ba'] = ba
    gameInfo['redDora'] = redDora
    gameInfo['kuitan'] = kuitan
    gameInfo['daisharin'] = daisharin

    p1Info['score'] = startScore
    p2Info['score'] = startScore
    p3Info['score'] = startScore
    p4Info['score'] = startScore




def SaveData():
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Discard, p2Discard, p3Discard, p4Discard
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global cardList
    
    count = 0
    
    with open('save.mj', 'w') as f:
        f.write('**Game Info**\n')
        count = 0
        for i in gameInfo.keys():
            f.write(i + ':' + str(gameInfo[i]))
            count += 1
            if count != len(gameInfo):
                f.write('.')
            else:
                f.write('\n')
                
        f.write('**P1 Info**\n')
        count = 0
        for i in p1Info.keys():
            f.write(i + ':' + str(p1Info[i]))
            count += 1
            if count != len(p1Info):
                f.write('.')
            else:
                f.write('\n')
        f.write('**P2 Info**\n')
        count = 0
        for i in p2Info.keys():
            f.write(i + ':' + str(p2Info[i]))
            count += 1
            if count != len(p2Info):
                f.write('.')
            else:
                f.write('\n')
        f.write('**P3 Info**\n')
        count = 0
        for i in p3Info.keys():
            f.write(i + ':' + str(p3Info[i]))
            count += 1
            if count != len(p3Info):
                f.write('.')
            else:
                f.write('\n')
        f.write('**P4 Info**\n')
        count = 0
        for i in p4Info.keys():
            f.write(i + ':' + str(p4Info[i]))
            count += 1
            if count != len(p4Info):
                f.write('.')
            else:
                f.write('\n')

        f.write('**Card**\n')
        count = 0
        for i in cardList:
            f.write(i)
            count += 1
            if count != len(cardList):
                f.write('.')
            else:
                f.write('\n')
                
        f.write('**P1 Hand**\n')
        count = 0
        for i in p1Hand:
            f.write(i)
            count += 1
            if count != len(p1Hand):
                f.write('.')
            else:
                f.write('\n')
        f.write('**P2 Hand**\n')
        count = 0
        for i in p2Hand:
            f.write(i)
            count += 1
            if count != len(p2Hand):
                f.write('.')
            else:
                f.write('\n')
        f.write('**P3 Hand**\n')
        count = 0
        for i in p3Hand:
            f.write(i)
            count += 1
            if count != len(p3Hand):
                f.write('.')
            else:
                f.write('\n')
        f.write('**P4 Hand**\n')
        count = 0
        for i in p4Hand:
            f.write(i)
            count += 1
            if count != len(p4Hand):
                f.write('.')
            else:
                f.write('\n')

        f.write('**P1 Discard**\n')
        count = 0
        if len(p1Discard) != 0:
            for i in p1Discard:
                f.write(i)
                count += 1
                if count != len(p1Discard):
                    f.write('.')
                else:
                    f.write('\n')
        else:
            f.write('0\n')
        f.write('**P2 Discard**\n')
        count = 0
        if len(p2Discard) != 0:
            for i in p2Discard:
                f.write(i)
                count += 1
                if count != len(p2Discard):
                    f.write('.')
                else:
                    f.write('\n')
        else:
            f.write('0\n')
        f.write('**P3 Discard**\n')
        count = 0
        if len(p3Discard) != 0:
            for i in p3Discard:
                f.write(i)
                count += 1
                if count != len(p3Discard):
                    f.write('.')
                else:
                    f.write('\n')
        else:
            f.write('0\n')
        f.write('**P4 Discard**\n')
        count = 0
        if len(p4Discard) != 0:
            for i in p4Discard:
                f.write(i)
                count += 1
                if count != len(p4Discard):
                    f.write('.')
                else:
                    f.write('\n')
        else:
            f.write('0\n')



def LoadData():
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Discard, p2Discard, p3Discard, p4Discard
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global cardList, handList

    ListInit()
    CardInit()
    GameInfoInit()

    line = ''
    infoList = []
    infoList_s = []
    
    with open('save.mj', 'r') as f:
        while True:
            line = f.readline().rstrip()
            if line == '':
                return False
            elif line == '**Game Info**':
                infoList = f.readline().rstrip().split('.')
                for i in range(len(infoList)):
                    infoList_s = infoList[i].split(':')
                    gameInfo[infoList_s[0]] = infoList_s[1]
                gameInfo['renchan'] = int(gameInfo['renchan'])
                gameInfo['kan'] = int(gameInfo['kan'])

                if gameInfo['suukantsu'] == 'True':
                    gameInfo['suukantsu'] = True
                else:
                    gameInfo['suukantsu'] = False
                    
                if gameInfo['redDora'] == 'True':
                    gameInfo['redDora'] = True
                else:
                    gameInfo['redDora'] = False
                    
                if gameInfo['kuitan'] == 'True':
                    gameInfo['kuitan'] = True
                else:
                    gameInfo['kuitan'] = False
                    
                if gameInfo['daisharin'] == 'True':
                    gameInfo['daisharin'] = True
                else:
                    gameInfo['daisharin'] = False
                    
                gameInfo['count'] = int(gameInfo['count'])
                gameInfo['rest'] = int(gameInfo['rest'])
                
            elif line == '**P1 Info**':
                infoList = f.readline().rstrip().split('.')
                for i in range(len(infoList)):
                    infoList_s = infoList[i].split(':')
                    p1Info[infoList_s[0]] = infoList_s[1]
                p1Info['score'] = int(p1Info['score'])
                p1Info['shanten'] = int(p1Info['shanten'])
                p1Info['riichi'] = int(p1Info['riichi'])
                p1Info['doubleriichi'] = int(p1Info['doubleriichi'])
                p1Info['ippatsu'] = int(p1Info['ippatsu'])
                    
                if p1Info['rinshan'] == 'True':
                    p1Info['rinshan'] = True
                else:
                    p1Info['rinshan'] = False

                if p1Info['hou'] == 'True':
                    p1Info['hou'] = True
                else:
                    p1Info['hou'] = False

                if p1Info['chankan'] == 'True':
                    p1Info['chankan'] = True
                else:
                    p1Info['chankan'] = False
                    
                p1Info['huro'] = list(eval(p1Info['huro']))
                p1Info['canHuro'] = list(eval(p1Info['canHuro']))
                p1Info['canAction'] = list(eval(p1Info['canAction']))
                
            elif line == '**P2 Info**':
                infoList = f.readline().rstrip().split('.')
                for i in range(len(infoList)):
                    infoList_s = infoList[i].split(':')
                    p2Info[infoList_s[0]] = infoList_s[1]
                p2Info['score'] = int(p2Info['score'])
                p2Info['shanten'] = int(p2Info['shanten'])
                p2Info['riichi'] = int(p2Info['riichi'])
                p2Info['doubleriichi'] = int(p2Info['doubleriichi'])
                p2Info['ippatsu'] = int(p2Info['ippatsu'])
                    
                if p2Info['rinshan'] == 'True':
                    p2Info['rinshan'] = True
                else:
                    p2Info['rinshan'] = False

                if p2Info['hou'] == 'True':
                    p2Info['hou'] = True
                else:
                    p2Info['hou'] = False

                if p2Info['chankan'] == 'True':
                    p2Info['chankan'] = True
                else:
                    p2Info['chankan'] = False
                    
                p2Info['huro'] = list(eval(p2Info['huro']))
                p2Info['canHuro'] = list(eval(p2Info['canHuro']))
                
            elif line == '**P3 Info**':
                infoList = f.readline().rstrip().split('.')
                for i in range(len(infoList)):
                    infoList_s = infoList[i].split(':')
                    p3Info[infoList_s[0]] = infoList_s[1]
                p3Info['score'] = int(p3Info['score'])
                p3Info['shanten'] = int(p3Info['shanten'])
                p3Info['riichi'] = int(p3Info['riichi'])   
                p3Info['doubleriichi'] = int(p3Info['doubleriichi'])
                p3Info['ippatsu'] = int(p3Info['ippatsu'])
                    
                if p3Info['rinshan'] == 'True':
                    p3Info['rinshan'] = True
                else:
                    p3Info['rinshan'] = False

                if p3Info['hou'] == 'True':
                    p3Info['hou'] = True
                else:
                    p3Info['hou'] = False

                if p3Info['chankan'] == 'True':
                    p3Info['chankan'] = True
                else:
                    p3Info['chankan'] = False
                    
                p3Info['huro'] = list(eval(p3Info['huro']))
                p3Info['canHuro'] = list(eval(p3Info['canHuro']))
                
            elif line == '**P4 Info**':
                infoList = f.readline().rstrip().split('.')
                for i in range(len(infoList)):
                    infoList_s = infoList[i].split(':')
                    p4Info[infoList_s[0]] = infoList_s[1]
                p4Info['score'] = int(p4Info['score'])
                p4Info['shanten'] = int(p4Info['shanten'])
                p4Info['riichi'] = int(p4Info['riichi'])
                p4Info['doubleriichi'] = int(p4Info['doubleriichi'])
                p4Info['ippatsu'] = int(p4Info['ippatsu'])
                    
                if p4Info['rinshan'] == 'True':
                    p4Info['rinshan'] = True
                else:
                    p4Info['rinshan'] = False

                if p4Info['hou'] == 'True':
                    p4Info['hou'] = True
                else:
                    p4Info['hou'] = False

                if p4Info['chankan'] == 'True':
                    p4Info['chankan'] = True
                else:
                    p4Info['chankan'] = False
                    
                p4Info['huro'] = list(eval(p4Info['huro']))
                p4Info['canHuro'] = list(eval(p4Info['canHuro']))

            elif line == '**Card**':
                infoList = f.readline().rstrip().split('.')
                cardList = infoList.copy()
            
            elif line == '**P1 Hand**':
                infoList = f.readline().rstrip().split('.')
                p1Hand = infoList.copy()
                if len(p1Hand) > len(handList):
                    for i in range(len(p1Hand) - len(handList)):
                        handList.append(0)
                elif len(p1Hand) < len(handList):
                    for i in range(len(handList) - len(p1Hand)):
                        handList.pop()
            elif line == '**P2 Hand**':
                infoList = f.readline().rstrip().split('.')
                p2Hand = infoList.copy()
            elif line == '**P3 Hand**':
                infoList = f.readline().rstrip().split('.')
                p3Hand = infoList.copy()
            elif line == '**P4 Hand**':
                infoList = f.readline().rstrip().split('.')
                p4Hand = infoList.copy()
                
            elif line == '**P1 Discard**':
                infoList = f.readline().rstrip().split('.')
                if infoList[0] != '0':
                    p1Discard = infoList.copy()
            elif line == '**P2 Discard**':
                infoList = f.readline().rstrip().split('.')
                if infoList[0] != '0':
                    p2Discard = infoList.copy()
            elif line == '**P3 Discard**':
                infoList = f.readline().rstrip().split('.')
                if infoList[0] != '0':
                    p3Discard = infoList.copy()
            elif line == '**P4 Discard**':
                infoList = f.readline().rstrip().split('.')
                if infoList[0] != '0':
                    p4Discard = infoList.copy()
                return

                

def DataReset():
    f = open('save.mj', 'w')
    f.close()

############################################################



############################## Screen, Input ##############################

def GameScreen(SCREEN, *printType):
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Discard, p2Discard, p3Discard, p4Discard
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global cutSize
    global handList, cardList

    
    cardMoveNum = -1
    
    
    SCREEN.fill((50, 150, 50))

    #p1 패 출력
    for i in range(len(p1Hand)):
        cardMove = False
        if inputType == 0 and handList[i] == 1:
            cardMove = True
            
        if len(p1Hand) % 3 == 2 and i == len(p1Hand)-1:
            if cardMove == True:
                SCREEN.blit(eval(p1Hand[i]), (p1HandPos[0] + (cardSize.w*i) + 44, p1HandPos[1] - 10), cardSize)
            else:
                SCREEN.blit(eval(p1Hand[i]), (p1HandPos[0] + (cardSize.w*i) + 44, p1HandPos[1]), cardSize)
            if len(printType) == 0:
                SCREEN.blit(eval('text' + str(i+1)), ((p1HandPos[0]//2)*3 + (cardSize.w*i) + 44, p1HandPos[1] - 20))
        else:
            if cardMove == True:
                SCREEN.blit(eval(p1Hand[i]), (p1HandPos[0] + (cardSize.w*i), p1HandPos[1] - 10), cardSize)
            else:
                SCREEN.blit(eval(p1Hand[i]), (p1HandPos[0] + (cardSize.w*i), p1HandPos[1]), cardSize)
            if len(printType) == 0:
                SCREEN.blit(eval('text' + str(i+1)), ((p1HandPos[0]//2)*3 + 12 + (cardSize.w*i), p1HandPos[1] - 20))

    #p2 ~ p4 패 출력
    for i in range(len(p2Hand)):
        if len(p2Hand) % 3 == 2 and i == len(p2Hand) - 1:
            SCREEN.blit(pygame.transform.rotate(up, 270), (p2HandPos[0], p2HandPos[1] - (cardSize_up.w * i) - cardSize_up.w // 4), cardSize_up_s)
        else:
            SCREEN.blit(pygame.transform.rotate(up, 270), (p2HandPos[0], p2HandPos[1] - (cardSize_up.w * i)), cardSize_up_s)

    for i in range(len(p3Hand)):
        if len(p3Hand) % 3 == 2 and i == len(p3Hand) - 1:
            SCREEN.blit(up, (p3HandPos[0] - (cardSize_up.w * i) - cardSize_up.w / 4, p3HandPos[1]), cardSize_up)
        else:
            SCREEN.blit(up, (p3HandPos[0] - (cardSize_up.w * i), p3HandPos[1]), cardSize_up)

    for i in range(len(p4Hand)):
        if len(p4Hand) % 3 == 2 and i == len(p4Hand) - 1:
            SCREEN.blit(pygame.transform.rotate(up, 90), (p4HandPos[0], p4HandPos[1] + (cardSize_up.w * i) + cardSize_up.w // 4), cardSize_up_s)
        else:
            SCREEN.blit(pygame.transform.rotate(up, 90), (p4HandPos[0], p4HandPos[1] + (cardSize_up.w * i)), cardSize_up_s)
                

    #운 패 출력
    if len(p1Info['huro']) != 0:
        cardHuroPos_x = p1HuroPos[0]
        cardHuroPos_y = p1HuroPos[1]
        moveSize = 0
        for i in range(len(p1Info['huro'])):
            count = 0
            kanIndex = -1
            for j in range(len(p1Info['huro'][i])):
                if p1Info['huro'][i][j][-1] != '1':
                    count += 1
                    if count == 2:
                        kanIndex = j
            if count == 0:
                moveSize = cardSize_p1_huro.w * 4
            elif count == 2 or len(p1Info['huro'][i]) == 3:
                moveSize = cardSize_p1_huro.w * 2 + cardSize_p1_huro.h
            else:
                moveSize = cardSize_p1_huro.w * 3 + cardSize_p1_huro.h
            cardHuroPos_x -= moveSize

            for j in range(len(p1Info['huro'][i])):
                if count == 0:
                    if j == 0 or j == 3:
                        SCREEN.blit(pygame.transform.scale(back, middleChangeSize), (cardHuroPos_x, cardHuroPos_y), cardSize_p1_huro)
                    else:
                        SCREEN.blit(pygame.transform.scale(eval(p1Info['huro'][i][j][:-1]), middleChangeSize), (cardHuroPos_x, cardHuroPos_y), cardSize_p1_huro)
                    cardHuroPos_x += cardSize_p1_huro.w
                else:
                    if p1Info['huro'][i][j][-1] == '1':
                        SCREEN.blit(pygame.transform.scale(eval(p1Info['huro'][i][j][:-1]), middleChangeSize), (cardHuroPos_x, cardHuroPos_y), cardSize_p1_huro)
                        cardHuroPos_x += cardSize_p1_huro.w
                    else:
                        if j == kanIndex - 1:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p1Info['huro'][i][j][:-1]), middleChangeSize), p2Degree), (cardHuroPos_x, cardHuroPos_y + (cardSize_p1_huro.h - cardSize_p1_huro.w)), cardSize_p1_huro_s)
                        elif j == kanIndex:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p1Info['huro'][i][j][:-1]), middleChangeSize), p2Degree), (cardHuroPos_x, cardHuroPos_y - cardSize_p1_huro.w + (cardSize_p1_huro.h - cardSize_p1_huro.w)), cardSize_p1_huro_s)
                            cardHuroPos_x += cardSize_p1_huro.h
                        else:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p1Info['huro'][i][j][:-1]), middleChangeSize), p2Degree), (cardHuroPos_x, cardHuroPos_y + (cardSize_p1_huro.h - cardSize_p1_huro.w)), cardSize_p1_huro_s)
                            cardHuroPos_x += cardSize_p1_huro.h
            cardHuroPos_x -= moveSize

    if len(p2Info['huro']) != 0:
        cardHuroPos_x = p2HuroPos[0]
        cardHuroPos_y = p2HuroPos[1]
        moveSize = 0
        for i in range(len(p2Info['huro'])):
            count = 0
            kanIndex = -1
            for j in range(len(p2Info['huro'][i])):
                if p2Info['huro'][i][j][-1] != '1':
                    count += 1
                    if count == 2:
                        kanIndex = j
            if count == 0:
                moveSize = cardSize_p2.h * 4
            elif count == 2 or len(p2Info['huro'][i]) == 3:
                moveSize = cardSize_p2.h * 2 + cardSize_p2.w
            else:
                moveSize = cardSize_p2.h * 3 + cardSize_p2.w
            cardHuroPos_y += moveSize

            for j in range(len(p2Info['huro'][i])):
                if count == 0:
                    if j == 0 or j == 3:
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(back, smallChangeSize), p2Degree), (cardHuroPos_x, cardHuroPos_y - cardSize_p2.h), cardSize_p2)
                    else:
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p2Info['huro'][i][j][:-1]), smallChangeSize), p2Degree), (cardHuroPos_x, cardHuroPos_y - cardSize_p2.h), cardSize_p2)
                    cardHuroPos_y -= cardSize_p2.h
                else:
                    if p2Info['huro'][i][j][-1] == '1':
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p2Info['huro'][i][j][:-1]), smallChangeSize), p2Degree), (cardHuroPos_x, cardHuroPos_y - cardSize_p2.h), cardSize_p2)
                        cardHuroPos_y -= cardSize_p2.h
                    else:
                        if j == kanIndex - 1:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p2Info['huro'][i][j][:-1]), smallChangeSize), p3Degree), (cardHuroPos_x + (cardSize_p3.h - cardSize_p3.w), cardHuroPos_y - (cardSize_p3.h - cardSize_p3.w) - cardSize_p3.w), cardSize_p3)
                        elif j == kanIndex:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p2Info['huro'][i][j][:-1]), smallChangeSize), p3Degree), (cardHuroPos_x - cardSize_p3.w + (cardSize_p3.h - cardSize_p3.w), cardHuroPos_y - (cardSize_p3.h - cardSize_p3.w) - cardSize_p3.w), cardSize_p3)
                            cardHuroPos_y -= cardSize_p3.h
                        else:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p2Info['huro'][i][j][:-1]), smallChangeSize), p3Degree), (cardHuroPos_x + (cardSize_p3.h - cardSize_p3.w), cardHuroPos_y - (cardSize_p3.h - cardSize_p3.w) - cardSize_p3.w), cardSize_p3)
                            cardHuroPos_y -= cardSize_p3.h
            cardHuroPos_y += moveSize

    if len(p3Info['huro']) != 0:
        cardHuroPos_x = p3HuroPos[0]
        cardHuroPos_y = p3HuroPos[1]
        moveSize = 0
        for i in range(len(p3Info['huro'])):
            count = 0
            kanIndex = -1
            for j in range(len(p3Info['huro'][i])):
                if p3Info['huro'][i][j][-1] != '1':
                    count += 1
                    if count == 2:
                        kanIndex = j
            if count == 0:
                moveSize = cardSize_p3.w * 4
            elif count == 2 or len(p3Info['huro'][i]) == 3:
                moveSize = cardSize_p3.w * 2 + cardSize_p3.h
            else:
                moveSize = cardSize_p3.w * 3 + cardSize_p3.h
            cardHuroPos_x += moveSize

            for j in range(len(p3Info['huro'][i])):
                if count == 0:
                    if j == 0 or j == 3:
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(back, smallChangeSize), p3Degree), (cardHuroPos_x - cardSize_p3.w, cardHuroPos_y), cardSize_p3)
                    else:
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p3Info['huro'][i][j][:-1]), smallChangeSize), p3Degree), (cardHuroPos_x - cardSize_p3.w, cardHuroPos_y), cardSize_p3)
                    cardHuroPos_x -= cardSize_p3.w
                else:
                    if p3Info['huro'][i][j][-1] == '1':
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p3Info['huro'][i][j][:-1]), smallChangeSize), p3Degree), (cardHuroPos_x - cardSize_p3.w, cardHuroPos_y), cardSize_p3)
                        cardHuroPos_x -= cardSize_p3.w
                    else:
                        if j == kanIndex - 1:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p3Info['huro'][i][j][:-1]), smallChangeSize), p4Degree), (cardHuroPos_x - cardSize_p4.h - (cardSize_p4.w - cardSize_p4.h), cardHuroPos_y), cardSize_p4)
                        elif j == kanIndex:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p3Info['huro'][i][j][:-1]), smallChangeSize), p4Degree), (cardHuroPos_x - cardSize_p4.h - (cardSize_p4.w - cardSize_p4.h), cardHuroPos_y + cardSize_p4.h), cardSize_p4)
                            cardHuroPos_x -= cardSize_p4.w
                        else:
                            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p3Info['huro'][i][j][:-1]), smallChangeSize), p4Degree), (cardHuroPos_x - cardSize_p4.h - (cardSize_p4.w - cardSize_p4.h), cardHuroPos_y), cardSize_p4)
                            cardHuroPos_x -= cardSize_p4.w
            cardHuroPos_x += moveSize

    if len(p4Info['huro']) != 0:
        cardHuroPos_x = p4HuroPos[0]
        cardHuroPos_y = p4HuroPos[1]
        moveSize = 0
        for i in range(len(p4Info['huro'])):
            count = 0
            kanIndex = -1
            for j in range(len(p4Info['huro'][i])):
                if p4Info['huro'][i][j][-1] != '1':
                    count += 1
                    if count == 2:
                        kanIndex = j
            if count == 0:
                moveSize = cardSize_p4.h * 4
            elif count == 2 or len(p4Info['huro'][i]) == 3:
                moveSize = cardSize_p4.h * 2 + cardSize_p4.w
            else:
                moveSize = cardSize_p4.h * 3 + cardSize_p4.w
            cardHuroPos_y -= moveSize

            for j in range(len(p4Info['huro'][i])):
                if count == 0:
                    if j == 0 or j == 3:
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(back, smallChangeSize), p4Degree), (cardHuroPos_x, cardHuroPos_y + cardSize_p4.h), cardSize_p4)
                    else:
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p4Info['huro'][i][j][:-1]), smallChangeSize), p4Degree), (cardHuroPos_x, cardHuroPos_y + cardSize_p4.h), cardSize_p4)
                    cardHuroPos_y += cardSize_p4.h
                else:
                    if p4Info['huro'][i][j][-1] == '1':
                        SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p4Info['huro'][i][j][:-1]), smallChangeSize), p4Degree), (cardHuroPos_x, cardHuroPos_y + cardSize_p4.h), cardSize_p4)
                        cardHuroPos_y += cardSize_p4.h
                    else:
                        if j == kanIndex - 1:
                            SCREEN.blit(pygame.transform.scale(eval(p4Info['huro'][i][j][:-1]), smallChangeSize), (cardHuroPos_x, cardHuroPos_y + cardSize_p1.w), cardSize_p1)
                        elif j == kanIndex:
                            SCREEN.blit(pygame.transform.scale(eval(p4Info['huro'][i][j][:-1]), smallChangeSize), (cardHuroPos_x + cardSize_p1.w, cardHuroPos_y + cardSize_p1.w), cardSize_p1)
                            cardHuroPos_y += cardSize_p1.h
                        else:
                            SCREEN.blit(pygame.transform.scale(eval(p4Info['huro'][i][j][:-1]), smallChangeSize), (cardHuroPos_x, cardHuroPos_y + cardSize_p1.w), cardSize_p1)
                            cardHuroPos_y += cardSize_p1.h
            cardHuroPos_y -= moveSize

                            

    #샹텐 출력
    if len(printType) == 0 and p1Info['shanten'] >= 0:
        SCREEN.blit(eval('text' + str(p1Info['shanten']) + 'Shan'), (disSize_w - cardSize.w - 45, p1HandPos[1] - 60))

    #가운데
    middleRect = Rect(p1DisPos[0], disSize_h // 2 - cardSize_p1.h * 2 - 25, cardSize_p1.w * cutSize, cardSize_p1.w * 4)
    pygame.draw.rect(SCREEN, Color(150, 150, 150), middleRect)
    
    #현재 국 출력
    kyokuPos_x = disSize_w // 2 - cardSize_p1.w * 2
    kyokuPos_y = disSize_h // 2 - cardSize_p1.h * 2 - 20
    if gameInfo['ba'] == gameInfo['kyoku'][:-1] and gameInfo['kyoku'][-1] == '4':
        SCREEN.blit(text_allLast, (kyokuPos_x, kyokuPos_y))
    else:
        if gameInfo['kyoku'][:-1] == 'east':
            SCREEN.blit(eval('text_' + gameInfo['kyoku'][:-1] + '_s'), (kyokuPos_x, kyokuPos_y))
        else:
            SCREEN.blit(eval('text_' + gameInfo['kyoku'][:-1]), (kyokuPos_x, kyokuPos_y))
        SCREEN.blit(eval('text' + gameInfo['kyoku'][-1]), (kyokuPos_x + cardSize_p1.w // 2 + 7, kyokuPos_y))
        SCREEN.blit(text_kyoku, (kyokuPos_x + cardSize_p1.w, kyokuPos_y))

    #본장 출력
    renchanPos_x = kyokuPos_x + cardSize_p1.w // 2 * 5
    renchanPos_y = kyokuPos_y

    if gameInfo['renchan'] // 10 != 0:
        SCREEN.blit(eval('text' + str(gameInfo['renchan'] // 10)), (renchanPos_x - 15, renchanPos_y))
    SCREEN.blit(eval('text' + str(gameInfo['renchan'] % 10)), (renchanPos_x, renchanPos_y))
    SCREEN.blit(text_renchan, (renchanPos_x + cardSize_p1.w // 2, renchanPos_y))
        
    #도라표시패 출력
    SCREEN.blit(text_dora, (disSize_w // 2 - cardSize_p1.w // 2 * 5 - 33 , disSize_h // 2 - cardSize_p1.h * 2 + 37))
    for i in range(gameInfo['kan'] + 1):
        SCREEN.blit(pygame.transform.scale(eval(cardList[-6 + gameInfo['kan'] - (i * 2)]), smallChangeSize), (disSize_w // 2 - cardSize_p1.w // 2 * 5 + 30 + (cardSize_p1.w * i), disSize_h // 2 - cardSize_p1.h * 2 + 33), cardSize_p1)
        
    #남은패산 수 출력
    text_cardRest = textFont.render('패산 : ' + str(gameInfo['rest']), True, textColor)
    SCREEN.blit(text_cardRest, (disSize_w // 2 - cardSize_p1.w // 2 * 3, disSize_h // 2 - cardSize_p1.h // 2 + 5))

    #바람, 점수 출력
    #p1
    SCREEN.blit(eval('text_' + p1Info['wind']), (p1DisPos[0] + 10, disSize_h // 2 - cardSize_p1.h + 35))
    text_score_p1 = textFont_small.render(str(p1Info['score']), True, textColor)
    SCREEN.blit(text_score_p1, (p1DisPos[0] + cardSize_p1.w + 10, disSize_h // 2 - cardSize_p1.h + 43))
    #p2
    SCREEN.blit(pygame.transform.rotate(eval('text_' + p2Info['wind']), p2Degree), (p1DisPos[0] + cardSize_p1.w * 9 - 5, disSize_h // 2 - cardSize_p1.h + 45))
    text_score_p2 = textFont_small.render(str(p2Info['score']), True, textColor)
    SCREEN.blit(pygame.transform.rotate(text_score_p2, p2Degree), (p1DisPos[0] + cardSize_p1.w * 9, disSize_h // 2 - cardSize_p1.h + 45 - cardSize_p1.w * 2 + 15))
    #p3
    SCREEN.blit(pygame.transform.rotate(eval('text_' + p3Info['wind']), p3Degree), (p1DisPos[0] + cardSize_p1.w * 9 + 5, disSize_h // 2 - cardSize_p1.h * 2 - 20))
    text_score_p3 = textFont_small.render(str(p3Info['score']), True, textColor)
    SCREEN.blit(pygame.transform.rotate(text_score_p3, p3Degree), (p1DisPos[0] + cardSize_p1.w * 7 + 20, disSize_h // 2 - cardSize_p1.h * 2 - 20))
    #p4
    SCREEN.blit(pygame.transform.rotate(eval('text_' + p4Info['wind']), p4Degree), (p1DisPos[0] + 5, disSize_h // 2 - cardSize_p1.h * 2 - 15))
    text_score_p4 = textFont_small.render(str(p4Info['score']), True, textColor)
    SCREEN.blit(pygame.transform.rotate(text_score_p4, p4Degree), (p1DisPos[0] + 5, disSize_h // 2 - cardSize_p1.h * 2 - 20 + cardSize_p1.w))

    
    

    #버린 패 출력
    riichiSize = 0
    for i in range(len(p1Discard)):
        if i%cutSize == 0:
            riichiSize = 0
        if 'riichi' in p1Discard[i]:
            riichiSize = cardSize_p1.h - cardSize_p1.w
            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p1Discard[i][:-6]), smallChangeSize), p2Degree), (p1DisPos[0] + cardSize_p1.w*(i%cutSize), p1DisPos[1] + cardSize_p1.h*(i//cutSize)), cardSize_p2)
        else:
            SCREEN.blit(pygame.transform.scale(eval(p1Discard[i]), smallChangeSize), (p1DisPos[0] + cardSize_p1.w*(i%cutSize) + riichiSize, p1DisPos[1] + cardSize_p1.h*(i//cutSize)), cardSize_p1)
        
    riichiSize = 0 
    for i in range(len(p2Discard)):
        if i%cutSize == 0:
            riichiSize = 0
        if 'riichi' in p2Discard[i]:
            riichiSize = cardSize_p2.w - cardSize_p2.h
            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p2Discard[i][:-6]), smallChangeSize), p3Degree), (p2DisPos[0] + cardSize_p2.w*(i//cutSize), p2DisPos[1] - cardSize_p2.h*(i%cutSize) - riichiSize), cardSize_p3)
        else:
            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p2Discard[i]), smallChangeSize), p2Degree), (p2DisPos[0] + cardSize_p2.w*(i//cutSize), p2DisPos[1] - cardSize_p2.h*(i%cutSize) - riichiSize), cardSize_p2)

    riichiSize = 0
    for i in range(len(p3Discard)):
        if i%cutSize == 0:
            riichiSize = 0
        if 'riichi' in p3Discard[i]:
            riichiSize = cardSize_p3.h - cardSize_p3.w
            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p3Discard[i][:-6]), smallChangeSize), p4Degree), (p3DisPos[0] - cardSize_p3.w*(i%cutSize) - riichiSize, p3DisPos[1] - cardSize_p3.h*(i//cutSize) + riichiSize), cardSize_p4)
        else:
            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p3Discard[i]), smallChangeSize), p3Degree), (p3DisPos[0] - cardSize_p3.w*(i%cutSize) - riichiSize, p3DisPos[1] - cardSize_p3.h*(i//cutSize)), cardSize_p3)

    riichiSize = 0
    for i in range(len(p4Discard)):
        if i%cutSize == 0:
            riichiSize = 0
        if 'riichi' in p4Discard[i]:
            riichiSize = cardSize_p4.w - cardSize_p4.h
            SCREEN.blit(pygame.transform.scale(eval(p4Discard[i][:-6]), smallChangeSize), (p4DisPos[0] - cardSize_p4.w*(i//cutSize) + riichiSize, p4DisPos[1] + cardSize_p4.h*(i%cutSize)), cardSize_p1)
        else:
            SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(p4Discard[i]), smallChangeSize), p4Degree), (p4DisPos[0] - cardSize_p4.w*(i//cutSize), p4DisPos[1] + cardSize_p4.h*(i%cutSize) + riichiSize), cardSize_p4)


    #Action 출력
    if ('kan' in actionList) == True:
        if inputType == 1 and actionList[actionSelect] == 'kan':
            pygame.draw.rect(SCREEN, buttonColor_s, f7Button_s)
        pygame.draw.rect(SCREEN, buttonColor, f7Button)
        SCREEN.blit(textKan, (f7Button.x + 45, f7Button.y - 3))
        SCREEN.blit(textF7, (f7Button.x + 40, f7Button.y - f7Button.h))

    if ('tsumo' in actionList) == True:
        if inputType == 1 and actionList[actionSelect] == 'tsumo':
            pygame.draw.rect(SCREEN, buttonColor_s, f8Button_s)
        pygame.draw.rect(SCREEN, buttonColor, f8Button)
        SCREEN.blit(textTsumo, (f8Button.x + 37, f8Button.y - 2))
        SCREEN.blit(textF8, (f8Button.x + 40, f8Button.y - f8Button.h))

    if ('riichi' in actionList) == True:
        if inputType == 1 and actionList[actionSelect] == 'riichi':
            pygame.draw.rect(SCREEN, buttonColor_s, f9Button_s)
        pygame.draw.rect(SCREEN, buttonColor, f9Button)
        SCREEN.blit(textRiichi, (f9Button.x + 37, f9Button.y - 1))
        SCREEN.blit(textF9, (f9Button.x + 40, f9Button.y - f9Button.h))

    if ('no' in actionList) == True:
        if inputType == 1 and actionList[actionSelect] == 'no':
            pygame.draw.rect(SCREEN, buttonColor_s, f9Button_s)
        pygame.draw.rect(SCREEN, buttonColor, f9Button)
        SCREEN.blit(textNo, (f9Button.x + 10, f9Button.y - 3))
        SCREEN.blit(textF9, (f9Button.x + 40, f9Button.y - f9Button.h))




def KeyInput(SCREEN):
    global handSelect, handList, mouseInButton
    global actionSelect, actionList, mouseInButton_a
    global inputType
    
    
    if len(p1Info['canAction']) != 0:
        actionList = p1Info['canAction'].copy()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        ##########mouse##########
        if pygame.mouse.get_focused():
            mX, mY = pygame.mouse.get_pos()
            if p1Info['riichi'] == 0:
                if cardPos1.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 1
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 2:
                    if len(handList) == 2:
                        if Rect(cardPos2.x + 44, cardPos2.y, cardPos2.w, cardPos2.h).collidepoint(mX, mY):
                            inputType = 0
                            handSelect = 2
                            ListInit(handSelect)
                            handList[handSelect-1] = 1
                            mouseInButton = True
                    else:
                        if cardPos2.collidepoint(mX, mY):
                            inputType = 0
                            handSelect = 2
                            ListInit(handSelect)
                            handList[handSelect-1] = 1
                            mouseInButton = True
                if len(handList) >= 3 and cardPos3.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 3
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 4 and cardPos4.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 4
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 5:
                    if len(handList) == 5:
                        if Rect(cardPos5.x + 44, cardPos5.y, cardPos5.w, cardPos5.h).collidepoint(mX, mY):
                            inputType = 0
                            handSelect = 5
                            ListInit(handSelect)
                            handList[handSelect-1] = 1
                            mouseInButton = True
                    else:
                        if cardPos5.collidepoint(mX, mY):
                            inputType = 0
                            handSelect = 5
                            ListInit(handSelect)
                            handList[handSelect-1] = 1
                            mouseInButton = True
                if len(handList) >= 6 and cardPos6.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 6
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 7 and cardPos7.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 7
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 8:
                    if len(handList) == 8:
                        if Rect(cardPos8.x + 44, cardPos8.y, cardPos8.w, cardPos8.h).collidepoint(mX, mY):
                            inputType = 0
                            handSelect = 8
                            ListInit(handSelect)
                            handList[handSelect-1] = 1
                            mouseInButton = True
                    else:
                       if cardPos8.collidepoint(mX, mY):
                            inputType = 0
                            handSelect = 8
                            ListInit(handSelect)
                            handList[handSelect-1] = 1
                            mouseInButton = True
                if len(handList) >= 9 and cardPos9.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 9
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 10 and cardPos10.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 10
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 11:
                    if len(handList) == 11:
                        if Rect(cardPos11.x + 44, cardPos11.y, cardPos11.w, cardPos11.h).collidepoint(mX, mY):
                            inputType = 0
                            handSelect = 11
                            ListInit(handSelect)
                            handList[handSelect-1] = 1
                            mouseInButton = True
                    else:
                        if cardPos11.collidepoint(mX, mY):
                            inputType = 0
                            handSelect = 11
                            ListInit(handSelect)
                            handList[handSelect-1] = 1
                            mouseInButton = True
                if len(handList) >= 12 and cardPos12.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 12
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 13 and cardPos13.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 13
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                if len(handList) >= 14 and cardPos14.collidepoint(mX, mY):
                    inputType = 0
                    handSelect = 14
                    ListInit(handSelect)
                    handList[handSelect-1] = 1
                    mouseInButton = True
                        
            ##########Action##########
            if len(actionList) != 0:
                if f7Button.collidepoint(mX, mY):
                    if ('kan' in actionList) == True:
                        inputType = 1
                        actionSelect = actionList.index('kan')
                        if mouseInButton == True:
                            mouseInButton = False
                        mouseInButton_a = True

                elif f8Button.collidepoint(mX, mY):
                    if ('tsumo' in actionList) == True:
                        inputType = 1
                        actionSelect = actionList.index('tsumo')
                        if mouseInButton == True:
                            mouseInButton = False
                        mouseInButton_a = True

                elif f9Button.collidepoint(mX, mY):
                    if ('riichi' in actionList) == True:
                        inputType = 1
                        actionSelect = actionList.index('riichi')
                        if mouseInButton == True:
                            mouseInButton = False
                        mouseInButton_a = True
                    elif ('no' in actionList) == True:
                        inputType = 1
                        actionSelect = actionList.index('no')
                        if mouseInButton == True:
                            mouseInButton = False
                        mouseInButton_a = True
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                if mouseInButton == True:
                    handList[handSelect-1] = 2
                elif mouseInButton_a == True:
                    DoAction(SCREEN, actionList[actionSelect], 'p1')
            mouseInButton = False
            mouseInButton_a = False
        ##########keyboard##########
        if not hasattr(event, 'key'):
            continue
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                GameExit()
                return True

            if len(actionList) != 0:
                if p1Info['riichi'] == 0:
                    if event.key == K_UP:
                        if inputType == 0:
                            inputType = 1
                    elif event.key == K_DOWN:
                        if inputType == 1:
                            inputType = 0
                else:
                    inputType = 1

                ##########Action##########
                if inputType == 1:
                    if event.key == K_LEFT:
                        actionSelect -= 1
                        if actionSelect == -1:
                            actionSelect = len(actionList) - 1
                    elif event.key == K_RIGHT:
                        actionSelect += 1
                        if actionSelect == len(actionList):
                            actionSelect = 0
                    elif event.key == K_RETURN:
                        DoAction(SCREEN, actionList[actionSelect], 'p1')

                if event.key == K_F7:
                    if ('kan' in actionList) == True:
                        if inputType == 1 and actionSelect == actionList.index('kan'):
                            DoAction(SCREEN, 'kan', 'p1')
                        else:
                            inputType = 1
                            actionSelect = actionList.index('kan')
                elif event.key == K_F8:
                    if ('tsumo' in actionList) == True:
                        if inputType == 1 and actionSelect == actionList.index('tsumo'):
                            DoAction(SCREEN, 'tsumo', 'p1')
                        else:
                            inputType = 1
                            actionSelect = actionList.index('tsumo')
                elif event.key == K_F9:
                    if ('riichi' in actionList) == True:
                        if inputType == 1 and actionSelect == actionList.index('riichi'):
                            DoAction(SCREEN, 'riichi', 'p1')
                        else:
                            inputType = 1
                            actionSelect = actionList.index('riichi')
                    elif ('no' in actionList) == True:
                        if inputType == 1 and actionSelect == actionList.index('no'):
                            DoAction(SCREEN, 'no', 'p1')
                        else:
                            inputType = 1
                            actionSelect = actionList.index('no')
            

            if p1Info['riichi'] >= 1:
                break
            if event.key == K_1:
                if len(handList) >= 1:
                    handSelect = 1
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_2:
                if len(handList) >= 2:
                    handSelect = 2
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_3:
                if len(handList) >= 3:
                    handSelect = 3
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_4:
                if len(handList) >= 4:
                    handSelect = 4
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_5:
                if len(handList) >= 5:
                    handSelect = 5
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_6:
                if len(handList) >= 6:
                    handSelect = 6
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_7:
                if len(handList) >= 7:
                    handSelect = 7
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_8:
                if len(handList) >= 8:
                    handSelect = 8
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_9:
                if len(handList) >= 9:
                    handSelect = 9
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_0:
                if len(handList) >= 10:
                    handSelect = 10
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_MINUS:
                if len(handList) >= 11:
                    handSelect = 11
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_EQUALS:
                if len(handList) >= 12:
                    handSelect = 12
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_BACKSLASH:
                if len(handList) >= 13:
                    handSelect = 13
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2
            elif event.key == K_BACKSPACE:
                if len(handList) >= 14:
                    handSelect = 14
                    ListInit(handSelect)
                    if inputType == 1 or handList[handSelect-1] == 0:
                        inputType = 0
                        handList[handSelect-1] = 1
                    elif inputType == 0 and handList[handSelect-1] == 1:
                        handList[handSelect-1] = 2

                        
            if inputType == 1:
                break
            ##########Hand##########
            if event.key == K_LEFT:
                if handSelect > 1:
                    handList[handSelect-1] = 0
                    handSelect -= 1
                    handList[handSelect-1] = 1
                elif handSelect == 1:
                    handList[handSelect-1] = 0
                    handSelect = len(handList)
                    handList[handSelect-1] = 1
                elif handSelect == 0:
                    handSelect = len(handList)
                    handList[handSelect-1] = 1
            elif event.key == K_RIGHT:
                if handSelect < len(handList):
                    if handSelect != 0:
                        handList[handSelect-1] = 0
                    handSelect += 1
                    handList[handSelect-1] = 1
                elif handSelect == len(handList):
                    handList[handSelect-1] = 0
                    handSelect = 1
                    handList[handSelect-1] = 1
            elif event.key == K_RETURN:
                if 1 <= handSelect and handSelect <= len(handList):
                    handList[handSelect-1] = 2

################################################################################



############################## GAME ##############################

def playTurn(SCREEN, player):
    global cardList, gameInfo
    global p1Info
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Discard, p2Discard, p3Discard, p4Discard
    global playerTurnPre, turnEnd

    
    if player == 'p1':
        if len(p1Hand) % 3 != 2:
            pygame.time.wait(300)
            playerTurnPre = True

            
        if playerTurnPre == True:
            playerTurnPre = False
            p1Hand.append(cardList.pop(0))
            handList.append(0)
            gameInfo['rest'] -= 1
            gameInfo['count'] += 1
            p1Info['shanten'] = HandCheck(p1Hand, p1Info, 'shanten')
            CanAction('p1')
        


        if p1Info['riichi'] == 0 or len(p1Info['canAction']) != 0:
            if KeyInput(SCREEN) == True:
                return 'exit'
        else:
            pygame.event.pump()
            GameScreen(SCREEN)
            pygame.display.flip()
            pygame.time.wait(500)
            handList.pop()
            ListInit()
            if p1Info['riichi'] == 2:
                p1Discard.append(p1Hand.pop(-1) + 'riichi')
                p1Info['riichi'] = 1
            else:
                p1Discard.append(p1Hand.pop(-1))

            gameInfo['turn'] = 'p1End'

        
        CardCheck()
    


            

    elif player == 'p1End':
        if turnEnd == False:
            turnEnd = True
            ResetAction('p1')
            if CanHuro('p1', p1Discard[-1]) == False:
                gameInfo['turn'] = 'p2'
                turnEnd = False
        else:
            turnEnd = False
            Decision(SCREEN, 'p1')

    
    elif player == 'p2':
        pygame.time.wait(500)

        if len(p2Hand) % 3 != 2:
            p2Hand.append(cardList.pop(0))
            gameInfo['rest'] -= 1
            gameInfo['count'] += 1
            
            GameScreen(SCREEN)
            pygame.display.flip()
            pygame.time.wait(500)
            
            p2Discard.append(p2Hand.pop())

        gameInfo['turn'] = 'p2End'
        

    elif player == 'p2End':
        if turnEnd == False:
            turnEnd = True
            if CanHuro('p2', p2Discard[-1]) == False:
                gameInfo['turn'] = 'p3'
                turnEnd = False
        else:
            turnEnd = False
            Decision(SCREEN, 'p2')
        
        
    elif player == 'p3':
        pygame.time.wait(500)

        if len(p3Hand) % 3 != 2:
            p3Hand.append(cardList.pop(0))
            gameInfo['rest'] -= 1
            gameInfo['count'] += 1

            GameScreen(SCREEN)
            pygame.display.flip()
            pygame.time.wait(500)
            
            p3Discard.append(p3Hand.pop())

        gameInfo['turn'] = 'p3End'


    elif player == 'p3End':
        if turnEnd == False:
            turnEnd = True
            if CanHuro('p3', p3Discard[-1]) == False:
                gameInfo['turn'] = 'p4'
                turnEnd = False
        else:
            turnEnd = False
            Decision(SCREEN, 'p3')
        
        
    elif player == 'p4':
        pygame.time.wait(500)

        if len(p4Hand) % 3 != 2:
            p4Hand.append(cardList.pop(0))
            gameInfo['rest'] -= 1
            gameInfo['count'] += 1

            GameScreen(SCREEN)
            pygame.display.flip()
            pygame.time.wait(500)
            
            p4Discard.append(p4Hand.pop())
            
        gameInfo['turn'] = 'p4End'


    elif player == 'p4End':
        if turnEnd == False:
            turnEnd = True
            if CanHuro('p4', p4Discard[-1]) == False:
                gameInfo['turn'] = 'p1'
                turnEnd = False
        else:
            turnEnd = False
            Decision(SCREEN, 'p4')



    return ''




def CardCheck():
    global handList, p1Hand, p1Discard
    global gameInfo
    
    for i in range(len(handList)):
        if handList[i] == 2:
            handList.pop()
            ListInit()
            p1Discard.append(p1Hand.pop(i))
            p1Hand = CardSort(p1Hand).copy()
            gameInfo['turn'] = 'p1End'
            break

##################################################################



############################## GAME END ##############################

def IsGameEnd(SCREEN):
    #유국, 게임종료 판별
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global gameRestart


    windList = ['east', 'south', 'west', 'north']


    if p1Info['score'] <= 0 or p2Info['score'] <= 0 or p3Info['score'] <= 0 or p4Info['score'] <= 0:
        GameEnd(SCREEN)
        return True

    
    if gameInfo['turn'][:3] == 'end':
        if eval(gameInfo['turn'][-2:] + 'Info')['wind'] == 'east':
            PrintScoreTotal(SCREEN)
            gameInfo['turn'] = gameInfo['turn'][-2:]
            gameInfo['renchan'] += 1
            PrintScoreTotal(SCREEN)
            gameRestart = True
        else:
            PrintScoreTotal(SCREEN)
            if KyokuExchange(SCREEN) == True:
                return True
            gameInfo['renchan'] = 0
            PrintScoreTotal(SCREEN)
            gameRestart = True


    #유국
    elif gameInfo['rest'] == 0:
        GameScreen(SCREEN)
        pygame.display.flip()

        
        isOyaTen = False
        tenList = [False, False, False, False]

        isP1Ten = False
        isP2Ten = False
        isP3Ten = False
        isP4Ten = False

        tenCount = 0
        
        if HandCheck(p1Hand, p1Info, 'shanten') == 0:
            if p1Info['wind'] == 'east':
                gameInfo['turn'] = 'p1'
                isOyaTen = True
            tenList[0] = True
            isP1Ten = True
            tenCount += 1
        if HandCheck(p2Hand, p2Info, 'shanten') == 0:
            if p2Info['wind'] == 'east':
                gameInfo['turn'] = 'p2'
                isOyaTen = True
            tenList[1] = True
            isP2Ten = True
            tenCount += 1
        if HandCheck(p3Hand, p3Info, 'shanten') == 0:
            if p3Info['wind'] == 'east':
                gameInfo['turn'] = 'p3'
                isOyaTen = True
            tenList[2] = True
            isP3Ten = True
            tenCount += 1
        if HandCheck(p4Hand, p4Info, 'shanten') == 0:
            if p4Info['wind'] == 'east':
                gameInfo['turn'] = 'p4'
                isOyaTen = True
            tenList[3] = True
            isP4Ten = True
            tenCount += 1

        
        if tenCount == 0:
            PrintScoreTotal(SCREEN, tenList)
            if KyokuExchange(SCREEN) == True:
                return True
            gameInfo['renchan'] = 0
            PrintScoreTotal(SCREEN)
            gameRestart = True

        else:
            PrintScoreTotal(SCREEN, tenList)
            
            if isP1Ten == False:
                p1Info['score'] -= 3000 // (4 - tenCount)
            if isP2Ten == False:
                p2Info['score'] -= 3000 // (4 - tenCount)
            if isP3Ten == False:
                p3Info['score'] -= 3000 // (4 - tenCount)
            if isP4Ten == False:
                p4Info['score'] -= 3000 // (4 - tenCount)

            for i in range(1, 5):
                if tenList[i - 1] == True:
                    eval('p' + str(i) + 'Info')['score'] += 3000 // tenCount

            if isOyaTen == True:
                gameInfo['renchan'] += 1
                PrintScoreTotal(SCREEN)
                gameRestart = True
            else:
                if KyokuExchange(SCREEN) == True:
                    return True
                gameInfo['renchan'] = 0
                PrintScoreTotal(SCREEN)
                gameRestart = True
            

    #사풍연타
    elif gameInfo['count'] == 4 and len(p1Discard) == 1 and len(p2Discard) == 1 and len(p3Discard) == 1 and len(p4Discard) == 1:
        if p1Discard[0] in windList and p1Discard[0] == p2Discard[0] == p3Discard[0] == p4Discard[0]:
            PrintScoreTotal(SCREEN)
            if KyokuExchange(SCREEN) == True:
                return True
            gameInfo['renchan'] += 1
            PrintScoreTotal(SCREEN)
            gameRestart = True

    #4깡
    elif (gameInfo['suukantsu'] == True and gameInfo['kan'] == 5) or (gameInfo['suukantsu'] == False and gameInfo['kan'] == 4):
        PrintScoreTotal(SCREEN)
        if KyokuExchange(SCREEN) == True:
            return True
        PrintScoreTotal(SCREEN)
        gameInfo['renchan'] += 1
        gameRestart = True

    #4인 리치
    elif p1Info['riichi'] >= 1 and p2Info['riichi'] >= 1 and p3Info['riichi'] >= 1 and p4Info['riichi'] >= 1:
        PrintScoreTotal(SCREEN)
        if KyokuExchange(SCREEN) == True:
            return True
        PrintScoreTotal(SCREEN)
        gameInfo['renchan'] += 1
        gameRestart = True

    #구종구패
    

    #트리플 론
    if gameInfo['turn'] == 'kyukoku':
        PrintScoreTotal(SCREEN)
        if KyokuExchange(SCREEN) == True:
            return True
        PrintScoreTotal(SCREEN)
        gameInfo['renchan'] += 1
        gameRestart = True

        
    return False



def GameExit():
    global gameStart

    SaveData()
    gameStart = False
    return



def GameEnd(SCREEN):
    global gameStart

    PrintScoreTotal(SCREEN, 'end')
    gameStart = False
    DataReset()



def KyokuExchange(SCREEN):
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    
    windList = ['east', 'south', 'west', 'north']
    
    if gameInfo['kyoku'][-1] == '4':
        if windList.index(gameInfo['kyoku'][:-1]) == windList.index(gameInfo['ba']):
            GameEnd(SCREEN)
            return True
        else:
            gameInfo['kyoku'] = windList[windList.index(gameInfo['kyoku'][:-1]) + 1] + '1'
                
            if windList.index(p1Info['wind']) - 1 == -1:
                p1Info['wind'] = 'north'
            else:
                p1Info['wind'] = windList[windList.index(p1Info['wind']) - 1]
                if p1Info['wind'] == 'east':
                    gameInfo['turn'] = 'p1'
            if windList.index(p2Info['wind']) - 1 == -1:
                p2Info['wind'] = 'north'
            else:
                p2Info['wind'] = windList[windList.index(p2Info['wind']) - 1]
                if p2Info['wind'] == 'east':
                    gameInfo['turn'] = 'p2'
            if windList.index(p3Info['wind']) - 1 == -1:
                p3Info['wind'] = 'north'
            else:
                p3Info['wind'] = windList[windList.index(p3Info['wind']) - 1]
                if p3Info['wind'] == 'east':
                    gameInfo['turn'] = 'p3'
            if windList.index(p4Info['wind']) - 1 == -1:
                p4Info['wind'] = 'north'
            else:
                p4Info['wind'] = windList[windList.index(p4Info['wind']) - 1]
                if p4Info['wind'] == 'east':
                    gameInfo['turn'] = 'p4'

    else:
        gameInfo['kyoku'] = gameInfo['kyoku'][:-1] + str(int(gameInfo['kyoku'][-1]) + 1)
            
        if windList.index(p1Info['wind']) - 1 == -1:
                p1Info['wind'] = 'north'
        else:
            p1Info['wind'] = windList[windList.index(p1Info['wind']) - 1]
            if p1Info['wind'] == 'east':
                gameInfo['turn'] = 'p1'
        if windList.index(p2Info['wind']) - 1 == -1:
            p2Info['wind'] = 'north'
        else:
            p2Info['wind'] = windList[windList.index(p2Info['wind']) - 1]
            if p2Info['wind'] == 'east':
                gameInfo['turn'] = 'p2'
        if windList.index(p3Info['wind']) - 1 == -1:
            p3Info['wind'] = 'north'
        else:
            p3Info['wind'] = windList[windList.index(p3Info['wind']) - 1]
            if p3Info['wind'] == 'east':
                gameInfo['turn'] = 'p3'
        if windList.index(p4Info['wind']) - 1 == -1:
            p4Info['wind'] = 'north'
        else:
            p4Info['wind'] = windList[windList.index(p4Info['wind']) - 1]
            if p4Info['wind'] == 'east':
                gameInfo['turn'] = 'p4'

######################################################################



############################## Huro ##############################

def CanHuro(player, discard):
    global gameInfo
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Info, p2Info, p3Info, p4Info
    global cardList

    
    Huro_Reset()

    playerList = ['p1', 'p2', 'p3', 'p4']
    playerList.pop(playerList.index(player))


    #론
    for i in range(3):
        if eval(playerList[i] + 'Info')['shanten'] == 0:
            playerHand = eval(playerList[i] + 'Hand').copy()
            playerHand.append(discard)
            if HandCheck(playerHand, eval(playerList[i] + 'Info'), 'shanten') == -1:
                playerYaku = YakuCheck(eval(playerList[i] + 'Hand'), eval(playerList[i] + 'Info'), gameInfo, cardList, discard)
                if playerYaku['fan'] != 0 or playerYaku['yakuman'] != 0:
                    eval(playerList[i] + 'Info')['canHuro'].append('ron')
    ################################################################################
    #후리텐
    ################################################################################

    #대명캉 + 퐁
    compareTile = discard
    for i in range(3):
        if eval(playerList[i] + 'Info')['riichi'] >= 1:
            continue
        count = 0
        for j in range(len(eval(playerList[i] + 'Hand'))):
            if compareTile[:2] == eval(playerList[i] + 'Hand')[j][:2]:
                count += 1
        if count >= 3:
            eval(playerList[i] + 'Info')['canHuro'].append('kan')
            eval(playerList[i] + 'Info')['canHuro'].append('pon')
        elif count >= 2:
            eval(playerList[i] + 'Info')['canHuro'].append('pon')

    
    #치
    if discard[1].isdigit() == True:
        chiPlayer = int(player[1]) + 1
        if chiPlayer == 5:
            chiPlayer = 1
        if eval('p' + str(chiPlayer) + 'Info')['riichi'] == 0:
            compareTile = discard
            tileList = [False, False, False, False]
            for i in range(len(eval('p' + str(chiPlayer) + 'Hand'))):
                if eval('p' + str(chiPlayer) + 'Hand')[i][1].isdigit() and eval('p' + str(chiPlayer) + 'Hand')[i][0] == compareTile[0]:
                    if int(compareTile[1]) == int(eval('p' + str(chiPlayer) + 'Hand')[i][1]) + 2:
                        tileList[0] = True
                    elif int(compareTile[1]) == int(eval('p' + str(chiPlayer) + 'Hand')[i][1]) + 1:
                         tileList[1] = True
                    elif int(compareTile[1]) == int(eval('p' + str(chiPlayer) + 'Hand')[i][1]) - 1:
                        tileList[2] = True
                    elif int(compareTile[1]) == int(eval('p' + str(chiPlayer) + 'Hand')[i][1]) - 2:
                        tileList[3] = True
            if (tileList[0] and tileList[1]) or (tileList[1] and tileList[2]) or (tileList[2] and tileList[3]):
                eval('p' + str(chiPlayer) + 'Info')['canHuro'].append('chi')


    count = 0
    for i in range(3):
        if len(eval(playerList[i] + 'Info')['canHuro']) == 0:
            count += 1
    if count == 3:
        Huro_Reset()
        return False
    else:
        return True


    
def Decision(SCREEN, player):
    global gameInfo
    global p1Select, p2Select, p3Select, p4Select
    global p1Discard, p2Discard, p3Discard, p4Discard

    
    if player != 'p1':
        if len(p1Info['canHuro']) != 0:
            p1Select = HuroKeyInput(SCREEN, player)
        else:
            p1Select = 'NO'
    else:
        p1Select = 'NO'

    if player != 'p2':
        if len(p2Info['canHuro']) != 0:
            #AI, 패 확인해서 론할지 울지 결정
            p2Select = 'NO' #AI 구현하면 삭제하기

        else:
            p2Select = 'NO'
    else:
        p2Select = 'NO'

    if player != 'p3':
        if len(p3Info['canHuro']) != 0:
            #AI, 패 확인해서 론할지 울지 결정
            p3Select = 'NO' #AI 구현하면 삭제하기

        else:
            p3Select = 'NO'
    else:
        p3Select = 'NO'

    if player != 'p4':
        if len(p4Info['canHuro']) != 0:
            #AI, 패 확인해서 론할지 울지 결정
            p4Select = 'NO' #AI 구현하면 삭제하기

        else:
            p4Select = 'NO'
    else:
        p4Select = 'NO'




    if p1Select == 'NO' and p2Select == 'NO' and p3Select == 'NO' and p4Select == 'NO':
        playerNum = int(player[1]) + 1
        if playerNum == 5:
            playerNum = 1
        gameInfo['turn'] = 'p' + str(playerNum)
        return

    else:
        gameInfo['count'] += 1
        if ('riichi' in eval(player + 'Discard')[-1]) == True:
            eval(player + 'Info')['riichi'] = 2
            
        huroList = [p1Select, p2Select, p3Select, p4Select]
        
        #론
        ronIndex = []
        for i in range(len(huroList)):
            if huroList[i] == 'ron':
                ronIndex.append(huroList.index('ron') + 1)
                
        if len(ronIndex) == 3:
            #유국
            gameInfo['turn'] = 'kyukyoku'
            Huro_Reset()
            return
        
        elif len(ronIndex) != 0:
            for i in range(len(ronIndex)):
                Huro_Ron(SCREEN, 'p' + str(ronIndex[i]), player, eval(player + 'Discard')[-1])
            Huro_Reset()
            return


        #울었을 때 사라지는 역들
        Huro_YakuDel()

        
        #캉
        for i in range(len(huroList)):
            if 'kan' in huroList:
                Huro_Kan('p' + str(huroList.index('kan') + 1), player)
                CanAction('p' + str(huroList.index('kan') + 1))
                if 'tsumo' in eval('p' + str(huroList.index('kan') + 1) + 'Info')['canAction']:
                    eval('p' + str(huroList.index('kan') + 1) + 'Info')['canAction'].pop(eval('p' + str(huroList.index('kan') + 1) + 'Info')['canAction'].index('tsumo'))
                eval('p' + str(huroList.index('kan') + 1) + 'Info')['shanten'] = HandCheck(eval('p' + str(huroList.index('kan') + 1) + 'Hand'), eval('p' + str(huroList.index('kan') + 1) + 'Info'), 'shanten')
                Huro_Reset()
                return

        #퐁
        for i in range(len(huroList)):
            if 'pon' in huroList:
                Huro_Pon(SCREEN, 'p' + str(huroList.index('pon') + 1), player)
                CanAction('p' + str(huroList.index('pon') + 1))
                if 'tsumo' in eval('p' + str(huroList.index('pon') + 1) + 'Info')['canAction']:
                    eval('p' + str(huroList.index('pon') + 1) + 'Info')['canAction'].pop(eval('p' + str(huroList.index('pon') + 1) + 'Info')['canAction'].index('tsumo'))
                eval('p' + str(huroList.index('pon') + 1) + 'Info')['shanten'] = HandCheck(eval('p' + str(huroList.index('pon') + 1) + 'Hand'), eval('p' + str(huroList.index('pon') + 1) + 'Info'), 'shanten')
                Huro_Reset()
                return

        #치
        for i in range(len(huroList)):
            if 'chi' in huroList:
                Huro_Chi(SCREEN, 'p' + str(huroList.index('chi') + 1), player)
                CanAction('p' + str(huroList.index('chi') + 1))
                if 'tsumo' in eval('p' + str(huroList.index('chi') + 1) + 'Info')['canAction']:
                    eval('p' + str(huroList.index('chi') + 1) + 'Info')['canAction'].pop(eval('p' + str(huroList.index('chi') + 1) + 'Info')['canAction'].index('tsumo'))
                eval('p' + str(huroList.index('chi') + 1) + 'Info')['shanten'] = HandCheck(eval('p' + str(huroList.index('chi') + 1) + 'Hand'), eval('p' + str(huroList.index('chi') + 1) + 'Info'), 'shanten')
                Huro_Reset()
                return
            


def Huro_TileMark(SCREEN, targetPlayer):
    global cutSize
    global p1Discard, p2Discard, p3Discard, p4Discard
    
    tilePos_x = eval(targetPlayer + 'DisPos')[0]
    tilePos_y = eval(targetPlayer + 'DisPos')[1]

    if targetPlayer == 'p1':
        indexNum = len(p1Discard) - 1

        tilePos_x += (indexNum % cutSize) * cardSize_p1.w
        for i in range((indexNum // cutSize) * cutSize, indexNum):
            if 'riichi' in p1Discard[i]:
                tilePos_x += cardSize_p1.h - cardSize_p1.w
        if 'riichi' in p1Discard[-1]:
            tilePos_x += cardSize_p1.h // 2
            tilePos_y += (indexNum // cutSize) * cardSize_p1.h + cardSize_p1.w // 2
        else:
            tilePos_x += cardSize_p1.w // 2
            tilePos_y += (indexNum // cutSize) * cardSize_p1.h + cardSize_p1.h // 2

    elif targetPlayer == 'p2':
        indexNum = len(p2Discard) - 1

        tilePos_x += cardSize_p2.w
        tilePos_y += cardSize_p2.h

        tilePos_y -= (indexNum % cutSize) * cardSize_p2.h
        for i in range((indexNum // cutSize) * cutSize, indexNum):
            if 'riichi' in p2Discard[i]:
                tilePos_y -= cardSize_p2.w - cardSize_p2.h
        if 'riichi' in p2Discard[-1]:
            tilePos_y -= cardSize_p2.w // 2
            tilePos_x += (indexNum // cutSize) * cardSize_p2.w - cardSize_p2.w + cardSize_p2.h // 2
        else:
            tilePos_y -= cardSize_p2.h // 2
            tilePos_x += (indexNum // cutSize) * cardSize_p2.w - cardSize_p2.w // 2

    elif targetPlayer == 'p3':
        indexNum = len(p3Discard) - 1

        tilePos_x += cardSize_p3.w

        tilePos_x -= (indexNum % cutSize) * cardSize_p3.w
        for i in range((indexNum // cutSize) * cutSize, indexNum):
            if 'riichi' in p3Discard[i]:
                tilePos_x -= cardSize_p3.h - cardSize_p3.w
        if 'riichi' in p3Discard[-1]:
            tilePos_x -= cardSize_p3.h // 2
            tilePos_y -= (indexNum // cutSize) * cardSize_p3.h - cardSize_p3.h + cardSize_p3.w // 2
        else:
            tilePos_x -= cardSize_p3.w // 2
            tilePos_y -= (indexNum // cutSize) * cardSize_p3.h - cardSize_p3.h // 2

    elif targetPlayer == 'p4':
        indexNum = len(p4Discard) - 1

        tilePos_y += (indexNum % cutSize) * cardSize_p4.h
        for i in range((indexNum // cutSize) * cutSize, indexNum):
            if 'riichi' in p4Discard[i]:
                tilePos_y += cardSize_p4.w - cardSize_p4.h
        if 'riichi' in p4Discard[-1]:
            tilePos_y += cardSize_p4.w // 2
            tilePos_x -= (indexNum // cutSize) * cardSize_p4.w - cardSize_p4.w + cardSize_p4.h // 2
        else:
            tilePos_y += cardSize_p4.h // 2
            tilePos_x -= (indexNum // cutSize) * cardSize_p4.w - cardSize_p4.w // 2


    radius = int(((cardSize_p1.w // 2)**2 + (cardSize_p1.h // 2)**2)**0.5) + 3


    for i in range(5):
        pygame.draw.circle(SCREEN, Color('red'), (tilePos_x, tilePos_y), radius + i, 1) 




def HuroKeyInput(SCREEN, targetPlayer):
    global p1Info
    global mouseInButton

    huroList = ['NO']
    if 'chi' in  p1Info['canHuro']:
        huroList.append('chi')
    if 'pon' in  p1Info['canHuro']:
        huroList.append('pon')
    if 'kan' in  p1Info['canHuro']:
        huroList.append('kan')
    if 'ron' in p1Info['canHuro']:
        huroList.append('ron')


    listNum = 0

    isInputDone = False
    while True:
        if isInputDone == True:
            return huroList[listNum]

        ##########Key Input##########
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                    
            ##########mouse##########
            if pygame.mouse.get_focused():
                mX, mY = pygame.mouse.get_pos()
                    
                if f5Button.collidepoint(mX, mY):
                    if 'chi' in huroList:
                        listNum = huroList.index('chi')
                        mouseInButton = True
                elif f6Button.collidepoint(mX, mY):
                    if 'pon' in huroList:
                        listNum = huroList.index('pon')
                        mouseInButton = True
                elif f7Button.collidepoint(mX, mY):
                    if 'kan' in huroList:
                        listNum = huroList.index('kan')
                        mouseInButton = True
                elif f8Button.collidepoint(mX, mY):
                    if 'ron' in huroList:
                        listNum = huroList.index('ron')
                        mouseInButton = True
                elif f9Button.collidepoint(mX, mY):
                    if 'NO' in huroList:
                        listNum = huroList.index('NO')
                        mouseInButton = True

                if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                    isInputDone = True
                mouseInButton = False
                    
            ##########keyboard##########
            if not hasattr(event, 'key'):
                continue
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    if listNum > 0:
                        listNum -= 1
                    else:
                        listNum = len(huroList) - 1
                elif event.key == K_RIGHT:
                    if listNum < len(huroList) - 1:
                        listNum += 1
                    else:
                        listNum = 0
                elif event.key == K_RETURN:
                    isInputDone = True
                elif event.key == K_F5:
                    if 'chi' in huroList:
                        if listNum == huroList.index('chi'):
                            isInputDone = True
                        else:
                            listNum = huroList.index('chi')
                elif event.key == K_F6:
                    if 'pon' in huroList:
                        if listNum == huroList.index('pon'):
                            isInputDone = True
                        else:
                            listNum = huroList.index('pon')
                elif event.key == K_F7:
                    if 'kan' in huroList:
                        if listNum == huroList.index('kan'):
                            isInputDone = True
                        else:
                            listNum = huroList.index('kan')
                elif event.key == K_F8:
                    if 'ron' in huroList:
                        if listNum == huroList.index('ron'):
                            isInputDone = True
                        else:
                            listNum = huroList.index('ron')
                elif event.key == K_F9:
                    if listNum == 0:
                        isInputDone = True
                    else:
                        listNum = 0



        GameScreen(SCREEN)


        Huro_TileMark(SCREEN, targetPlayer)

        
        if huroList[listNum] == 'NO':
            pygame.draw.rect(SCREEN, buttonColor_s, f9Button_s)
        pygame.draw.rect(SCREEN, buttonColor, f9Button)
        SCREEN.blit(textNo, (f9Button.x + 10, f9Button.y - 3))
        SCREEN.blit(textF9, (f9Button.x + 40, f9Button.y - f9Button.h))
            
        if 'ron' in huroList:
            if huroList[listNum] == 'ron':
                pygame.draw.rect(SCREEN, buttonColor_s, f8Button_s)
            pygame.draw.rect(SCREEN, buttonColor, f8Button)
            SCREEN.blit(textRon, (f8Button.x + 50, f8Button.y - 3))
            SCREEN.blit(textF8, (f8Button.x + 40, f8Button.y - f8Button.h))
                
        if 'kan' in huroList:
            if huroList[listNum] == 'kan':
                pygame.draw.rect(SCREEN, buttonColor_s, f7Button_s)
            pygame.draw.rect(SCREEN, buttonColor, f7Button)
            SCREEN.blit(textKan, (f7Button.x + 45, f7Button.y - 3))
            SCREEN.blit(textF7, (f7Button.x + 40, f7Button.y - f7Button.h))
                
        if 'pon' in huroList:
            if huroList[listNum] == 'pon':
                pygame.draw.rect(SCREEN, buttonColor_s, f6Button_s)
            pygame.draw.rect(SCREEN, buttonColor, f6Button)
            SCREEN.blit(textPon, (f6Button.x + 47, f6Button.y - 4))
            SCREEN.blit(textF6, (f6Button.x + 40, f6Button.y - f6Button.h))
                
        if 'chi' in huroList:
            if huroList[listNum] == 'chi':
                pygame.draw.rect(SCREEN, buttonColor_s, f5Button_s)
            pygame.draw.rect(SCREEN, buttonColor, f5Button)
            SCREEN.blit(textChi, (f5Button.x + 46, f5Button.y - 2))
            SCREEN.blit(textF5, (f5Button.x + 40, f5Button.y - f5Button.h))


        pygame.display.flip()
        clock.tick(TARGET_FPS)

    
        

def Huro_Chi(SCREEN, player, targetPlayer):
    global gameInfo
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Discard, p2Discard, p3Discard, p4Discard
    global handList, mouseInButton


    #1이 있고 4가 없으면 첫번째, 1이 없고 4가 있으면 2번째, 1,4가 둘다 있으면 3번째
    if player == 'p1':
        compareTile = eval(targetPlayer + 'Discard')[-1]
        chiTileList = [-1, -1, -1, -1]
        for i in range(len(p1Hand)):
            if p1Hand[i][1].isdigit() and p1Hand[i][0] == compareTile[0]:
                if int(compareTile[1]) == int(p1Hand[i][1]) + 2:
                    chiTileList[0] = i
                elif int(compareTile[1]) == int(p1Hand[i][1]) + 1:
                    chiTileList[1] = i
                elif int(compareTile[1]) == int(p1Hand[i][1]) - 1:
                    chiTileList[2] = i
                elif int(compareTile[1]) == int(p1Hand[i][1]) - 2:
                    chiTileList[3] = i

        count = 0
        for i in range(4):
            if chiTileList[i] != -1:
                count += 1

        if chiTileList[0] != -1 and chiTileList[1] != -1 and chiTileList[2] == -1:
            if targetPlayer == 'p2':
                p1Info['huro'].append([p1Hand[chiTileList[0]] + '1', p1Hand[chiTileList[1]] + '1', compareTile + '2'])
            elif targetPlayer == 'p3':
                p1Info['huro'].append([p1Hand[chiTileList[0]] + '1', compareTile + '3', p1Hand[chiTileList[1]] + '1'])
            elif targetPlayer == 'p4':
                p1Info['huro'].append([compareTile + '4', p1Hand[chiTileList[0]] + '1', p1Hand[chiTileList[1]] + '1'])

            eval(targetPlayer + 'Discard').pop(-1)
            p1Hand.pop(chiTileList[1])
            p1Hand.pop(chiTileList[0])
            handList.pop()
            handList.pop()
        elif chiTileList[0] == -1 and chiTileList[1] != -1 and chiTileList[2] != -1 and chiTileList[3] == -1:
            if targetPlayer == 'p2':
                p1Info['huro'].append([p1Hand[chiTileList[1]] + '1', p1Hand[chiTileList[2]] + '1', compareTile + '2'])
            elif targetPlayer == 'p3':
                p1Info['huro'].append([p1Hand[chiTileList[1]] + '1', compareTile + '3', p1Hand[chiTileList[2]] + '1'])
            elif targetPlayer == 'p4':
                p1Info['huro'].append([compareTile + '4', p1Hand[chiTileList[1]] + '1', p1Hand[chiTileList[2]] + '1'])

            eval(targetPlayer + 'Discard').pop(-1)
            p1Hand.pop(chiTileList[2])
            p1Hand.pop(chiTileList[1])
            handList.pop()
            handList.pop()
        elif chiTileList[1] == -1 and chiTileList[2] != -1 and chiTileList[3] != -1:
            if targetPlayer == 'p2':
                p1Info['huro'].append([p1Hand[chiTileList[2]] + '1', p1Hand[chiTileList[3]] + '1', compareTile + '2'])
            elif targetPlayer == 'p3':
                p1Info['huro'].append([p1Hand[chiTileList[2]] + '1', compareTile + '3', p1Hand[chiTileList[3]] + '1'])
            elif targetPlayer == 'p4':
                p1Info['huro'].append([compareTile + '4', p1Hand[chiTileList[2]] + '1', p1Hand[chiTileList[3]] + '1'])

            eval(targetPlayer + 'Discard').pop(-1)
            p1Hand.pop(chiTileList[3])
            p1Hand.pop(chiTileList[2])
            handList.pop()
            handList.pop()

        elif count >= 3:
            #사용자에게 어떤걸로 울건지 정함
            #12 3, 2 34, 12 34 만 있음
            #12 34라면 방향키로 움직여 12, 23, 34 3개만 고를수 있게함
            if chiTileList[0] != -1 and chiTileList[3] == -1:
                chiTileList.pop(3)
            elif chiTileList[0] == -1 and chiTileList[3] != -1:
                chiTileList.pop(0)

            ListInit()

            chiSelect = 1

            isInputDone = False
            while True:
                if isInputDone == True:
                    ListInit()
                    if chiSelect == 1:
                        if targetPlayer == 'p2':
                            p1Info['huro'].append([p1Hand[chiTileList[0]] + '1', p1Hand[chiTileList[1]] + '1', compareTile + '2'])
                        elif targetPlayer == 'p3':
                            p1Info['huro'].append([p1Hand[chiTileList[0]] + '1', compareTile + '3', p1Hand[chiTileList[1]] + '1'])
                        elif targetPlayer == 'p4':
                            p1Info['huro'].append([compareTile + '4', p1Hand[chiTileList[0]] + '1', p1Hand[chiTileList[1]] + '1'])

                        eval(targetPlayer + 'Discard').pop(-1)
                        p1Hand.pop(chiTileList[1])
                        p1Hand.pop(chiTileList[0])
                        handList.pop()
                        handList.pop()
                                
                    elif chiSelect == 2:
                        if targetPlayer == 'p2':
                            p1Info['huro'].append([p1Hand[chiTileList[1]] + '1', p1Hand[chiTileList[2]] + '1', compareTile + '2'])
                        elif targetPlayer == 'p3':
                            p1Info['huro'].append([p1Hand[chiTileList[1]] + '1', compareTile + '3', p1Hand[chiTileList[2]] + '1'])
                        elif targetPlayer == 'p4':
                            p1Info['huro'].append([compareTile + '4', p1Hand[chiTileList[2]] + '1', p1Hand[chiTileList[2]] + '1'])

                        eval(targetPlayer + 'Discard').pop(-1)
                        p1Hand.pop(chiTileList[2])
                        p1Hand.pop(chiTileList[1])
                        handList.pop()
                        handList.pop()
                                
                    elif chiSelect == 3:
                        if targetPlayer == 'p2':
                            p1Info['huro'].append([p1Hand[chiTileList[2]] + '1', p1Hand[chiTileList[3]] + '1', compareTile + '2'])
                        elif targetPlayer == 'p3':
                            p1Info['huro'].append([p1Hand[chiTileList[2]] + '1', compareTile + '3', p1Hand[chiTileList[3]] + '1'])
                        elif targetPlayer == 'p4':
                            p1Info['huro'].append([compareTile + '4', p1Hand[chiTileList[2]] + '1', p1Hand[chiTileList[3]] + '1'])

                        eval(targetPlayer + 'Discard').pop(-1)
                        p1Hand.pop(chiTileList[3])
                        p1Hand.pop(chiTileList[2])
                        handList.pop()
                        handList.pop()
                    
                    break
                
                if chiSelect == 1:
                    ListInit()
                    handList[chiTileList[0]] = 1
                    handList[chiTileList[1]] = 1
                elif chiSelect == 2:
                    ListInit()
                    handList[chiTileList[1]] = 1
                    handList[chiTileList[2]] = 1
                elif chiSelect == 3:
                    ListInit()
                    handList[chiTileList[2]] = 1
                    handList[chiTileList[3]] = 1

                ##########Key Input##########
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    ##########mouse##########
                    if pygame.mouse.get_focused():
                        mX, mY = pygame.mouse.get_pos()
                        
                        if eval('cardPos' + str(chiTileList[0] + 1)).collidepoint(mX, mY):
                            chiSelect = 1
                            mouseInButton = True
                        elif len(chiTileList) == 3 and eval('cardPos' + str(chiTileList[1] + 1)).collidepoint(mX, mY) or eval('cardPos' + str(chiTileList[2] + 1)).collidepoint(mX, mY):
                            chiSelect = 2
                            mouseInButton = True
                        elif len(chiTileList) == 4:
                            if eval('cardPos' + str(chiTileList[1] + 1)).collidepoint(mX, mY):
                                chiSelect = 2
                                mouseInButton = True
                            elif eval('cardPos' + str(chiTileList[2] + 1)).collidepoint(mX, mY) or eval('cardPos' + str(chiTileList[3] + 1)).collidepoint(mX, mY):
                                chiSelect = 3
                                mouseInButton = True
                        
                        if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                            isInputDone = True
                        mouseInButton = False
                    
                    ##########keyboard##########
                    if not hasattr(event, 'key'):
                        continue
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            if chiSelect > 1:
                                chiSelect -= 1
                        elif event.key == K_RIGHT:
                            if chiSelect < len(chiTileList) - 1:
                                chiSelect += 1
                        elif event.key == K_RETURN:
                            isInputDone = True
                        elif event.key == K_F1:
                            if chiSelect == 1:
                                isInputDone = True
                            else:
                                chiSelect = 1
                        elif event.key == K_F2:
                            if chiSelect == 2:
                                isInputDone = True
                            else:
                                chiSelect = 2
                        elif event.key == K_F3:
                            if len(chiTileList) == 4:
                                if chiSelect == 3:
                                    isInputDone = True
                                else:
                                    chiSelect = 3
                            
                    
                GameScreen(SCREEN, 'clear')

                Huro_TileMark(SCREEN, targetPlayer)
                
                pointList = [[((p1HandPos[0]//2)*3 + 6 + (cardSize.w * chiTileList[0]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * chiTileList[0]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * chiTileList[0]), p1HandPos[1] - 6)],
                             [((p1HandPos[0]//2)*3 + 6 + (cardSize.w * chiTileList[1]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * chiTileList[1]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * chiTileList[1]), p1HandPos[1] - 6)],
                             [((p1HandPos[0]//2)*3 + 6 + (cardSize.w * chiTileList[2]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * chiTileList[2]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * chiTileList[2]), p1HandPos[1] - 6)]]
                if len(chiTileList) == 4:
                    pointList.append([((p1HandPos[0]//2)*3 + 6 + (cardSize.w * chiTileList[3]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * chiTileList[3]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * chiTileList[3]), p1HandPos[1] - 6)])
                for i in range(len(chiTileList)):
                    pygame.draw.polygon(SCREEN, Color('red'), pointList[i])
                    if i == len(chiTileList) - 1:
                        SCREEN.blit(eval('textF' + str(i)), ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * chiTileList[i]), p1HandPos[1] - 50))
                    else:
                        SCREEN.blit(eval('textF' + str(i+1)), ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * chiTileList[i]), p1HandPos[1] - 50))


                pygame.display.flip()
                clock.tick(TARGET_FPS)

                
        
            
    else:
        ''

    gameInfo['turn'] = player




def Huro_Pon(SCREEN, player, targetPlayer):
    global gameInfo
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Discard, p2Discard, p3Discard, p4Discard
    global handList, mouseInButton

    if player == 'p1':
        #패에 똑같은게 3개면 선택, 2개면 바로 퐁
        compareTile = eval(targetPlayer + 'Discard')[-1]
        ponIndexList = []
        redDoraIndex = -1
        for i in range(len(p1Hand)):
            if compareTile[:2] == p1Hand[i][:2]:
                if len(p1Hand[i]) >= 3 and p1Hand[i][1] == '5' and p1Hand[i][2] == 'r':
                    redDoraIndex = i
                else:
                    ponIndexList.append(i)
                
        if redDoraIndex == -1 or (len(ponIndexList) == 1 and redDoraIndex != -1):
            if redDoraIndex != -1:
                ponIndexList.append(redDoraIndex)
            if targetPlayer == 'p2':
                p1Info['huro'].append([p1Hand[ponIndexList[-2]] + '1', p1Hand[ponIndexList[-1]] + '1', compareTile + '2'])
            elif targetPlayer == 'p3':
                p1Info['huro'].append([p1Hand[ponIndexList[-2]] + '1', compareTile + '3', p1Hand[ponIndexList[-1]] + '1'])
            elif targetPlayer == 'p4':
                p1Info['huro'].append([compareTile + '4', p1Hand[ponIndexList[-2]] + '1', p1Hand[ponIndexList[-1]] + '1'])

            eval(targetPlayer + 'Discard').pop(-1)
            for i in ponIndexList[-1:-3:-1]:
                p1Hand.pop(i)
                handList.pop()
                
        elif len(ponIndexList) == 2 and redDoraIndex != -1:
            #적도라가 있고 패가 3개면 사용자가 선택
            ponIndexList.append(redDoraIndex)
            ListInit()

            ponSelect = 1

            isInputDone = False
            while True:
                if isInputDone == True:
                    ListInit()
                    if ponSelect == 1:
                        if targetPlayer == 'p2':
                            p1Info['huro'].append([p1Hand[ponIndexList[0]] + '1', p1Hand[ponIndexList[1]] + '1', compareTile + '2'])
                        elif targetPlayer == 'p3':
                            p1Info['huro'].append([p1Hand[ponIndexList[0]] + '1', compareTile + '3', p1Hand[ponIndexList[1]] + '1'])
                        elif targetPlayer == 'p4':
                            p1Info['huro'].append([compareTile + '4', p1Hand[ponIndexList[0]] + '1', p1Hand[ponIndexList[1]] + '1'])

                        eval(targetPlayer + 'Discard').pop(-1)
                        p1Hand.pop(ponIndexList[1])
                        p1Hand.pop(ponIndexList[0])
                        handList.pop()
                        handList.pop()
                                
                    elif chiSelect == 2:
                        if targetPlayer == 'p2':
                            p1Info['huro'].append([p1Hand[ponIndexList[1]] + '1', p1Hand[ponIndexList[2]] + '1', compareTile + '2'])
                        elif targetPlayer == 'p3':
                            p1Info['huro'].append([p1Hand[ponIndexList[1]] + '1', compareTile + '3', p1Hand[ponIndexList[2]] + '1'])
                        elif targetPlayer == 'p4':
                            p1Info['huro'].append([compareTile + '4', p1Hand[ponIndexList[2]] + '1', p1Hand[ponIndexList[2]] + '1'])

                        eval(targetPlayer + 'Discard').pop(-1)
                        p1Hand.pop(ponIndexList[2])
                        p1Hand.pop(ponIndexList[1])
                        handList.pop()
                        handList.pop()
                                
                    break

                if ponSelect == 1:
                    ListInit()
                    handList[ponIndexList[0]] = 1
                    handList[ponIndexList[1]] = 1
                elif ponSelect == 2:
                    ListInit()
                    handList[ponIndexList[1]] = 1
                    handList[ponIndexList[2]] = 1

                ##########Key Input##########
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    ##########mouse##########
                    if pygame.mouse.get_focused():
                        mX, mY = pygame.mouse.get_pos()
                        
                        if eval('cardPos' + str(ponIndexList[0] + 1)).collidepoint(mX, mY) or eval('cardPos' + str(ponIndexList[1] + 1)).collidepoint(mX, mY):
                            ponSelect = 1
                            mouseInButton = True
                        elif eval('cardPos' + str(ponIndexList[2] + 1)).collidepoint(mX, mY):
                            ponSelect = 2
                            mouseInButton = True
                        
                        if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                            isInputDone = True
                        mouseInButton = False
                    
                    ##########keyboard##########
                    if not hasattr(event, 'key'):
                        continue
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            if ponSelect > 1:
                                ponSelect -= 1
                        elif event.key == K_RIGHT:
                            if ponSelect < 2:
                                ponSelect += 1
                        elif event.key == K_RETURN:
                            isInputDone = True
                        elif event.key == K_F1:
                            if ponSelect == 1:
                                isInputDone = True
                            else:
                                ponSelect = 1
                        elif event.key == K_F2:
                            if ponSelect == 2:
                                isInputDone = True
                            else:
                                ponSelect = 2
                            
                    
                GameScreen(SCREEN, 'clear')

                Huro_TileMark(SCREEN, targetPlayer)

                pointList = [[((p1HandPos[0]//2)*3 + 6 + (cardSize.w * ponIndexList[0]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * ponIndexList[0]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * ponIndexList[0]), p1HandPos[1] - 6)],
                             [((p1HandPos[0]//2)*3 + 6 + (cardSize.w * ponIndexList[1]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * ponIndexList[1]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * ponIndexList[1]), p1HandPos[1] - 6)],
                             [((p1HandPos[0]//2)*3 + 6 + (cardSize.w * ponIndexList[2]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * ponIndexList[2]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * ponIndexList[2]), p1HandPos[1] - 6)]]
                for i in range(3):
                    pygame.draw.polygon(SCREEN, Color('red'), pointList[i])
                SCREEN.blit(textF1, ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * ponIndexList[0]), p1HandPos[1] - 50))
                SCREEN.blit(textF1, ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * ponIndexList[1]), p1HandPos[1] - 50))
                SCREEN.blit(textF2, ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * ponIndexList[2]), p1HandPos[1] - 50))


                pygame.display.flip()
                clock.tick(TARGET_FPS)

            

            
    else:
        ''

    gameInfo['turn'] = player
    


def Huro_Kan(player, targetPlayer):
    global gameInfo
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Info, p2Info, p3Info, p4Info
    global p1Discard, p2Discard, p3Discard, p4Discard
    global handList, cardList


    compareTile = eval(targetPlayer + 'Discard')[-1]
    kanIndexList = []
    for i in range(len(eval(player + 'Hand'))):
        if compareTile[:2] == p1Hand[i][:2]:
            kanIndexList.append(i)
            
    if int(targetPlayer[1]) == int(player[1]) + 1 or int(targetPlayer[1]) == (int(player[1]) + 1) % 4:
        eval(player + 'Info')['huro'].append([compareTile + '1', compareTile + '1', compareTile + '1', compareTile + '2'])
    elif int(targetPlayer[1]) == int(player[1]) + 2 or int(targetPlayer[1]) == (int(player[1]) + 2) % 4:
        eval(player + 'Info')['huro'].append([compareTile + '1', compareTile + '3', compareTile + '1', compareTile + '1'])
    elif int(targetPlayer[1]) == int(player[1]) + 3 or int(targetPlayer[1]) == (int(player[1]) + 3) % 4:
        eval(player + 'Info')['huro'].append([compareTile + '4', compareTile + '1', compareTile + '1', compareTile + '1'])

    eval(targetPlayer + 'Discard').pop(-1)
    for i in kanIndexList[::-1]:
        eval(player + 'Hand').pop(i)
        if player == 'p1':
            handList.pop()

    eval(player + 'Hand').append(cardList.pop(-1))
    if player == 'p1':
        handList.append(0)

    gameInfo['kan'] += 1
    if gameInfo['kan'] == 4:
        if len(HandCheck(eval(player + 'Hand'), eval(player + 'Info'), 'huro')['kantsu']) == 4:
            gameInfo['suukantsu'] = True

    eval(player + 'Info')['rinshan'] = True

    gameInfo['turn'] = player
    
    


def Huro_Ron(SCREEN, player, *target):
    global gameInfo, cardList
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Discard, p2Discard, p3Discard, p4Discard

    yaku = YakuCheck(eval(player + 'Hand'), eval(player + 'Info'), gameInfo, cardList, target[1])

    pygame.time.wait(500)
    
    ScoreCalculate(SCREEN, yaku, player, target[0], target[1])
    
    gameInfo['turn'] = 'end' + player
    return



def Huro_YakuDel():
    global p1Info, p2Info, p3Info, p4Info

    #울었을때
    for i in range(1, 5):
        eval('p' + str(i) + 'Info')['hou'] = False
        eval('p' + str(i) + 'Info')['ippatsu'] = 0
        eval('p' + str(i) + 'Info')['doubleriichi'] = -1
        eval('p' + str(i) + 'Info')['rinshan'] = False

        

def Huro_Reset():
    global p1Info, p2Info, p3Info, p4Info

    p1Info['canHuro'] = []
    p2Info['canHuro'] = []
    p3Info['canHuro'] = []
    p4Info['canHuro'] = []
    
##################################################################



############################## Action ##############################

def CanAction(player):
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Info, p2Info, p3Info, p4Info

    
    shanten = HandCheck(eval(player + 'Hand'), eval(player + 'Info'), 'shanten')
    
    #쯔모
    if shanten == -1:
        playerYaku = YakuCheck(eval(player + 'Hand'), eval(player + 'Info'), gameInfo, cardList)
        if playerYaku['fan'] != 0 or playerYaku['yakuman'] != 0:
            eval(player + 'Info')['canAction'].append('tsumo')


    #리치
    if shanten == 0 and eval(player + 'Info')['riichi'] == 0:
        huro = False
        if len(eval(player + 'Info')['huro']) != 0:
            for i in range(len(eval(player + 'Info')['huro'])):
                if len(eval(player + 'Info')['huro'][i]) != 4:
                    huro = True
                    break
                else:
                    for j in range(4):
                        if eval(player + 'Info')['huro'][i][j][-1] != '1':
                            huro = True
                            break
                if huro == True:
                    break

        if huro == False:
            eval(player + 'Info')['canAction'].append('riichi')


    #암캉
    for i in range(len(eval(player + 'Hand')) - 3):
        count = 0
        compareTile = eval(player + 'Hand')[i]
        for j in range(i + 1, len(eval(player + 'Hand'))):
            if eval(player + 'Hand')[j] == compareTile:
                count += 1
        if count == 3:
            eval(player + 'Info')['canAction'].append('kan')
            if eval(player + 'Info')['riichi'] >= 1:
                eval(player + 'Info')['canAction'].append('no')
            return


    #가깡
    huroList = HandCheck([], eval(player + 'Info'), 'huro')
    if len(huroList['koutsu']) != 0:
        for i in range(len(huroList['koutsu'])):
            for j in range(len(eval(player + 'Hand'))):
                if huroList['koutsu'][i][0][:2] == eval(player + 'Hand')[j][:2]:
                    eval(player + 'Info')['canAction'].append('kan')
                    return



def DoAction(SCREEN, actionType, player):

    ResetAction(player, 'clear')

    if actionType == 'riichi':
        Action_Riichi(SCREEN, player)
    elif actionType == 'tsumo':
        Action_Tsumo(SCREEN, player)
    elif actionType == 'kan':
        Action_Kan(SCREEN, player)
    elif actionType == 'no':
        return

    CanAction(player)
    eval(player + 'Info')['shanten'] = HandCheck(eval(player + 'Hand'), eval(player + 'Info'), 'shanten')




def Action_Riichi(SCREEN, player):
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global p1Hand, p2Hand, p3Hand, p4Hand
    global handList, mouseInButton

    eval(player + 'Info')['riichi'] = 2
    eval(player + 'Info')['ippatsu'] = 2
    if eval(player + 'Info')['doubleriichi'] == 0:
        if gameInfo['count'] <= 4:
            eval(player + 'Info')['doubleriichi'] = 1
        else:
            eval(player + 'Info')['doubleriichi'] = -1

    #버릴 패 고르기
    riichiList = []
    for i in range(len(eval(player + 'Hand'))):
        hList = eval(player + 'Hand').copy()
        hList.pop(i)
        if HandCheck(hList, eval(player + 'Info'), 'shanten') == 0:
            riichiList.append(i)


    if player == 'p1':
        if len(riichiList) == 1:
            handList.pop()
            ListInit()
            p1Discard.append(p1Hand.pop(riichiList[0]) + 'riichi')
            p1Hand = CardSort(p1Hand).copy()
            p1Info['riichi'] = 1
            gameInfo['turn'] = 'p1End'
        else:
            riichiSelect = 0
            isInputDone = False
            while True:
                if isInputDone == True:
                    handList.pop()
                    ListInit()
                    p1Discard.append(p1Hand.pop(riichiList[riichiSelect - 1]) + 'riichi')
                    p1Hand = CardSort(p1Hand).copy()
                    p1Info['riichi'] = 1
                    gameInfo['turn'] = 'p1End'
                    return

                ListInit()
                handList[riichiList[riichiSelect - 1]] = 1

                ##########Key Input##########
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    ##########mouse##########
                    if pygame.mouse.get_focused():
                        mX, mY = pygame.mouse.get_pos()
                        
                        if eval('cardPos' + str(riichiList[0] + 1)).collidepoint(mX, mY):
                            riichiSelect = 1
                            mouseInButton = True
                        if eval('cardPos' + str(riichiList[1] + 1)).collidepoint(mX, mY):
                            riichiSelect = 2
                            mouseInButton = True
                        if len(riichiList) >= 3:
                            if eval('cardPos' + str(riichiList[2] + 1)).collidepoint(mX, mY):
                                riichiSelect = 3
                                mouseInButton = True
                        if len(riichiList) >= 4:
                            if eval('cardPos' + str(riichiList[3] + 1)).collidepoint(mX, mY):
                                riichiSelect = 4
                                mouseInButton = True
                        if len(riichiList) >= 5:
                            if eval('cardPos' + str(riichiList[4] + 1)).collidepoint(mX, mY):
                                riichiSelect = 5
                                mouseInButton = True
                        if len(riichiList) >= 6:
                            if eval('cardPos' + str(riichiList[5] + 1)).collidepoint(mX, mY):
                                riichiSelect = 6
                                mouseInButton = True
                        if len(riichiList) >= 7:
                            if eval('cardPos' + str(riichiList[6] + 1)).collidepoint(mX, mY):
                                riichiSelect = 7
                                mouseInButton = True
                        if len(riichiList) >= 8:
                            if eval('cardPos' + str(riichiList[7] + 1)).collidepoint(mX, mY):
                                riichiSelect = 8
                                mouseInButton = True
                        if len(riichiList) >= 9:
                            if eval('cardPos' + str(riichiList[8] + 1)).collidepoint(mX, mY):
                                riichiSelect = 9
                                mouseInButton = True
                        if len(riichiList) >= 10:
                            if eval('cardPos' + str(riichiList[9] + 1)).collidepoint(mX, mY):
                                riichiSelect = 10
                                mouseInButton = True
                        if len(riichiList) >= 11:
                            if eval('cardPos' + str(riichiList[10] + 1)).collidepoint(mX, mY):
                                riichiSelect = 11
                                mouseInButton = True
                        if len(riichiList) >= 12:
                            if eval('cardPos' + str(riichiList[11] + 1)).collidepoint(mX, mY):
                                riichiSelect = 12
                                mouseInButton = True
                        if len(riichiList) >= 13:
                            if eval('cardPos' + str(riichiList[12] + 1)).collidepoint(mX, mY):
                                riichiSelect = 13
                                mouseInButton = True
                        if len(riichiList) >= 14:
                            if eval('cardPos' + str(riichiList[13] + 1)).collidepoint(mX, mY):
                                riichiSelect = 14
                                mouseInButton = True
                        
                        if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                            isInputDone = True
                        mouseInButton = False
                    
                    ##########keyboard##########
                    if not hasattr(event, 'key'):
                        continue
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            riichiSelect -= 1
                            if riichiSelect == 0:
                                riichiSelect = len(riichiList)
                            elif riichiSelect == -1:
                                riichiSelect = len(riichiList)
                        elif event.key == K_RIGHT:
                            riichiSelect += 1
                            if riichiSelect == len(riichiList) + 1:
                                riichiSelect = 1
                        elif event.key == K_RETURN:
                            isInputDone = True
                        elif event.key == K_1:
                            if riichiSelect == 1:
                                isInputDone = True
                            else:
                                riichiSelect = 1
                        elif event.key == K_2:
                            if riichiSelect == 2:
                                isInputDone = True
                            else:
                                riichiSelect = 2
                        elif event.key == K_3:
                            if len(riichiList) >= 3:
                                if riichiSelect == 3:
                                    isInputDone = True
                                else:
                                    riichiSelect = 3
                        elif event.key == K_4:
                            if len(riichiList) >= 4:
                                if riichiSelect == 4:
                                    isInputDone = True
                                else:
                                    riichiSelect = 4
                        elif event.key == K_5:
                            if len(riichiList) >= 5:
                                if riichiSelect == 5:
                                    isInputDone = True
                                else:
                                    riichiSelect = 5
                        elif event.key == K_6:
                            if len(riichiList) >= 6:
                                if riichiSelect == 6:
                                    isInputDone = True
                                else:
                                    riichiSelect = 6
                        elif event.key == K_7:
                            if len(riichiList) >= 7:
                                if riichiSelect == 7:
                                    isInputDone = True
                                else:
                                    riichiSelect = 7
                        elif event.key == K_8:
                            if len(riichiList) >= 8:
                                if riichiSelect == 8:
                                    isInputDone = True
                                else:
                                    riichiSelect = 8
                        elif event.key == K_9:
                            if len(riichiList) >= 9:
                                if riichiSelect == 9:
                                    isInputDone = True
                                else:
                                    riichiSelect = 9
                        elif event.key == K_0:
                            if len(riichiList) >= 10:
                                if riichiSelect == 10:
                                    isInputDone = True
                                else:
                                    riichiSelect = 10
                        elif event.key == K_MINUS:
                            if len(riichiList) >= 11:
                                if riichiSelect == 11:
                                    isInputDone = True
                                else:
                                    riichiSelect = 11
                        elif event.key == K_EQUALS:
                            if len(riichiList) >= 12:
                                if riichiSelect == 12:
                                    isInputDone = True
                                else:
                                    riichiSelect = 3
                        elif event.key == K_BACKSLASH:
                            if len(riichiList) >= 13:
                                if riichiSelect == 13:
                                    isInputDone = True
                                else:
                                    riichiSelect = 13
                        elif event.key == K_BACKSPACE:
                            if len(riichiList) >= 14:
                                if riichiSelect == 14:
                                    isInputDone = True
                                else:
                                    riichiSelect = 14


                GameScreen(SCREEN, 'clear')

                for i in range(len(riichiList)):
                    if riichiList[i] == len(eval(player + 'Hand')) - 1:
                        pygame.draw.polygon(SCREEN, Color('red'), [((p1HandPos[0]//2)*3 + 6 + (cardSize.w * riichiList[i]) + 44, p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * riichiList[i]) + 44, p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * riichiList[i]) + 44, p1HandPos[1] - 6)])
                        SCREEN.blit(eval('text' + str(i+1)), ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * riichiList[i]) + 44, p1HandPos[1] - 50))
                    else:
                        pygame.draw.polygon(SCREEN, Color('red'), [((p1HandPos[0]//2)*3 + 6 + (cardSize.w * riichiList[i]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * riichiList[i]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * riichiList[i]), p1HandPos[1] - 6)])
                        SCREEN.blit(eval('text' + str(i+1)), ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * riichiList[i]), p1HandPos[1] - 50))


                pygame.display.flip()
                clock.tick(TARGET_FPS)

        


def Action_Tsumo(SCREEN, player):
    global gameInfo, cardList
    global p1Hand, p2Hand, p3Hand, p4Hand

    ListInit()

    yaku = YakuCheck(eval(player + 'Hand'), eval(player + 'Info'), gameInfo, cardList)

    pygame.time.wait(500)
    
    ScoreCalculate(SCREEN, yaku, player)
    
    gameInfo['turn'] = 'end' + player
    return


    
def Action_Kan(SCREEN, player):
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global cardList, handList
    global p1Hand, p2Hand, p3Hand, p4Hand
    global handList, mouseInButton
    
    kanList = []


    for i in range(len(eval(player + 'Hand')) - 3):
        compareTile = eval(player + 'Hand')[i]
        kanList_s = [i]
        for j in range(i + 1, len(eval(player + 'Hand'))):
            if compareTile[:2] == eval(player + 'Hand')[j][:2]:
                kanList_s.append(j)
        if len(kanList_s) == 4:
            kanList.append(kanList_s)


    #가깡
    if eval(player + 'Info')['riichi'] == 0:
        status = HandCheck(eval(player + 'Hand'), eval(player + 'Info'), 'huro')
        if len(status['koutsu']) != 0:
            for i in range(len(status['koutsu'])):
                compareTile = status['koutsu'][i][0][:2]
                for j in range(len(eval(player + 'Hand'))):
                    if compareTile == eval(player + 'Hand')[j][:2]:
                        kanList.append([j])



    if len(kanList) == 1:
        ListInit()
        discard = ''
        if len(kanList[0]) == 4:
            eval(player + 'Info')['huro'].append([eval(player + 'Hand')[kanList[0][0]] + '1', eval(player + 'Hand')[kanList[0][1]] + '1', eval(player + 'Hand')[kanList[0][2]] + '1', eval(player + 'Hand')[kanList[0][3]] + '1'])
            for i in range(1, 5):
                eval(player + 'Hand').pop(kanList[0][-i])
                handList.pop()
        else:
            loopExit = False
            for i in range(len(eval(player + 'Info')['huro'])):
                if loopExit == True:
                    break
                if eval(player + 'Hand')[kanList[0][0]][:2] == eval(player + 'Info')['huro'][i][0][:2]:
                    discard = eval(player + 'Hand')[kanList[0][0]][:-1]
                    for j in range(3):
                        if eval(player + 'Info')['huro'][i][j][-1] != '1':
                            eval(player + 'Info')['huro'][i].insert(j, eval(player + 'Hand')[kanList[0][0]] + eval(player + 'Info')['huro'][i][j][-1])
                            eval(player + 'Hand').pop(kanList[0][0])
                            handList.pop()
                            loopExit = True
                            break
        eval(player + 'Hand').append(cardList.pop(-1))
        handList.append(0)
        gameInfo['kan'] += 1
        if gameInfo['kan'] == 4:
            if len(HandCheck(eval(player + 'Hand'), eval(player + 'Info'), 'huro')['kantsu']) == 4:
                gameInfo['suukantsu'] = True
        eval(player + 'Info')['rinshan'] = True
        gameInfo['turn'] = player
        if len(kanList[0]) == 1:
            ChankanCheck(SCREEN, player, discard)
        return


    else:
        if player == 'p1':
            isInputDone = False
            kanSelect = 0
            while True:
                if isInputDone == True:
                    ListInit()
                    discard = ''
                    if len(kanList[kanSelect]) == 4:
                        eval(player + 'Info')['huro'].append([eval(player + 'Hand')[kanList[kanSelect][0]] + '1', eval(player + 'Hand')[kanList[kanSelect][1]] + '1', eval(player + 'Hand')[kanList[kanSelect][2]] + '1', eval(player + 'Hand')[kanList[kanSelect][3]] + '1'])
                        for i in range(1, 5):
                            eval(player + 'Hand').pop(kanList[kanSelect][-i])
                            handList.pop()
                    else:
                        for i in range(len(eval(player + 'Info')['huro'])):
                            if eval(player + 'Hand')[kanList[kanSelect][0]][:2] == eval(player + 'Info')['huro'][i][0][:2]:
                                discard = eval(player + 'Hand')[kanList[kanSelect][0]][:-1]
                                for j in range(3):
                                    if eval(player + 'Info')['huro'][i][j][-1] != '1':
                                        eval(player + 'Info')['huro'][i].insert(j, eval(player + 'Hand')[kanList[kanSelect][0]] + eval(player + 'Info')['huro'][i][j][-1])
                                        eval(player + 'Hand').pop(kanList[kanSelect][0])
                                        handList.pop()
                                        break
                    eval(player + 'Hand').append(cardList.pop(-1))
                    handList.append(0)
                    gameInfo['kan'] += 1
                    if gameInfo['kan'] == 4:
                        if len(HandCheck(eval(player + 'Hand'), eval(player + 'Info'), 'huro')['kantsu']) == 4:
                            gameInfo['suukantsu'] = True
                    gameInfo['turn'] = player
                    eval(player + 'Info')['rinshan'] = True
                    if len(kanList[kanSelect]) == 1:
                        ChankanCheck(SCREEN, player, discard)
                    return


                ListInit()
                if len(kanList[kanSelect]) == 4:
                    for i in range(4):
                        handList[kanList[kanSelect][i]] = 1
                else:
                    handList[kanList[kanSelect][0]] = 1

                ##########Key Input##########
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    ##########mouse##########
                    if pygame.mouse.get_focused():
                        mX, mY = pygame.mouse.get_pos()

                        loopExit = False
                        for i in range(len(kanList)):
                            if loopExit == True:
                                break
                            for j in range(len(kanList[i])):
                                if eval('cardPos' + str(kanList[i][j] + 1)).collidepoint(mX, mY):
                                    kanSelect = i
                                    loopExit = True
                                    mouseInButton = True
                                    break

                        if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                            isInputDone = True
                        mouseInButton = False


                    ##########keyboard##########
                    if not hasattr(event, 'key'):
                        continue
                    if event.type == KEYDOWN:
                        if event.key == K_LEFT:
                            kanSelect -= 1
                            if kanSelect == -1:
                                kanSelect = len(kanList) - 1
                        elif event.key == K_RIGHT:
                            kanSelect += 1
                            if kanSelect == len(kanList):
                                kanSelect = 0
                        elif event.key == K_RETURN:
                            isInputDone = True
                        elif event.key == K_1:
                            if kanSelect == 0:
                                isInputDone = True
                            else:
                                kanSelect = 0
                        elif event.key == K_2:
                            if kanSelect == 1:
                                isInputDone = True
                            else:
                                kanSelect = 1
                        elif event.key == K_3:
                            if len(kanList) >= 3:
                                if kanSelect == 2:
                                    isInputDone = True
                                else:
                                    kanSelect = 2




                GameScreen(SCREEN, 'clear')


                for i in range(len(kanList)):
                    for j in range(len(kanList[i])):
                        if kanList[i] == len(eval(player + 'Hand')) - 1:
                            pygame.draw.polygon(SCREEN, Color('red'), [((p1HandPos[0]//2)*3 + 6 + (cardSize.w * kanList[i][j]) + 44, p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * kanList[i][j]) + 44, p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * kanList[i][j]) + 44, p1HandPos[1] - 6)])
                            SCREEN.blit(eval('text' + str(i+1)), ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * kanList[i][j]) + 44, p1HandPos[1] - 50))
                        else:
                            pygame.draw.polygon(SCREEN, Color('red'), [((p1HandPos[0]//2)*3 + 6 + (cardSize.w * kanList[i][j]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 26 + (cardSize.w * kanList[i][j]), p1HandPos[1] - 14), ((p1HandPos[0]//2)*3 + 16 + (cardSize.w * kanList[i][j]), p1HandPos[1] - 6)])
                            SCREEN.blit(eval('text' + str(i+1)), ((p1HandPos[0]//2)*3 + 6 + (cardSize.w * kanList[i][j]), p1HandPos[1] - 50))


                pygame.display.flip()
                clock.tick(TARGET_FPS)



def ChankanCheck(SCREEN, kanPlayer, discard):
    global p1Info, p2Info, p3Info, p4Info
    global p1Hand, p2Hand, p3Hand, p4Hand


    chankanList = []

    playerList = ['p1', 'p2', 'p3', 'p4']
    playerList.pop(playerList.index(kanPlayer))

    for i in range(3):
        if eval(playerList[i] + 'Info')['shanten'] == 0:
            playerHand = eval(playerList[i] + 'Hand').copy()
            playerHand.append(discard)
            if HandCheck(playerHand, eval(playerList[i] + 'Info'), 'shanten') == -1:
                chankanList.append(playerList[i])
    ################################################################################
    #후리텐
    ################################################################################
    

    for i in range(len(chankanList)):
        Action_Chankan(SCREEN, chankanList[i], kanPlayer, discard)
    





def Action_Chankan(SCREEN, player, targetPlayer, discard):
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global cardList, handList
    global p1Hand, p2Hand, p3Hand, p4Hand
    global handList, mouseInButton


    if player == 'p1':
        isInputDone = False
        chankanSelect = 0
        while True:
            if isInputDone == True:
                if chankanSelect == 0:
                    return
                else:
                    ListInit()
                    eval(player + 'Info')['chankan'] = True
                    yaku = YakuCheck(eval(player + 'Hand'), eval(player + 'Info'), gameInfo, cardList, discard)
                    
                    pygame.time.wait(500)
                    
                    ScoreCalculate(SCREEN, yaku, player, targetPlayer, discard)
                    gameInfo['turn'] = 'end' + player
                    return


            ##########Key Input##########
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                    
                ##########mouse##########
                if pygame.mouse.get_focused():
                    mX, mY = pygame.mouse.get_pos()

                    if f8Button.collidepoint(mX, mY):
                        chankanSelect = 1
                        mouseInButton = True
                    elif f9Button.collidepoint(mX, mY):
                        chankanSelect = 0
                        mouseInButton = True

                    if mouseInButton == True and event.type == MOUSEBUTTONDOWN and event.button == 1: #왼쪽버튼 클릭
                        isInputDone = True
                    mouseInButton = False
                    
                ##########keyboard##########
                if not hasattr(event, 'key'):
                    continue
                if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == K_RIGHT:
                        if chankanSelect == 0:
                            chankanSelect = 1
                        else:
                            chankanSelect = 0
                    elif event.key == K_RETURN:
                        isInputDone = True
                    elif event.key == K_F8:
                        if chankanSelect == 1:
                            isInputDone = True
                        else:
                            chankanSelect = 1
                    elif event.key == K_F9:
                        if chankanSelect == 0:
                            isInputDone = True
                        else:
                            chankanSelect = 0


            GameScreen(SCREEN, 'clear')

            if chankanSelect == 0:
                pygame.draw.rect(SCREEN, buttonColor_s, f9Button_s)
            pygame.draw.rect(SCREEN, buttonColor, f9Button)
            SCREEN.blit(textNo, (f9Button.x - 10, f9Button.y - 3))
            SCREEN.blit(textF9, (f9Button.x + 40, f9Button.y - f9Button.h))
            
            if chankanSelect == 1:
                pygame.draw.rect(SCREEN, buttonColor_s, f8Button_s)
            pygame.draw.rect(SCREEN, buttonColor, f8Button)
            SCREEN.blit(textRon, (f8Button.x + 50, f8Button.y - 3))
            SCREEN.blit(textF8, (f8Button.x + 40, f8Button.y - f8Button.h))

            pygame.display.flip()
            clock.tick(TARGET_FPS)


    else:
        eval(player + 'Info')['chankan'] = True
        yaku = YakuCheck(eval(player + 'Hand'), eval(player + 'Info'), gameInfo, cardList, discard)

        pygame.time.wait(500)
        
        ScoreCalculate(SCREEN, yaku, player, targetPlayer, discard)
        gameInfo['turn'] = 'end' + player
        return



def ResetAction(player, *actionType):
    global p1Info, p2Info, p3Info, p4Info
    global actionList, actionSelect, inputType

    eval(player + 'Info')['canAction'] = []
    if player == 'p1':
        actionList = []
        actionSelect = 0
        inputType = 0



    if len(actionType) != 0:
        return

    
    if gameInfo['count'] <= 4:
        eval(player + 'Info')['hou'] = False
        
    if eval(player + 'Info')['ippatsu'] == 2:
        eval(player + 'Info')['ippatsu'] = 1
    elif eval(player + 'Info')['ippatsu'] == 1:
        eval(player + 'Info')['ippatsu'] = 0

    if eval(player + 'Info')['doubleriichi'] == 0:
        eval(player + 'Info')['doubleriichi'] = -1

    eval(player + 'Info')['rinshan'] = False
    
####################################################################



############################## Yaku ##############################

def StatusCheck_1(playerHand, playerInfo, returnType):
    status = {'shuntsu':[], 'koutsu':[], 'kantsu':[], 'ankan':[], 'toitsu':[], 'tatsu':[], 'pentatsu':[], 'ryantatsu':[], 'kantatsu':[]}
    hList = []

    #패가 14개일때. 즉, 패산에서 패 하나를 쯔모 했을때 확인함
    hList = playerHand.copy()
    hList = CardSort(hList).copy()

    
    #운 패(퐁, 치, 깡)
    if returnType == 'form' or returnType == 'huro' or returnType == 'shanten':
        if len(playerInfo['huro']) != 0:
            for num in range(len(playerInfo['huro'])):
                tempList = []
                if len(playerInfo['huro'][num]) == 3:
                    if playerInfo['huro'][num][0][:2] == playerInfo['huro'][num][1][:2] == playerInfo['huro'][num][2][:2]:
                        status['koutsu'].append(playerInfo['huro'][num])
                    else:
                        status['shuntsu'].append(playerInfo['huro'][num])
                else:
                    count = 0
                    for i in range(4):
                        if playerInfo['huro'][num][-1] != '1':
                            count += 1
                    if count == 0:
                        status['ankan'].append(playerInfo['huro'][num])
                    else:
                        status['kantsu'].append(playerInfo['huro'][num])

    if returnType == 'huro':
        return status, 0
    
    
    #몸통
    for loop in range(len(hList)//3):
        loopExit = False
        for i in range(len(hList) - 2):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList) - 1):
                if loopExit == True:
                    break
                for k in range(j + 1, len(hList)):
                    if loopExit == True:
                        break
                    if (hList[i][0] == hList[j][0] == hList[k][0]) and hList[i][1].isdigit() == True and hList[j][1].isdigit() == True and hList[k][1].isdigit() == True:
                        if int(hList[i][1]) + 2 == int(hList[j][1]) + 1 == int(hList[k][1]):
                            if hList[i][:2] == hList[i+1][:2]:
                                if hList[j][:2] == hList[j+1][:2] == hList[j+2][:2]:
                                    status['shuntsu'].append([hList[j], hList[j+1], hList[j+2]])
                                    hList.pop(j+2)
                                    hList.pop(j+1)
                                    hList.pop(j)
                                    loopExit = True
                                    break
                                else:
                                    for l in range(k + 1, len(hList)):
                                        if (hList[k][0] == hList[l][0]) and hList[l][1].isdigit() == True and (int(hList[k][1]) + 1 == int(hList[l][1])):
                                            status['shuntsu'].append([hList[j], hList[k], hList[l]])
                                            hList.pop(l)
                                            hList.pop(k)
                                            hList.pop(j)
                                            loopExit = True
                                            break
                            else:
                                status['shuntsu'].append([hList[i], hList[j], hList[k]])
                                hList.pop(k)
                                hList.pop(j)
                                hList.pop(i)
                                loopExit = True
                        elif hList[i][1] == hList[j][1] == hList[k][1]:
                            status['koutsu'].append([hList[i], hList[j], hList[k]])
                            hList.pop(k)
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True
                    elif hList[i][:2] == hList[j][:2] == hList[k][:2]:
                        status['koutsu'].append([hList[i], hList[j], hList[k]])
                        hList.pop(k)
                        hList.pop(j)
                        hList.pop(i)
                        loopExit = True
                    

    #또이
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][:2] == hList[j][:2]:
                    status['toitsu'].append([hList[i], hList[j]])
                    hList.pop(j)
                    hList.pop(i)
                    loopExit = True

    #연속되는 타쯔(펜타츠 + 량타츠)
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][1].isdigit() == True and hList[j][1].isdigit() == True:
                    if (hList[i][0] == hList[j][0]) and (int(hList[i][1]) + 1 == int(hList[j][1])):
                        if hList[i][1] == '1' or hList[j][1] == '1':
                            status['tatsu'].append([hList[i], hList[j]])
                            status['pentatsu'].append([hList[i], hList[j]])
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True
                        else:
                            status['tatsu'].append([hList[i], hList[j]])
                            status['ryantatsu'].append([hList[i], hList[j]])
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True

    #한칸 떨어진 타쯔(칸타츠)
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][1].isdigit() == True and hList[j][1].isdigit() == True:
                    if (hList[i][0] == hList[j][0]) and int(hList[i][1]) + 2 == int(hList[j][1]):
                        status['tatsu'].append([hList[i], hList[j]])
                        status['kantatsu'].append([hList[i], hList[j]])
                        hList.pop(j)
                        hList.pop(i)
                        loopExit = True


    #샹텐 계산
    shanten = 8
    shanten = 8 - ((len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']))*2 + len(status['toitsu']) + len(status['tatsu']))

    if (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']) + len(status['toitsu']) + len(status['tatsu'])) >= 6:
        shanten = shanten + (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']) + len(status['toitsu']) + len(status['tatsu'])) - 5
    if (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu'])) != 4:
        if len(status['toitsu']) == 0:
            shanten += 1
    elif shanten == -1:
        if len(status['toitsu']) == 0:
            shanten += 1
            

    return status, shanten
        

def StatusCheck_2(playerHand, playerInfo, returnType):
    status = {'shuntsu':[], 'koutsu':[], 'kantsu':[], 'ankan':[], 'toitsu':[], 'tatsu':[], 'pentatsu':[], 'ryantatsu':[], 'kantatsu':[]}
    hList = []

    #패가 14개일때. 즉, 패산에서 패 하나를 쯔모 했을때 확인함
    hList = playerHand.copy()
    hList = CardSort(hList).copy()

    
    #운 패(퐁, 치, 깡)
    if returnType == 'form' or returnType == 'huro' or returnType == 'shanten':
        if len(playerInfo['huro']) != 0:
            for num in range(len(playerInfo['huro'])):
                if len(playerInfo['huro'][num]) == 3:
                    if playerInfo['huro'][num][0][:2] == playerInfo['huro'][num][1][:2] == playerInfo['huro'][num][2][:2]:
                        status['koutsu'].append(playerInfo['huro'][num])
                    else:
                        status['shuntsu'].append(playerInfo['huro'][num])
                else:
                    count = 0
                    for i in range(4):
                        if playerInfo['huro'][num][-1] != '1':
                            count += 1
                    if count == 0:
                        status['ankan'].append(playerInfo['huro'][num])
                    else:
                        status['kantsu'].append(playerInfo['huro'][num])

    if returnType == 'huro':
        return status, 0
          
    
    #몸통
    for loop in range(len(hList) // 3):
        loopExit = False
        for i in range(len(hList) - 2):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList) - 1):
                if loopExit == True:
                    break
                for k in range(j + 1, len(hList)):
                    if loopExit == True:
                        break
                    if (hList[i][0] == hList[j][0] == hList[k][0]) and hList[i][1].isdigit() == True and hList[j][1].isdigit() == True and hList[k][1].isdigit() == True:
                        if int(hList[i][1]) + 2 == int(hList[j][1]) + 1 == int(hList[k][1]):
                            status['shuntsu'].append([hList[i], hList[j], hList[k]])
                            hList.pop(k)
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True
                        elif hList[i][:2] == hList[j][:2] == hList[k][:2]:
                            status['koutsu'].append([hList[i], hList[j], hList[k]])
                            hList.pop(k)
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True
                    elif hList[i][:2] == hList[j][:2] == hList[k][:2]:
                        status['koutsu'].append([hList[i], hList[j], hList[k]])
                        hList.pop(k)
                        hList.pop(j)
                        hList.pop(i)
                        loopExit = True



    #또이
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][:2] == hList[j][:2]:
                    status['toitsu'].append([hList[i], hList[j]])
                    hList.pop(j)
                    hList.pop(i)
                    loopExit = True

    #연속되는 타쯔(펜타츠 + 량타츠)
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][1].isdigit() == True and hList[j][1].isdigit() == True:
                    if (hList[i][0] == hList[j][0]) and (int(hList[i][1]) + 1 == int(hList[j][1])):
                        if hList[i][1] == '1' or hList[j][1] == '1':
                            status['tatsu'].append([hList[i], hList[j]])
                            status['pentatsu'].append([hList[i], hList[j]])
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True
                        else:
                            status['tatsu'].append([hList[i], hList[j]])
                            status['ryantatsu'].append([hList[i], hList[j]])
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True

    #한칸 떨어진 타쯔(칸타츠)
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][1].isdigit() == True and hList[j][1].isdigit() == True:
                    if (hList[i][0] == hList[j][0]) and int(hList[i][1]) + 2 == int(hList[j][1]):
                        status['tatsu'].append([hList[i], hList[j]])
                        status['kantatsu'].append([hList[i], hList[j]])
                        hList.pop(j)
                        hList.pop(i)
                        loopExit = True
    

    #샹텐 계산
    shanten = 8
    shanten = 8 - ((len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']))*2 + len(status['toitsu']) + len(status['tatsu']))

    if (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']) + len(status['toitsu']) + len(status['tatsu'])) >= 6:
        shanten = shanten + (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']) + len(status['toitsu']) + len(status['tatsu'])) - 5
    if (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu'])) != 4:
        if len(status['toitsu']) == 0:
            shanten += 1
    elif shanten == -1:
        if len(status['toitsu']) == 0:
            shanten += 1
            


    return status, shanten


def StatusCheck_3(playerHand, playerInfo, returnType):
    status = {'shuntsu':[], 'koutsu':[], 'kantsu':[], 'toitsu':[], 'tatsu':[], 'pentatsu':[], 'ryantatsu':[], 'kantatsu':[]}
    hList = []

    #패가 14개일때. 즉, 패산에서 패 하나를 쯔모 했을때 확인함
    hList = playerHand.copy()
    hList = CardSort(hList).copy()

    
    #운 패(퐁, 치, 깡)
    if returnType == 'form' or returnType == 'huro' or returnType == 'shanten':
        if len(playerInfo['huro']) != 0:
            for num in range(len(playerInfo['huro'])):
                if len(playerInfo['huro'][num]) == 3:
                    if playerInfo['huro'][num][0][:2] == playerInfo['huro'][num][1][:2] == playerInfo['huro'][num][2][:2]:
                        status['koutsu'].append(playerInfo['huro'][num])
                    else:
                        status['shuntsu'].append(playerInfo['huro'][num])
                else:
                    status['kantsu'].append(playerInfo['huro'][num])

    if returnType == 'huro':
        return status, 0
          
    
    #몸통
    for loop in range(len(hList)//3):
        loopExit = False
        for i in range(len(hList) - 2):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList) - 1):
                if loopExit == True:
                    break
                for k in range(j + 1, len(hList)):
                    if loopExit == True:
                        break
                    if (hList[i][0] == hList[j][0] == hList[k][0]) and hList[i][1].isdigit() == True and hList[j][1].isdigit() == True and hList[k][1].isdigit() == True:
                        if int(hList[i][1]) + 2 == int(hList[j][1]) + 1 == int(hList[k][1]):
                            status['shuntsu'].append([hList[i], hList[j], hList[k]])
                            hList.pop(k)
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True

                            
    for loop in range(len(hList)//3):
        loopExit = False
        for i in range(len(hList) - 2):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList) - 1):
                if loopExit == True:
                    break
                for k in range(j + 1, len(hList)):
                    if loopExit == True:
                        break
                    if hList[i][:2] == hList[j][:2] == hList[k][:2]:
                        status['koutsu'].append([hList[i], hList[j], hList[k]])
                        hList.pop(k)
                        hList.pop(j)
                        hList.pop(i)
                        loopExit = True
                        

                    

    #또이
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][:2] == hList[j][:2]:
                    status['toitsu'].append([hList[i], hList[j]])
                    hList.pop(j)
                    hList.pop(i)
                    loopExit = True

    #연속되는 타쯔(펜타츠 + 량타츠)
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][1].isdigit() == True and hList[j][1].isdigit() == True:
                    if (hList[i][0] == hList[j][0]) and (int(hList[i][1]) + 1 == int(hList[j][1])):
                        if hList[i][1] == '1' or hList[j][1] == '1':
                            status['tatsu'].append([hList[i], hList[j]])
                            status['pentatsu'].append([hList[i], hList[j]])
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True
                        else:
                            status['tatsu'].append([hList[i], hList[j]])
                            status['ryantatsu'].append([hList[i], hList[j]])
                            hList.pop(j)
                            hList.pop(i)
                            loopExit = True

    #한칸 떨어진 타쯔(칸타츠)
    for loop in range(len(hList)//2):
        loopExit = False
        for i in range(len(hList) - 1):
            if loopExit == True:
                break
            for j in range(i + 1, len(hList)):
                if loopExit == True:
                    break
                if hList[i][1].isdigit() == True and hList[j][1].isdigit() == True:
                    if (hList[i][0] == hList[j][0]) and int(hList[i][1]) + 2 == int(hList[j][1]):
                        status['tatsu'].append([hList[i], hList[j]])
                        status['kantatsu'].append([hList[i], hList[j]])
                        hList.pop(j)
                        hList.pop(i)
                        loopExit = True
    

    #샹텐 계산
    shanten = 8
    shanten = 8 - ((len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']))*2 + len(status['toitsu']) + len(status['tatsu']))


    if (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']) + len(status['toitsu']) + len(status['tatsu'])) >= 6:
        shanten = shanten + (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu']) + len(status['toitsu']) + len(status['tatsu'])) - 5
    if (len(status['shuntsu']) + len(status['koutsu']) + len(status['kantsu'])) != 4:
        if len(status['toitsu']) == 0:
            shanten += 1
    elif shanten == -1:
        if len(status['toitsu']) == 0:
            shanten += 1 



    return status, shanten

    

def HandCheck(playerHand, playerInfo, returnType):
    #샹텐 계산 or 확인
    #shuntsu(슌쯔) + koutsu(컷쯔) + kantsu(캉쯔) = mentsu(멘쯔)
    #toitsu(또이쯔) + tatsu(타쯔)
    status = {}
    shanten = 8

    status_1, shanten_1 = StatusCheck_1(playerHand, playerInfo, returnType)
    status_2, shanten_2 = StatusCheck_2(playerHand, playerInfo, returnType)
    status_3, shanten_3 = StatusCheck_3(playerHand, playerInfo, returnType)
    
    if shanten_1 <= shanten_2:
        if shanten_1 <= shanten_3:
            status = status_1
            shanten = shanten_1
        else:
            status = status_3
            shanten = shanten_3
        
    else:
        if shanten_2 <= shanten_3:
            status = status_2
            shanten = shanten_2
        else:
            status = status_3
            shanten = shanten_3
        
    
    if returnType == 'shanten':        
        #치또이츠
        if len(status['toitsu']) == 5:
            shanten = 1
        elif len(status['toitsu']) == 6:
            shanten = 0
        elif len(status['toitsu']) == 7:
            shanten = -1
    
        
        #국사무쌍
        hList = playerHand.copy()
        hList = CardSort(hList).copy()
        kokushimusouList = ['m1', 'm9', 'p1', 'p9', 's1', 's9', 'ea', 'so', 'we', 'no', 'ha', 'gr', 'ch']
        compareTile = kokushimusouList.copy()
        kokushiLeft = ''
        
        for i in range(len(hList)):
            if hList[i][:2] in kokushimusouList:
                kokushimusouList.pop(kokushimusouList.index(hList[i][:2]))
            else:
                if (hList[i][:2] in compareTile) and kokushiLeft == '':
                    kokushiLeft = hList[i]

        if len(kokushimusouList) == 0 and kokushiLeft != '':
            shanten = -1
        elif len(kokushimusouList) == 0 or (len(kokushimusouList) == 1 and kokushiLeft != ''):
            shanten = 0
        elif (len(kokushimusouList) == 1 and kokushiLeft == '') or (len(kokushimusouList) == 2 and kokushiLeft != ''):
            shanten = 1
        elif (len(kokushimusouList) == 2 and kokushiLeft == '') or (len(kokushimusouList) == 3 and kokushiLeft != ''):
            shanten = 2
        

            
        #텐파이이면 0 리턴, 패가 완성됬을경우 -1 리턴
        return shanten
    
    else:
        return status
    



def YakuCheck(playerHand, playerInfo, gameInfo, cardList, *disCard):
    #1판
    #리치, 일발, 쯔모, 핑후, 이페코, 탕야오, 역패, 영상개화, 챵깡, 해저로월, 하저로어

    #2판
    #삼색동순, 삼색동각, 일기통관, 챤타, 치또이츠, 또이또이, 산앙커, 혼노두, 산깡쯔, 소삼원, 더블리치

    #3판
    #량페코(치또이츠와 중첩X), 혼일색, 준짱

    #6판
    #청일색

    #역만
    #국사무쌍, 스앙코(앙코를 론으로 완성했을경우 또이또이+산앙코 로 봄), 구련보등, 자일색, 녹일색, 청노두, 스깡쯔, 사희화(동남서북 모두 코쯔면 대사희, 3개 코쯔에 머리1개면 소사희) , 대삼원, 천화, 지화, 인화


    hList = []
    tsumo = False
    huro = False

    yaku = {'fan':0, 'yakuman':0, 'fu':20}

    #자패
    jihai = ['east', 'south', 'west', 'north', 'haku', 'green', 'chun']
    #삼원패
    sangenhai = ['haku', 'gree', 'chun']
    
    #len(playerInfo['huro']) == 0 이면 울지않은상태
    if len(playerInfo['huro']) != 0:
        for i in range(len(playerInfo['huro'])):
            if len(playerInfo['huro'][i]) != 4:
                huro = True
                break
            else:
                for j in range(4):
                    if playerInfo['huro'][i][j][-1] != '1':
                        huro = True
                        break
            if huro == True:
                break

            

    #disCard가 없으면 패가 완성된 상태(쯔모), disCard가 있으면 텐파이인 상태에서 다른 사람이 버린 패를 추가하여 계산
    if len(disCard) == 0:
        status_original = HandCheck(playerHand[:-1], playerInfo, 'formNoHuro')
        hList = playerHand.copy()
        hList = CardSort(hList).copy()
        tsumo = True
    else:
        status_original = HandCheck(playerHand, playerInfo, 'formNoHuro')
        hList = playerHand.copy()
        hList.append(disCard[0])
        hList = CardSort(hList).copy()

    status_hand = HandCheck(hList, playerInfo, 'formNoHuro')
    status_huro = HandCheck(hList, playerInfo, 'huro')
    status = HandCheck(hList, playerInfo, 'form')


    if huro == True:
        for i in range(len(playerInfo['huro'])):
            for j in range(len(playerInfo['huro'][i])):
                hList.append(playerInfo['huro'][i][j][:-1])
        hList = CardSort(hList).copy()
    

    

    #리치(riichi) - 1 + 더블리치(doubleriichi) - 2
    if playerInfo['riichi'] == 1 or playerInfo['riichi'] == 2:
        if playerInfo['doubleriichi'] == 1:
            yaku['doubleriichi'] = 2
            yaku['fan'] += 2
        else:
            yaku['riichi'] = 1
            yaku['fan'] += 1
    
    #일발(ippatsu) - 1
    if playerInfo['ippatsu'] == 1:
        yaku['ippatsu'] = 1
        yaku['fan'] += 1
    
    #쯔모(tsumo) - 1
    if huro == False and tsumo == True:
        yaku['tsumo'] = 1
        yaku['fan'] += 1
        
    #핑후(pinfu) - 1
    if huro == False:
        if len(status['shuntsu']) == 4 and len(status['toitsu']) == 1:
            if '1' <= status['toitsu'][0][0][1] and status['toitsu'][0][0][1] <= '9':
                if len(status_original['tatsu']) == 1 and status_original['tatsu'][0][0][1] != '1' and status_original['tatsu'][0][1][1] != '9':
                    if int(status_original['tatsu'][0][0][1]) + 1 == int(status_original['tatsu'][0][1][1]):
                        yaku['pinfu'] = 1
                        yaku['fan'] += 1

    #치또이츠(chiitoitsu) - 2
    if len(status['toitsu']) == 7:
        yaku['chiitoitsu'] = 2
        yaku['fan'] += 2

    #이페코(iipeikou) - 1 + 량페코(ryanpeikou) - 3 (치또이츠와 중첩X)
    if huro == False:
        if len(status['shuntsu']) >= 2:
            for i in range(len(status['shuntsu']) - 1):
                if status['shuntsu'][i][0][:2] == status['shuntsu'][i+1][0][:2]:
                    yaku['iipeikou'] = 1
                    yaku['fan'] += 1
                    break
        if len(status['shuntsu']) == 4:
            if status['shuntsu'][0][0][:2] == status['shuntsu'][1][0][:2] and status['shuntsu'][2][0][:2] == status['shuntsu'][3][0][:2]:
                if ('iipeikou' in yaku):
                    yaku['fan'] -= yaku['iipeikou']
                    yaku.pop('iipeikou')
                if ('chiitoitsu' in yaku):
                    yaku['fan'] -= yaku['chiitoitsu']
                    yaku.pop('chiitoitsu')
                yaku['ryanpeikou'] = 3
                yaku['fan'] += 3

    #탕야오(tanyao) - 1
    if gameInfo['kuitan'] == True:
        count = 0
        for i in range(len(hList)):
            if '2' <=  hList[i][1] and hList[i][1] <= '8':
                count += 1
        if count == len(hList):
            yaku['tanyao'] = 1
            yaku['fan'] += 1
    else:
        if huro == False:
            count = 0
            for i in range(len(hList)):
                if '2' <=  hList[i][1] and hList[i][1] <= '8':
                    count += 1
            if count == len(hList):
                yaku['tanyao'] = 1
                yaku['fan'] += 1

    #역패(yakuhai) - 1
    for i in range(len(status['koutsu'])):
        if status['koutsu'][i][0][:4] == gameInfo['kyoku'][:4]:
            if ('yakuhai' in yaku) == False:
                yaku['yakuhai'] = 0
            yaku['yakuhai'] += 1
            yaku['fan'] += 1
        if status['koutsu'][i][0][:4] == playerInfo['wind'][:4]:
            if ('yakuhai' in yaku) == False:
                yaku['yakuhai'] = 0
            yaku['yakuhai'] += 1
            yaku['fan'] += 1
        if status['koutsu'][i][0][:4] in sangenhai:
            if ('yakuhai' in yaku) == False:
                yaku['yakuhai'] = 0
            yaku['yakuhai'] += 1
            yaku['fan'] += 1
    for i in range(len(status['kantsu'])):
        if status['kantsu'][i][0][:4] == gameInfo['kyoku'][:4]:
            if ('yakuhai' in yaku) == False:
                yaku['yakuhai'] = 0
            yaku['yakuhai'] += 1
            yaku['fan'] += 1
        if status['kantsu'][i][0][:4] == playerInfo['wind'][:4]:
            if ('yakuhai' in yaku) == False:
                yaku['yakuhai'] = 0
            yaku['yakuhai'] += 1
            yaku['fan'] += 1
        if status['kantsu'][i][0][:4] in sangenhai:
            if ('yakuhai' in yaku) == False:
                yaku['yakuhai'] = 0
            yaku['yakuhai'] += 1
            yaku['fan'] += 1
            
    #영상개화(rinshankaihou) - 1
    if playerInfo['rinshan'] == True:
        yaku['rinshankaihou'] = 1
        yaku['fan'] += 1

    #챵깡(chankan) - 1
    if playerInfo['chankan'] == True:
        yaku['chankan'] = 1
        yaku['fan'] += 1

    #해저로월(haiteiraoyue) - 1
    if gameInfo['rest'] == 0:
        if tsumo == True:
            yaku['haiteiraoyue'] = 1
            yaku['fan'] += 1
            
    #하저로어(houteiraoyui) - 1
    if gameInfo['rest'] == 0:
        if tsumo == False:
            yaku['houteiraoyui'] = 1
            yaku['fan'] += 1

    #삼색동순(sanshokudoujun) - 2/1
    if len(status['shuntsu']) >= 3:
        sanshokudoujun = False
        if len(status['shuntsu']) == 3:
            if status['shuntsu'][0][0][1] == status['shuntsu'][1][0][1] == status['shuntsu'][2][0][1]:
                if status['shuntsu'][0][0][0] != status['shuntsu'][1][0][0] and status['shuntsu'][1][0][0] != status['shuntsu'][2][0][0] and status['shuntsu'][0][0][0] != status['shuntsu'][2][0][0]:
                    sanshokudoujun = True
        else:
            for i in range(4):
                compareTile = [0, 1, 2, 3]
                compareTile.pop(i)
                if status['shuntsu'][compareTile[0]][0][1] == status['shuntsu'][compareTile[1]][0][1] == status['shuntsu'][compareTile[2]][0][1]:
                    if status['shuntsu'][compareTile[0]][0][0] != status['shuntsu'][compareTile[1]][0][0] and status['shuntsu'][compareTile[1]][0][0] != status['shuntsu'][compareTile[2]][0][0] and status['shuntsu'][compareTile[0]][0][0] != status['shuntsu'][compareTile[2]][0][0]:
                        sanshokudoujun = True
        if sanshokudoujun == True:
            if huro == False:
                yaku['sanshokudoujun'] = 2
                yaku['fan'] += 2
            else:
                yaku['sanshokudoujun'] = 1        
                yaku['fan'] += 1

    #삼색동각(sanshokudoukou) - 2
    if len(status['koutsu']) + len(status['kantsu']) >= 3:
        sanshokudoukou = False
        sanshokuList = []
        for i in range(len(status['koutsu'])):
            sanshokuList.append(status['koutsu'][i][0])
        for i in range(len(status['kantsu'])):
            sanshokuList.append(status['kantsu'][i][0])
        if len(sanshokuList) == 3:
            if sanshokuList[0][1] == sanshokuList[1][1] == sanshokuList[2][1]:
                if sanshokuList[0][0] != sanshokuList[1][0] and sanshokuList[1][0] != sanshokuList[2][0] and sanshokuList[0][0] != sanshokuList[2][0]:
                    sanshokudoukou = True
        else:
            for i in range(4):
                compareTile = [0, 1, 2, 3]
                compareTile.pop(i)
                if sanshokuList[compareTile[0]][1] == sanshokuList[compareTile[1]][1] == sanshokuList[compareTile[2]][1]:
                    if sanshokuList[compareTile[0]][0] != sanshokuList[compareTile[1]][0] and sanshokuList[compareTile[1]][0] != sanshokuList[compareTile[2]][0] and sanshokuList[compareTile[0]][0] != sanshokuList[compareTile[2]][0]:
                        sanshokudoukou = True
        if sanshokudoukou == True:
            yaku['sanshokudoukou'] = 2
            yaku['fan'] += 2

                
    #일기통관(ikkitsukan) - 2/1
    if len(status['shuntsu']) >= 3:
        for i in range(1 + len(status['shuntsu'])%3):
            if status['shuntsu'][i][0][1] == '1':
                if status['shuntsu'][i][0][0] == status['shuntsu'][i+1][0][0] == status['shuntsu'][i+2][0][0]:
                    if int(status['shuntsu'][i][0][1]) + 6 == int(status['shuntsu'][i+1][0][1]) + 3 == int(status['shuntsu'][i+2][0][1]):
                        if huro == False:
                            yaku['ikkitsukan'] = 2
                            yaku['fan'] += 2
                            break
                        else:
                            yaku['ikkitsukan'] = 1
                            yaku['fan'] += 1
                            break

    #챤타(chanta) - 2/1
    count = 0
    chantaList = ['m1', 'm9', 'p1', 'p9', 's1', 's9', 'ea', 'so', 'we', 'no', 'ha', 'gr', 'ch']
    for i in range(len(status['shuntsu'])):
        for j in range(3):
            if (status['shuntsu'][i][j][:2] in chantaList):
                count += 1
                break
    for i in range(len(status['koutsu'])):
        if (status['koutsu'][i][0][:2] in chantaList):
            count += 1
    for i in range(len(status['kantsu'])):
        if (status['kantsu'][i][0][:2] in chantaList):
            count += 1
    if status['toitsu'][0][0][:2] in chantaList:
        count += 1

    if count == 5:
        if huro == False:
            yaku['chanta'] = 2
            yaku['fan'] += 2
        else:
            yaku['chanta'] = 1
            yaku['fan'] += 1

    #준짱(junchan) - 3/2
    count = 0
    for i in range(len(status['shuntsu'])):
        for j in range(3):
            if ('1' in status['shuntsu'][i][j][1]) or ('9' in status['shuntsu'][i][j][1]):
                count += 1
                break
    for i in range(len(status['koutsu'])):
        if ('1' in status['koutsu'][i][0][1]) or ('9' in status['koutsu'][i][0][1]):
            count += 1
    for i in range(len(status['kantsu'])):
        if ('1' in status['kantsu'][i][0][1]) or ('9' in status['kantsu'][i][0][1]):
            count += 1
    if ('1' in status['toitsu'][0][0][1]) or ('9' in status['toitsu'][0][0][1]):
        count += 1

    if count == 5:
        if ('chanta' in yaku):
            yaku['fan'] -= yaku['chanta']
            yaku.pop('chanta')
        if huro == False:
            yaku['junchan'] = 3
            yaku['fan'] += 3
        else:
            yaku['junchan'] = 2
            yaku['fan'] += 2

    #또이또이(toitoi) - 2
    if len(status['koutsu']) + len(status['kantsu']) == 4:
        yaku['toitoi'] = 2
        yaku['fan'] += 2

    #산앙코(sanankou) - 2
    if len(status_original['koutsu']) + len(status_huro['ankan']) == 3:
        yaku['sanankou'] = 2
        yaku['fan'] += 2

    #스앙코(suuankou) - 역만/더블역만
    if len(status_original['koutsu']) + len(status_huro['ankan']) == 4:
        if ('sanankou' in yaku):
            yaku['fan'] -= yaku['sanankou']
            yaku.pop('sanankou')
        yaku['suuankou'] = 26
        yaku['yakuman'] += 2
    elif tsumo == True and len(status['koutsu']) == 4:
        if ('sanankou' in yaku):
            yaku['fan'] -= yaku['sanankou']
            yaku.pop('sanankou')
        yaku['suuankou'] = 13
        yaku['yakuman'] += 1

    #혼노두(honroutou) - 2
    count = 0
    honroutouList = ['m1', 'm9', 'p1', 'p9', 's1', 's9', 'ea', 'so', 'we', 'no', 'ha', 'gr', 'ch']
    for i in range(len(hList)):
        if (hList[i][:2] in honroutouList):
            count += 1
    if count == 14:
        yaku['honroutou'] = 2
        yaku['fan'] += 2

    #청노두(chinroutou) - 역만
    count = 0
    for i in range(len(hList)):
        if hList[i][1] == '1' or hList[i][1] == '9':
            count += 1
    if count == 14:
        yaku['chinroutou'] = 13
        yaku['yakuman'] += 1

    #산캉쯔(sankantsu) - 2
    if len(status['kantsu']) == 3:
        yaku['sankantsu'] = 2
        yaku['fan'] += 2

    #스깡쯔(suukantsu) - 역만
    if len(status['kantsu']) == 4:
        yaku['sankantsu'] = 13
        yaku['yakuman'] += 1

    #소삼원(shousangen) - 2
    if len(status['koutsu']) + len(status['kantsu']) >= 2:
        if (status['toitsu'][0][0][:4] in sangenhai):
            count = 0
            for i in range(len(status['koutsu'])):
                if (status['koutsu'][i][0][:4] in sangenhai):
                    count += 1
            if count >= 2:
                yaku['shousangen'] = 2
                yaku['fan'] += 2

    #대삼원(daisangen) - 역만
    if len(status['koutsu']) + len(status['kantsu']) >= 3:
        count = 0
        for i in range(len(status['koutsu'])):
            if (status['koutsu'][i][0][:4] in sangenhai):
                count += 1
        if count >= 3:
            yaku['shousangen'] = 13
            yaku['yakuman'] += 1

    #혼일색(honiisou) - 3/2
    honiisou = True
    compareTile = ''
    for i in range(len(hList)):
        if hList[i][1].isdigit() == True:
            if compareTile == '':
                compareTile = hList[i][0]
            if compareTile != hList[i][0]:
                honiisou = False
                break
    if honiisou == True:
        if huro == False:
            yaku['honiisou'] = 3
            yaku['fan'] += 3
        else:
            yaku['honiisou'] = 2
            yaku['fan'] += 2

    #청일색(chiniisou) - 6/5
    chiniisou = True
    compareTile = ''
    for i in range(len(hList)):
        if hList[i][1].isdigit() == True:
            if compareTile == '':
                compareTile = hList[i][0]
            if compareTile != hList[i][0]:
                chiniisou = False
                break
        else:
            chiniisou = False
            break
    if chiniisou == True:
        if ('honiisou' in yaku):
            yaku['fan'] -= yaku['honiisou']
            yaku.pop('honiisou')
        if huro == False:
            yaku['chiniisou'] = 6
            yaku['fan'] += 6
        else:
            yaku['chiniisou'] = 5
            yaku['fan'] += 5

    #국사무쌍(kokushimusou) - 역만/더블역만
    kokushimusouList = ['m1', 'm9', 'p1', 'p9', 's1', 's9', 'ea', 'so', 'we', 'no', 'ha', 'gr', 'ch']
    compareTile = kokushimusouList.copy()
    kokushiLeft = ''
    for i in range(len(hList)):
        if (hList[i][:2] in kokushimusouList):
            kokushimusouList.pop(kokushimusouList.index(hList[i][:2]))
        else:
            if (hList[i][:2] in compareTile) and kokushiLeft == '':
                kokushiLeft = hList[i]

    if len(kokushimusouList) == 0 and kokushiLeft != '':
        loopLen = 0
        if len(disCard) == 0:
            loopLen = len(playerHand[:-1])
        else:
            loopLen = len(playerHand)
            
        kokushimusouList = ['m1', 'm9', 'p1', 'p9', 's1', 's9', 'ea', 'so', 'we', 'no', 'ha', 'gr', 'ch']
        for i in range(loopLen):
            if (playerHand[i][:2] in kokushimusouList):
                kokushimusouList.pop(kokushimusouList.index(playerHand[i][:2]))
        if len(kokushimusouList) == 0:
            yaku['kokushimusou'] = 26
            yaku['yakuman'] += 2
        else:
            yaku['kokushimusou'] = 13
            yaku['yakuman'] += 1

    #구련보등(chuurenpoutou) - 역만/더블역만
    if ('chiniisou' in yaku) and huro == False:
        chiniisouList = ['1', '1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '9']
        for i in range(len(hList)):
            if (hList[i][1] in chiniisouList):
                chiniisouList.pop(chiniisouList.index(hList[i][1]))
        if len(chiniisouList) == 0:
            loopLen = 0
            if len(disCard) == 0:
                loopLen = len(playerHand[:-1])
            else:
                loopLen = len(playerHand)

            chiniisouList = ['1', '1', '1', '2', '3', '4', '5', '6', '7', '8', '9', '9', '9']
            for i in range(loopLen):
                if (playerHand[i][1] in chiniisouList):
                    chiniisouList.pop(chiniisouList.index(playerHand[i][1]))
            if len(chiniisouList) == 0:
                yaku['chuurenpoutou'] = 26
                yaku['yakuman'] += 2
            else:
                yaku['chuurenpoutou'] = 13
                yaku['yakuman'] += 1

    #자일색(tsuuiisou) - 역만
    count = 0
    for i in range(len(hList)):
        if (hList[i] in jihai):
            count += 1
    if count == 14:
        yaku['tsuuiisou'] = 13
        yaku['yakuman'] = 1

    #녹일색(ryuuiisou) - 역만
    count = 0
    ryuuiisouList = ['s2', 's3', 's4', 's6', 's8', 'gr']
    for i in range(len(hList)):
        if (hList[i][:2] in ryuuiisouList):
            count += 1
    if count == 14:
        yaku['ryuuiisou'] = 13
        yaku['yakuman'] += 1

    #소사희(shousuushii) - 역만
    if len(status['koutsu']) + len(status['kantsu']) >= 3:
        shousuushiiList = ['east', 'south', 'west', 'north']
        for i in range(len(status['koutsu'])):
            if (status['koutsu'][i][0] in shousuushiiList):
                shousuushiiList.pop(shousuushiiList.index(status['koutsu'][i][0]))
        for i in range(len(status['kantsu'])):
            if (status['kantsu'][i][0] in shousuushiiList):
                shousuushiiList.pop(shousuushiiList.index(status['kantsu'][i][0]))
        if (status['toitsu'][0][0] in shousuushiiList):
            shousuushiiList.pop(shousuushiiList.index(status['toitsu'][0][0]))
        if len(shousuushiiList) == 0:
            yaku['shousuushii'] = 13
            yaku['yakuman'] += 1

    #대사희(daisuushii) - 더블역만
    if len(status['koutsu']) + len(status['kantsu']) == 4:
        daisuushiiList = ['east', 'south', 'west', 'north']
        for i in range(len(status['koutsu'])):
            if (status['koutsu'][i][0] in daisuushiiList):
                daisuushiiList.pop(daisuushiiList.index(status['koutsu'][i][0]))
        for i in range(len(status['kantsu'])):
            if (status['kantsu'][i][0] in daisuushiiList):
                daisuushiiList.pop(daisuushiiList.index(status['kantsu'][i][0]))
        if len(daisuushiiList) == 0:
            if ('shousuushii' in yaku):
                yaku['yakuman'] -= yaku['shousuushii']//13
                yaku.pop('shousuushii')
            yaku['daisuushii'] = 26
            yaku['yakuman'] += 2

    #대차륜(daisharin) - 역만
    if gameInfo['daisharin'] == True:
        if ('ryanpeikou' in yaku) and ('chiniisou' in yaku):
            daisharinList = ['2', '2', '3', '3', '4', '4', '5', '5', '6', '6', '7', '7', '8', '8']
            for i in range(len(hList)):
                if hList[i][1] in daisharinList:
                    daisharinList.pop(daisharinList.index(hList[i][1]))
            if len(daisharinList) == 0:
                yaku['daisharin'] = 13
                yaku['yakuman'] += 1

    #천화(tenhou) - 역만
    if playerInfo['wind'] == 'east' and playerInfo['hou'] == True:
        yaku['tenhou'] = 13
        yaku['yakuman'] += 1

    #지화(chiihou) - 역만
    if playerInfo['wind'] != 'east' and playerInfo['hou'] == True and tsumo == True:
        yaku['chiihou'] = 13
        yaku['yakuman'] += 1

    #인화(renhou) - 역만
    if playerInfo['wind'] != 'east' and playerInfo['hou'] == True and tsumo == False:
        yaku['renhou'] = 13
        yaku['yakuman'] += 1

    #도라
    #적도라
    for i in range(len(hList)):
        if len(hList[i]) >= 3 and hList[i][1].isdigit() == True and hList[i][2] == 'r':
            if ('dora' in yaku) == False:
                yaku['dora'] = 1
            else:
                yaku['dora'] += 1

    #도라표시패
    doraList = []
    for i in range(gameInfo['kan'] + 1):
        doraList.append(cardList[-6 + gameInfo['kan'] - (i * 2)])
        if ('riichi' in yaku) or ('doubleriichi' in yaku):
            doraList.append(cardList[-6 + gameInfo['kan'] + 1 - (i * 2)])

    if len(doraList) != 0:
        mList = ['m1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9']
        pList = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6', 'p7', 'p8', 'p9']
        sList = ['s1', 's2', 's3', 's4', 's5', 's6', 's7', 's8', 's9']
        windList = ['east', 'sout', 'west', 'nort']
        sangenhaiList = ['haku', 'gree', 'chun']
        for i in range(len(doraList)):
            if doraList[i][:2] in mList:
                indexNum = mList.index(doraList[i][:2])
                if indexNum == len(mList) - 1:
                    indexNum = 0
                else:
                    indexNum += 1

                for j in range(len(hList)):
                    if hList[j][:2] == mList[indexNum]:
                        if ('dora' in yaku) == False:
                            yaku['dora'] = 1
                        else:
                            yaku['dora'] += 1
            elif doraList[i][:2] in pList:
                indexNum = pList.index(doraList[i][:2])
                if indexNum == len(pList) - 1:
                    indexNum = 0
                else:
                    indexNum += 1

                for j in range(len(hList)):
                    if hList[j][:2] == pList[indexNum]:
                        if ('dora' in yaku) == False:
                            yaku['dora'] = 1
                        else:
                            yaku['dora'] += 1
            elif doraList[i][:2] in sList:
                indexNum = sList.index(doraList[i][:2])
                if indexNum == len(sList) - 1:
                    indexNum = 0
                else:
                    indexNum += 1

                for j in range(len(hList)):
                    if hList[j][:2] == sList[indexNum]:
                        if ('dora' in yaku) == False:
                            yaku['dora'] = 1
                        else:
                            yaku['dora'] += 1
            elif doraList[i][:4] in windList:
                indexNum = windList.index(doraList[i][:4])
                if indexNum == len(windList) - 1:
                    indexNum = 0
                else:
                    indexNum += 1

                for j in range(len(hList)):
                    if hList[j][:4] == windList[indexNum]:
                        if ('dora' in yaku) == False:
                            yaku['dora'] = 1
                        else:
                            yaku['dora'] += 1
            elif doraList[i][:4] in sangenhaiList:
                indexNum = sangenhaiList.index(doraList[i][:4])
                if indexNum == len(sangenhaiList) - 1:
                    indexNum = 0
                else:
                    indexNum += 1

                for j in range(len(hList)):
                    if hList[j][:4] == sangenhaiList[indexNum]:
                        if ('dora' in yaku) == False:
                            yaku['dora'] = 1
                        else:
                            yaku['dora'] += 1
                    
        


    #부수계산
    if ('pinfu' in yaku):
        if tsumo == True:
            yaku['fu'] = 20
        else:
            yaku['fu'] = 30
    elif ('chiitoitsu' in yaku):
        yaku['fu'] = 25
    else:
        if tsumo == True:
            yaku['fu'] += 2
        elif huro == False:
            yaku['fu'] += 10

        yaochuhai = ['m1', 'm9', 'p1', 'p9', 's1', 's9', 'ea', 'so', 'we', 'no', 'ha', 'gr', 'ch']
        for i in range(len(status_huro['koutsu'])):
            if status_huro['koutsu'][i][0][:2] in yaochuhai:
                yaku['fu'] += 4
            else:
                yaku['fu'] += 2
        for i in range(len(status_hand['koutsu'])):
            if status_hand['koutsu'][i][0][:2] in yaochuhai:
                yaku['fu'] += 8
            else:
                yaku['fu'] += 4
        for i in range(len(status_huro['kantsu'])):
            ankan = 0
            for j in range(4):
                if status_huro['kantsu'][i][j][-1] == 1:
                    ankan += 1
            if ankan == 4:
                if status_huro['kantsu'][i][0][:2] in yaochuhai:
                    yaku['fu'] += 32
                else:
                    yaku['fu'] += 16
            else:
                if status_huro['kantsu'][i][0][:2] in yaochuhai:
                    yaku['fu'] += 16
                else:
                    yaku['fu'] += 8

        if (status_hand['toitsu'][0][0][:4] in sangenhai) or status_hand['toitsu'][0][0] == gameInfo['kyoku'][:-1] or status_hand['toitsu'][0][0] == playerInfo['wind']:
            if status_hand['toitsu'][0][0] == gameInfo['kyoku'][:-1] == playerInfo['wind']:
                yaku['fu'] += 4
            else:
                yaku['fu'] += 2

        if not(len(status_original['toitsu']) == 2 or len(status_original['ryantatsu']) == 1):
            yaku['fu'] += 2

    return yaku

##################################################################



############################## Score ##############################

def ScoreCalculate(SCREEN, yaku, player, *target):
    global p1Hand, p2Hand, p3Hand, p4Hand
    global p1Info, p2Info, p3Info, p4Info
    global p1Discard, p2Discard, p3Discard, p4Discard
    global handList, cardList
    global mouseInButton


    textScore_P1_Original = textFont.render(str(p1Info['score']), True, textColor)
    textScore_P2_Original = textFont.render(str(p2Info['score']), True, textColor)
    textScore_P3_Original = textFont.render(str(p3Info['score']), True, textColor)
    textScore_P4_Original = textFont.render(str(p4Info['score']), True, textColor)

        
    score = 0

    if ('dora' in yaku) == True:
        yaku['fan'] += yaku['dora']

    if yaku['fan'] >= 5 or yaku['yakuman'] != 0:
        if yaku['yakuman'] >= 1:
            score = 8000 * yaku['yakuman']
        elif yaku['fan'] == 5:
            score = 2000
        elif yaku['fan'] == 6 or yaku['fan'] == 7:
            score = 3000
        elif yaku['fan'] == 8 or yaku['fan'] == 9 or yaku['fan'] == 10:
            score = 4000
        elif yaku['fan'] == 11 or yaku['fan'] == 12:
            score = 6000
        elif yaku['fan'] >= 13:
            score = 8000

    else:
        #부수계산
        if 'chiitoitsu' in yaku:
            score = yaku['fu'] * (2 ** (2 + yaku['fan']))
        else:
            if yaku['fu'] % 10 != 0:
                yaku['fu'] = (yaku['fu'] // 10 + 1) * 10
                
            if (yaku['fan'] == 4 and yaku['fu'] >= 40) or (yaku['fan'] == 3 and yaku['fu'] >= 70):
                score = 2000
            else:
                score = yaku['fu'] * (2 ** (2 + yaku['fan']))

    oya = ''
    score_1 = 0
    score_2 = 0
    scoreTotal = 0
    #쯔모
    if len(target) == 0:
        oya = ''
        for i in range(1, 5):
            if eval('p' + str(i) + 'Info')['wind'] == 'east':
                oya = 'p' + str(i)
                break

        if oya == player:
            score *= 2

        if score % 100 != 0:
            score_1 = (score // 100 + 1) * 100
        else:
            score_1 = score

        if (score * 2) % 100 != 0:
            score_2 = ((score * 2) // 100 + 1) * 100
        else:
            score_2 = score * 2


        score_1 += (300 * gameInfo['renchan']) // 3
        score_2 += (300 * gameInfo['renchan']) // 3
            
            
        for i in range(1, 5):
            if 'p' + str(i) != player:
                if oya == 'p' + str(i):
                    eval('p' + str(i) + 'Info')['score'] -= score_2
                else:
                    eval('p' + str(i) + 'Info')['score'] -= score_1

        if oya == player:
            scoreTotal = score_1 * 3
            eval(player + 'Info')['score'] += scoreTotal
        else:
            scoreTotal += score_1 * 2 + score_2
                
            eval(player + 'Info')['score'] += scoreTotal

    #론
    else:
        if eval(player + 'Info')['wind'] == 'east':
            score *= 6
        else:
            score *= 4

        if score % 100 != 0:
            scoreTotal = (score // 100 + 1) * 100
        else:
            scoreTotal = score


        scoreTotal += 300 * gameInfo['renchan']
            
        
        eval(target[0] + 'Info')['score'] -= scoreTotal
        eval(player + 'Info')['score'] += scoreTotal
            



    #####역, 점수 출력#####
    isInputDone = False
    page = 1
    while True:
        if isInputDone == True:
            isInputDone = False
            if page == 2:
                pygame.time.wait(500)
                return
            else:
                pygame.time.wait(500)
                page += 1

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
                    


        GameScreen(SCREEN, 'clear')

        #사각형
        pygame.draw.rect(SCREEN, Color(150, 150, 150, 150), Rect(200, 50, disSize_w - 400, disSize_h - 100))
        
        #확인 버튼
        pygame.draw.rect(SCREEN, buttonColor, enterButton)
        SCREEN.blit(textEnter, (enterButton.x, enterButton.y))


        #현재 국 출력
        kyokuPos_x = disSize_w // 2 - cardSize_p1.w * 2
        kyokuPos_y = disSize_h // 8 - cardSize_p1.h // 4
        if gameInfo['ba'] == gameInfo['kyoku'][:-1] and gameInfo['kyoku'][-1] == '4':
            SCREEN.blit(text_allLast, (kyokuPos_x, kyokuPos_y))
        else:
            if gameInfo['kyoku'][:-1] == 'east':
                SCREEN.blit(eval('text_' + gameInfo['kyoku'][:-1] + '_s'), (kyokuPos_x, kyokuPos_y))
            else:
                SCREEN.blit(eval('text_' + gameInfo['kyoku'][:-1]), (kyokuPos_x, kyokuPos_y))
            SCREEN.blit(eval('text' + gameInfo['kyoku'][-1]), (kyokuPos_x + cardSize_p1.w // 2 + 7, kyokuPos_y))
            SCREEN.blit(text_kyoku, (kyokuPos_x + cardSize_p1.w, kyokuPos_y))

        #본장 출력
        renchanPos_x = kyokuPos_x + cardSize_p1.w // 2 * 5
        renchanPos_y = kyokuPos_y

        if gameInfo['renchan'] // 10 != 0:
            SCREEN.blit(eval('text' + str(gameInfo['renchan'] // 10)), (renchanPos_x - 15, renchanPos_y))
        SCREEN.blit(eval('text' + str(gameInfo['renchan'] % 10)), (renchanPos_x, renchanPos_y))
        SCREEN.blit(text_renchan, (renchanPos_x + cardSize_p1.w // 2, renchanPos_y))


                        
        #패
        cardScorePos_x = disSize_w // 2 - (cardSize_p1.w * 8)
        cardScorePos_y = disSize_h // 8 + cardSize_p1.h
        for i in range(len(eval(player + 'Hand'))):
            if len(eval(player + 'Hand')) % 3 == 2 and i == len(eval(player + 'Hand')) - 1:
                cardScorePos_x += 10
                SCREEN.blit(pygame.transform.scale(eval(eval(player + 'Hand')[i]), smallChangeSize), (cardScorePos_x, cardScorePos_y - 5), cardSize_p1)
            else:
                SCREEN.blit(pygame.transform.scale(eval(eval(player + 'Hand')[i]), smallChangeSize), (cardScorePos_x, cardScorePos_y), cardSize_p1)
            cardScorePos_x += cardSize_p1.w

        if len(eval(player + 'Hand')) % 3 != 2:
            cardScorePos_x += 10
            if len(target) == 1:
                SCREEN.blit(pygame.transform.scale(eval(eval(target[1] + 'Discard')[-1]), smallChangeSize), (cardScorePos_x, cardScorePos_y - 10), cardSize_p1)
            elif len(target) == 2:
                SCREEN.blit(pygame.transform.scale(eval(target[1]), smallChangeSize), (cardScorePos_x, cardScorePos_y - 10), cardSize_p1)
            cardScorePos_x += cardSize_p1.w


        #운 패
        if len(eval(player + 'Info')['huro']) != 0:
            cardScorePos_x += 20
            for i in range(1, len(eval(player + 'Info')['huro']) + 1):
                count = 0
                kanIndex = -1
                for j in range(len(eval(player + 'Info')['huro'][-i])):
                    if eval(player + 'Info')['huro'][-i][j][-1] != '1':
                        count += 1
                        if count == 2:
                            kanIndex = j
                for j in range(len(eval(player + 'Info')['huro'][-i])):
                    if count == 0:
                        if j == 0 or j == 3:
                            SCREEN.blit(pygame.transform.scale(back, smallChangeSize), (cardScorePos_x, cardScorePos_y), cardSize_p1)
                            cardScorePos_x += cardSize_p1.w
                        else:
                            SCREEN.blit(pygame.transform.scale(eval(eval(player + 'Info')['huro'][-i][j][:-1]), smallChangeSize), (cardScorePos_x, cardScorePos_y), cardSize_p1)
                            cardScorePos_x += cardSize_p1.w
                    else:
                        if eval(player + 'Info')['huro'][-i][j][-1] == '1':
                            SCREEN.blit(pygame.transform.scale(eval(eval(player + 'Info')['huro'][-i][j][:-1]), smallChangeSize), (cardScorePos_x, cardScorePos_y), cardSize_p1)
                            cardScorePos_x += cardSize_p1.w
                        else:
                            if j == kanIndex - 1:
                                SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(eval(player + 'Info')['huro'][-i][j][:-1]), smallChangeSize), p2Degree), (cardScorePos_x, cardScorePos_y - (cardSize_p2.h - cardSize_p2.w)), cardSize_p2)
                            elif j == kanIndex:
                                SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(eval(player + 'Info')['huro'][-i][j][:-1]), smallChangeSize), p2Degree), (cardScorePos_x, cardScorePos_y - cardSize_p2.h - (cardSize_p2.h - cardSize_p2.w)), cardSize_p2)
                                cardScorePos_x += cardSize_p2.w
                            else:
                                SCREEN.blit(pygame.transform.rotate(pygame.transform.scale(eval(eval(player + 'Info')['huro'][-i][j][:-1]), smallChangeSize), p2Degree), (cardScorePos_x, cardScorePos_y - (cardSize_p2.h - cardSize_p2.w)), cardSize_p2)
                                cardScorePos_x += cardSize_p1.h


        #역
        if page == 1:
            yakuPos_x = disSize_w // 2 - (cardSize_p1.w * 7)
            yakuPos_y = disSize_h // 4 + cardSize_p1.h

            yakuDisList = ['fan', 'yakuman', 'fu']
            for i in yaku.keys():
                if (i in yakuDisList) == False:
                    SCREEN.blit(eval('text_' + i), (yakuPos_x, yakuPos_y))
                    SCREEN.blit(eval('text' + str(yaku[i] % 10)), (yakuPos_x + cardSize_p1.w * 3 + 18, yakuPos_y))
                    if yaku[i] // 10 != 0:
                        SCREEN.blit(eval('text' + str(yaku[i] // 10)), (yakuPos_x + cardSize_p1.w * 3 + 3, yakuPos_y))
                    SCREEN.blit(text_fan, (yakuPos_x + cardSize_p1.w * 4, yakuPos_y))
                    yakuPos_y += 40

            #도라
            doraPos_x = disSize_w // 2 + cardSize_p1.w * 2
            doraPos_y = disSize_h // 4 + cardSize_p1.h + 10
            
            for i in range(gameInfo['kan'] + 1):
                SCREEN.blit(pygame.transform.scale(eval(cardList[-6 + gameInfo['kan'] - (i * 2)]), smallChangeSize), (doraPos_x + (cardSize_p1.w * i), doraPos_y), cardSize_p1)
                if ('riichi' in yaku) or ('doubleriichi' in yaku):
                    SCREEN.blit(pygame.transform.scale(eval(cardList[-6 + gameInfo['kan'] + 1 - (i * 2)]), smallChangeSize), (doraPos_x + (cardSize_p1.w * i), doraPos_y + cardSize_p1.h), cardSize_p1)

            #총 판수, 부수, 점수 출력
            totalFuFanPos_x = disSize_w // 2 + cardSize_p1.w // 2 * 5
            totalFuFanPos_y = disSize_h // 4 * 3 - cardSize_p1.h * 2
            
            #부
            SCREEN.blit(eval('text' + str(yaku['fu'] % 10)), (totalFuFanPos_x + 18, totalFuFanPos_y))
            if yaku['fu'] // 10 != 0:
                SCREEN.blit(eval('text' + str(yaku['fu'] // 10)), (totalFuFanPos_x + 3, totalFuFanPos_y))
            SCREEN.blit(text_fu, (totalFuFanPos_x + cardSize_p1.w, totalFuFanPos_y))
            
            #판
            if yaku['yakuman'] != 0:
                yakumanTotal = yaku['yakuman'] * 13
                SCREEN.blit(eval('text' + str(yakumanTotal % 10)), (totalFuFanPos_x + cardSize_p1.w * 2 + 18, totalFuFanPos_y))
                if yakumanTotal // 10 != 0:
                    SCREEN.blit(eval('text' + str(yakumanTotal // 10)), (totalFuFanPos_x + cardSize_p1.w * 2 + 3, totalFuFanPos_y))
                SCREEN.blit(text_fan, (totalFuFanPos_x + cardSize_p1.w * 3, totalFuFanPos_y))
            else:
                SCREEN.blit(eval('text' + str(yaku['fan'] % 10)), (totalFuFanPos_x + cardSize_p1.w * 2 + 18, totalFuFanPos_y))
                if yaku['fan'] // 10 != 0:
                    SCREEN.blit(eval('text' + str(yaku['fan'] // 10)), (totalFuFanPos_x + cardSize_p1.w * 2 + 3, totalFuFanPos_y))
                SCREEN.blit(text_fan, (totalFuFanPos_x + cardSize_p1.w * 3, totalFuFanPos_y))

            #점수
            scorePos_x = disSize_w // 2 + cardSize_p1.w // 2 * 5
            scorePos_y = disSize_h // 4 * 3 - cardSize_p1.h - 10
            
            if yaku['yakuman'] != 0:
                if yaku['yakuman'] == 1:
                    SCREEN.blit(text_yakuman, (scorePos_x, scorePos_y))
                elif yaku['yakuman'] == 2:
                    SCREEN.blit(text_doubleyakuman, (scorePos_x, scorePos_y))
                elif yaku['yakuman'] == 3:
                    SCREEN.blit(text_tripleyakuman, (scorePos_x, scorePos_y))
            elif (yaku['fan'] == 4 and yaku['fu'] >= 40) or (yaku['fan'] == 3 and yaku['fu'] >= 70) or yaku['fan'] == 5:
                SCREEN.blit(text_mangan, (scorePos_x, scorePos_y))
            elif yaku['fan'] == 6 or yaku['fan'] == 7:
                SCREEN.blit(text_haneman, (scorePos_x, scorePos_y))
            elif yaku['fan'] == 8 or yaku['fan'] == 9 or yaku['fan'] == 10:
                SCREEN.blit(text_baiman, (scorePos_x, scorePos_y))
            elif yaku['fan'] == 11 or yaku['fan'] == 12:
                SCREEN.blit(text_sanbaiman, (scorePos_x, scorePos_y))
            elif yaku['fan'] >= 13:
                SCREEN.blit(text_kazoeyakuman, (scorePos_x, scorePos_y))
            else:
                text_score = textFont_big.render(str(scoreTotal), True, textColor)
                SCREEN.blit(text_score, (scorePos_x, scorePos_y))
            

            

        #점수
        elif page == 2:
            textScore_Score_Total = textFont.render('+' + str(scoreTotal), True, Color('blue'))
            
            p1ScorePos = (disSize_w // 2 - 50, disSize_h // 4 * 3 - 98)
            p1ScorePos_s = (p1ScorePos[0] + 30, p1ScorePos[1] + 30)
            p2ScorePos = (disSize_w // 4 * 3 - 180, disSize_h // 2 - 20)
            p2ScorePos_s = (p2ScorePos[0] + 30, p2ScorePos[1] + 30)
            p3ScorePos = (disSize_w // 2 - 50, disSize_h // 4 + 50)
            p3ScorePos_s = (p3ScorePos[0] + 30, p3ScorePos[1] + 30)
            p4ScorePos = (disSize_w // 4 + 90, disSize_h // 2 - 20)
            p4ScorePos_s = (p4ScorePos[0] + 30, p4ScorePos[1] + 30)

            p1WindPos = (disSize_w // 2 - 20, disSize_h // 2 + 35)
            p2WindPos = (disSize_w // 2 + 30, disSize_h // 2 - 15)
            p3WindPos = (disSize_w // 2 - 20, disSize_h // 2 - 65)
            p4WindPos = (disSize_w // 2 - 70, disSize_h // 2 - 15)
            
        
            #쯔모
            if len(target) == 0:
                textScore_Score_1 = textFont.render('-' + str(score_1), True, Color('red'))
                textScore_Score_2 = textFont.render('-' + str(score_2), True, Color('red'))


                SCREEN.blit(textScore_P1_Original, p1ScorePos)
                if player == 'p1':
                    SCREEN.blit(textScore_Score_Total, p1ScorePos_s)
                elif oya == 'p1':
                    SCREEN.blit(textScore_Score_2, p1ScorePos_s)
                else:
                    SCREEN.blit(textScore_Score_1, p1ScorePos_s)

                SCREEN.blit(textScore_P2_Original, p2ScorePos)
                if player == 'p2':
                    SCREEN.blit(textScore_Score_Total, p2ScorePos_s)
                elif oya == 'p2':
                    SCREEN.blit(textScore_Score_2, p2ScorePos_s)
                else:
                    SCREEN.blit(textScore_Score_1, p2ScorePos_s)

                SCREEN.blit(textScore_P3_Original, p3ScorePos)
                if player == 'p3':
                    SCREEN.blit(textScore_Score_Total, p3ScorePos_s)
                elif oya == 'p3':
                    SCREEN.blit(textScore_Score_2, p3ScorePos_s)
                else:
                    SCREEN.blit(textScore_Score_1, p3ScorePos_s)

                SCREEN.blit(textScore_P4_Original, p4ScorePos)
                if player == 'p4':
                    SCREEN.blit(textScore_Score_Total, p4ScorePos_s)
                elif oya == 'p4':
                    SCREEN.blit(textScore_Score_2, p4ScorePos_s)
                else:
                    SCREEN.blit(textScore_Score_1, p4ScorePos_s)

            #론
            else:
                textScore_Score_1 = textFont.render('-' + str(scoreTotal), True, Color('red'))
                textScore_Score_Total = textFont.render('+' + str(scoreTotal), True, Color('blue'))

        
                SCREEN.blit(textScore_P1_Original, p1ScorePos)
                if player == 'p1':
                    SCREEN.blit(textScore_Score_Total, p1ScorePos_s)
                elif target[0] == 'p1':
                    SCREEN.blit(textScore_Score_1, p1ScorePos_s)

                SCREEN.blit(textScore_P2_Original, p2ScorePos)
                if player == 'p2':
                    SCREEN.blit(textScore_Score_Total, p2ScorePos_s)
                elif target[0] == 'p2':
                    SCREEN.blit(textScore_Score_1, p2ScorePos_s)

                SCREEN.blit(textScore_P3_Original, p3ScorePos)
                if player == 'p3':
                    SCREEN.blit(textScore_Score_Total, p3ScorePos_s)
                elif target[0] == 'p3':
                    SCREEN.blit(textScore_Score_1, p3ScorePos_s)

                SCREEN.blit(textScore_P4_Original, p4ScorePos)
                if player == 'p4':
                    SCREEN.blit(textScore_Score_Total, p4ScorePos_s)
                elif target[0] == 'p4':
                    SCREEN.blit(textScore_Score_1, p4ScorePos_s)
        

            #바람
            SCREEN.blit(eval('text_' + p1Info['wind']), p1WindPos)
            SCREEN.blit(eval('text_' + p2Info['wind']), p2WindPos)
            SCREEN.blit(eval('text_' + p3Info['wind']), p3WindPos)
            SCREEN.blit(eval('text_' + p4Info['wind']), p4WindPos)

        
        pygame.display.flip()
        clock.tick(TARGET_FPS)



def PrintScoreTotal(SCREEN, *printType):
    global gameInfo, p1Info, p2Info, p3Info, p4Info
    global mouseInButton


    pygame.time.wait(500)
    
    isInputDone = False
    while True:
        if isInputDone == True:
            pygame.time.wait(500)
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
                    


        GameScreen(SCREEN, 'clear')

        #사각형
        pygame.draw.rect(SCREEN, Color(150, 150, 150, 150), Rect(200, 50, disSize_w - 400, disSize_h - 100))
        
        #확인 버튼
        pygame.draw.rect(SCREEN, buttonColor, enterButton)
        SCREEN.blit(textEnter, (enterButton.x, enterButton.y))


        #현재 국 출력
        kyokuPos_x = disSize_w // 2 - cardSize_p1.w * 2
        kyokuPos_y = disSize_h // 8 - cardSize_p1.h // 4
        if gameInfo['ba'] == gameInfo['kyoku'][:-1] and gameInfo['kyoku'][-1] == '4':
            SCREEN.blit(text_allLast, (kyokuPos_x, kyokuPos_y))
        else:
            if gameInfo['kyoku'][:-1] == 'east':
                SCREEN.blit(eval('text_' + gameInfo['kyoku'][:-1] + '_s'), (kyokuPos_x, kyokuPos_y))
            else:
                SCREEN.blit(eval('text_' + gameInfo['kyoku'][:-1]), (kyokuPos_x, kyokuPos_y))
            SCREEN.blit(eval('text' + gameInfo['kyoku'][-1]), (kyokuPos_x + cardSize_p1.w // 2 + 7, kyokuPos_y))
            SCREEN.blit(text_kyoku, (kyokuPos_x + cardSize_p1.w, kyokuPos_y))

        #본장 출력
        renchanPos_x = kyokuPos_x + cardSize_p1.w // 2 * 5
        renchanPos_y = kyokuPos_y

        if gameInfo['renchan'] // 10 != 0:
            SCREEN.blit(eval('text' + str(gameInfo['renchan'] // 10)), (renchanPos_x - 15, renchanPos_y))
        SCREEN.blit(eval('text' + str(gameInfo['renchan'] % 10)), (renchanPos_x, renchanPos_y))
        SCREEN.blit(text_renchan, (renchanPos_x + cardSize_p1.w // 2, renchanPos_y))


        #점수, 바람 출력
        p1ScorePos = (disSize_w // 2 - 45, disSize_h // 4 * 3 - 85)
        p2ScorePos = (disSize_w // 4 * 3 - 180, disSize_h // 2 - 38)
        p3ScorePos = (disSize_w // 2 - 45, disSize_h // 4 + 5)
        p4ScorePos = (disSize_w // 4 + 100, disSize_h // 2 - 38)

        text_Score_p1 = textFont.render(str(p1Info['score']), True, textColor)
        text_Score_p2 = textFont.render(str(p2Info['score']), True, textColor)
        text_Score_p3 = textFont.render(str(p3Info['score']), True, textColor)
        text_Score_p4 = textFont.render(str(p4Info['score']), True, textColor)


        p1WindPos = (disSize_w // 2 - 20, disSize_h // 2 + 10)
        p2WindPos = (disSize_w // 2 + 30, disSize_h // 2 - 40)
        p3WindPos = (disSize_w // 2 - 20, disSize_h // 2 - 90)
        p4WindPos = (disSize_w // 2 - 70, disSize_h // 2 - 40)
        

        SCREEN.blit(text_Score_p1, p1ScorePos)
        SCREEN.blit(text_Score_p2, p2ScorePos)
        SCREEN.blit(text_Score_p3, p3ScorePos)
        SCREEN.blit(text_Score_p4, p4ScorePos)

        SCREEN.blit(eval('text_' + p1Info['wind']), p1WindPos)
        SCREEN.blit(eval('text_' + p2Info['wind']), p2WindPos)
        SCREEN.blit(eval('text_' + p3Info['wind']), p3WindPos)
        SCREEN.blit(eval('text_' + p4Info['wind']), p4WindPos)


        if len(printType) != 0:
            if type(printType[0]) == type([]):
                tenCount = 0
                for i in range(4):
                    if printType[0][i] == True:
                        tenCount += 1

                score_NoTen = 0
                score_Ten = 0
                if 1 <= tenCount and tenCount <= 3:
                    score_NoTen = 3000 // (4 - tenCount)
                    score_Ten = 3000 // tenCount
                    text_Score_NoTen = textFont.render('-' + str(score_NoTen), True, Color('red'))
                    text_Score_Ten = textFont.render('+' + str(score_Ten), True, Color('blue'))

                for i in range(1, 5):
                    if printType[0][i - 1] == True:
                        SCREEN.blit(text_Ten, (eval('p' + str(i) + 'ScorePos')[0], eval('p' + str(i) + 'ScorePos')[1] - 35))
                        if 1 <= tenCount and tenCount <= 3:
                            SCREEN.blit(text_Score_Ten, (eval('p' + str(i) + 'ScorePos')[0] + 30, eval('p' + str(i) + 'ScorePos')[1] + 30))
                    else:
                        SCREEN.blit(text_NoTen, (eval('p' + str(i) + 'ScorePos')[0], eval('p' + str(i) + 'ScorePos')[1] - 35))
                        if 1 <= tenCount and tenCount <= 3:
                            SCREEN.blit(text_Score_NoTen, (eval('p' + str(i) + 'ScorePos')[0] + 30, eval('p' + str(i) + 'ScorePos')[1] + 30))

            if printType[0] == 'end':
                SCREEN.blit(text_gameEnd, (disSize_w // 3 * 2 - 50, disSize_h // 3 * 2))
            else:
                SCREEN.blit(text_kyukyoku, (disSize_w // 3 * 2, disSize_h // 3 * 2))



        pygame.display.flip()
        clock.tick(TARGET_FPS)
        
###################################################################

