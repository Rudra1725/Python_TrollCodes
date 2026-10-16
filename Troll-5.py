import secrets 
import pyautogui as pg

pg.press('win')
pg.sleep(0.30)
pg.write("cmd")
pg.press("enter")
pg.sleep(1)
pg.press('f11')
pg.sleep(0.10)
pg.write('color 8')
pg.press('enter')
pg.write('color c')
pg.press('enter')
pg.write('color a')
pg.press('enter')
pg.sleep(0.10)
pg.write('dir/s')
pg.press('enter')


