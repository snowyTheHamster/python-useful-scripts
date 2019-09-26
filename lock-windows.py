# shortcut to lockdown windows

import pyautogui as pag
import time

pag.FAILSAFE = True
print('move cursor to top left of screen to force quit the app.')

# Lock out windows
pag.keyDown('winleft')
pag.keyDown('x')
pag.keyUp('winleft')
pag.keyUp('x')
time.sleep(1)

pag.typewrite('u')
time.sleep(1)

pag.typewrite('i')