#stupid script that keeps mouse moving to prevent youtube 
# navbar hiding in fullscreen mode
import pyautogui as pag
import time

pag.FAILSAFE = True
print('move cursor to top left of screen to quit.')
print('Press Ctrl-C to quit.')
print('Press Ctrl-Alt-Del to quit.')

#click top right settings tab
pag.moveTo(1900, 10, duration = 0.5)
pag.click(button='left')
time.sleep(0.1)

#click settings icon
pag.moveTo(1670, 260, duration = 0.5)
pag.click(button='left')
time.sleep(1)

#click sound icon
pag.moveTo(600, 720, duration = 0.5)
pag.click(button='left')

#click digital output
pag.moveTo(1400, 520, duration = 0.5)
pag.click(button='left')

#click toggle on/off
pag.moveTo(1400, 290, duration = 0.5)
pag.click(button='left')

#click exit
pag.moveTo(1457, 212, duration = 0.5)
pag.click(button='left')