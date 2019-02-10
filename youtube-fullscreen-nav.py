#stupid script that keeps mouse moving to prevent youtube 
# navbar hiding in fullscreen mode
import pyautogui as pag
import time

pag.FAILSAFE = True
print('move cursor to top left of screen to quit.')
print('Press Ctrl-C to quit.')
print('Press Ctrl-Alt-Del to quit.')

for i in range(9999):
    pag.moveTo(3, 3, duration = 1.0)
    time.sleep(0.5)
    pag.moveTo(4, 4, duration = 1.0)
    time.sleep(0.5)