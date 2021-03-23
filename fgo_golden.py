import pyscreenshot as ImageGrab
import pyautogui
import time
from PIL import Image

import math
import operator
from functools import reduce

#判斷卡片顏色
def get_main_color(img):
    
    img.thumbnail((200, 200))
    img_values = list(img.getdata())    
    
    red=0
    green=0
    blue=0
    for rgb in img_values:
        red=red+rgb[0]
        green=green+rgb[1]
        blue=blue+rgb[2]
    if(red>green):
        if(red>blue):
            return 'r'
        else:
            return 'b'
    if(green>blue):
        if(green>red):
            return 'g'
        else:
            return 'r'
    if(blue>red):
        if(blue>green):
            return 'b'
        else:
            return 'g'

#取得所有卡片
def get_all_cards(): 
    card1=ImageGrab.grab(bbox=(50,525,225,650)) # X1,Y1,X2,Y2
    card2=ImageGrab.grab(bbox=(300,525,475,650))
    card3=ImageGrab.grab(bbox=(550,525,725,650))
    card4=ImageGrab.grab(bbox=(825,525,1000,650))
    card5=ImageGrab.grab(bbox=(1075,525,1250,650))
    
    card_list=[]

    card_list.append(get_main_color(card1))
    card_list.append(get_main_color(card2))
    card_list.append(get_main_color(card3))
    card_list.append(get_main_color(card4))
    card_list.append(get_main_color(card5))
    print(card_list)
    return card_list
#卡片點擊
def click_card(n):
    if n==1:
        return pyautogui.click(146, 591)
    if n==2:
        return pyautogui.click(399, 603)
    if n==3:
        return pyautogui.click(655, 599)
    if n==4:
        return pyautogui.click(929, 610)
    if n==5:
        return pyautogui.click(1174, 611)
    
#判斷是否可以執行攻擊
def attack_btn():
    img=Image.open('atkBtn.png')
    grab=ImageGrab.grab(bbox=(1110, 566,1159, 704))
    
    h1=img.histogram()
    h2=grab.histogram()
    
    result = math.sqrt(reduce(operator.add,list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1))
    
    if(result<10):
        print('attack!')
        return True
    else:
        print('stay cool.')
        return False
    
#判斷是否結束關卡    
def end_mission():
    img=Image.open('continueBtn.png')
    grab=ImageGrab.grab(bbox=(551, 673,728, 685))
    
    h1=img.histogram()
    h2=grab.histogram()
    
    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    
    if(result<25):
        print('end mission.')
        return True
    else:
        print(result)
        return False
    
#判斷是否在主畫面    
def main_page():
    img=Image.open('mainPage.png')
    grab=ImageGrab.grab(bbox=(398, 693,459, 713))
    
    h1=img.histogram()
    h2=grab.histogram()
    
    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    
    if(result<10):
        print('ready to go.')
        return True
    else:
        return False
    
#開始攻擊    
def start_attack():  
    pyautogui.click(1137,690)
    time.sleep(0.3)
    cards_list=get_all_cards()
    
    if(cards_list.count('g')>=3):
        for i in range(5):
            if(cards_list[i]=='g'):
                click_card(i+1)
    elif(cards_list.count('b')>=3):
        for i in range(5):
            if(cards_list[i]=='b'):
                click_card(i+1)
    else:            
        count=0
        for i in range(3):
            for j in range(len(cards_list)):
                if(cards_list[j]=='r' and i==0 and count<4):
                    click_card(j+1)
                    count=count+1
                if(cards_list[j]=='b' and i==1 and count<4):
                    click_card(j+1)
                    count=count+1
                if(cards_list[j]=='g' and i==2 and count<4):
                    click_card(j+1)
                    count=count+1  
                    
#開始任務---也可用來結束關卡
def start_mission():
    pyautogui.click(1625, 382)#delete all address
    pyautogui.click(1018, 530)#click yes 
    time.sleep(1)
    pyautogui.click(1010, 274)#進關卡
    time.sleep(2.2)
    #pyautogui.click(1010, 274)#選第一個support
    pyautogui.click(967, 479)#選第二個support
    time.sleep(1.5)
    pyautogui.click(1137,690)#開始任務
    time.sleep(1.5)#讀取緩衝
    pyautogui.click(1137,690)
    
#判斷NP是否足夠   
def eat_apple():
    img=Image.open('apple.png')
    grab=ImageGrab.grab(bbox=(337, 317,416, 341))
    
    h1=img.histogram()
    h2=grab.histogram()
    
    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    
    if(result<10):
        print('np is not enough')
        return True
    else:
        return False
 
    
#MAIN------------------------------
for i in range(3):  #周回次數      
    while(True):
        if(main_page()):
            start_mission()
            break 
        else:
            time.sleep(3)
            
    time.sleep(6)        
    pyautogui.click(904, 1017)#execute script
    time.sleep(7)
    
    while(True):
        if(end_mission()):
               
            start_mission() 
            break
        if(attack_btn()):
            pyautogui.click(1137,690)#atk_btn
            time.sleep(2)
            pyautogui.click(385, 250)#寶具
            pyautogui.click(640, 250)
            pyautogui.click(885, 250)
            pyautogui.click(146, 591)#card1
            pyautogui.click(399, 603)#card2
        else:
            time.sleep(3)
            

