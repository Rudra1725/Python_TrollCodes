import webbrowser as wb
import time
import random
import pyautogui as pg 
pg.FAILSAFE = False
time.sleep(2)

while True:
    pg.moveTo(0, 0,duration = 0.50)
    link = [" "] #Just put here funny or 18+ website to prank your friend.
    choice = random.choice(link)
    time.sleep(1)
    wb.open(choice)
   
    



