#stupid script that keeps mouse moving to prevent youtube 
# navbar hiding in fullscreen mode
import pyautogui as pag
import time

pag.FAILSAFE = True
print('move cursor to top left of screen to quit.')
print('Press Ctrl-C to quit.')
print('Press Ctrl-Alt-Del to quit.')

#click top right settings tab
time.sleep(0.5)
pag.click(1900, 10)
time.sleep(1)

#click settings icon
pag.click(1670, 260)
time.sleep(2)

#click sound icon
pag.click(600, 720)
time.sleep(0.2)

#click line out
pag.click(916, 595)
time.sleep(0.2)

# #click digital output
# pag.moveTo(1400, 520, duration = 0.5)
# pag.click(button='left')

# #click toggle on/off
# pag.moveTo(1400, 290, duration = 0.5)
# pag.click(button='left')

# #click on hdmi output
# pag.moveTo(1400, 490, duration = 0.5)
# pag.click(button='left')

#click exit
pag.click(1457, 212)