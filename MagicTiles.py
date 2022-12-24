import pyautogui as pg
import pygetwindow as gw
import pywinauto
import keyboard
from PIL import ImageGrab
import warnings
warnings.simplefilter('ignore', category=UserWarning)

win = gw.getWindowsWithTitle("게임핵(리듬게임)")[0]
if win.isActive == False :
    pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()

Gameover = False
loc_y = 0
loc_x = [0,0,0]
keys = ['1','2','3','4']
while(not Gameover):
    if win.isActive == False :
        win.activate()
    i_win = [win.left, win.top, win.size]
    loc_y = int(i_win[2][1] * (0.64))
    loc_x = [int(i_win[2][0] * (0.12)),
            int(i_win[2][0] * (0.39)), 
            int(i_win[2][0] * (0.63)),
            int(i_win[2][0] * (0.88))]
    screen = ImageGrab.grab()
    for i in range(4):
        if(screen.getpixel((i_win[0]+loc_x[i],i_win[1]+loc_y)) == (0,0,0)):
            pg.press(keys[i])
    
    if keyboard.is_pressed('p'):
        Gameover = True
        break
