#If you want to make it harmful add the while loop where i have given and the make sure to add these additional lines
import pyautogui as pg
#og.FAILSAFE = True
#While True:
#pg.moveTo(X,Y) Mouse Co-rdinates
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


