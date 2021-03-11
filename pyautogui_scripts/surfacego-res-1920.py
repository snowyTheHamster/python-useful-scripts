# changes the screen resolution to 1920x1080
# on windows 10
import pyautogui as pag
import time

pag.FAILSAFE = True
print('move cursor to top left of screen to force quit the app.')

# Open Windows "Display Settings"
pag.press('winleft')
pag.typewrite('display settings')
time.sleep(2)
pag.press('enter')
time.sleep(5)

# tab down to the display resolution option
for i in range(10):
    pag.press('tab')
time.sleep(2)

# select the screen resolution here
pag.press('space')
time.sleep(1)
pag.press('pageup')
time.sleep(1)
pag.press('space')
time.sleep(1)

# select "keep changes" if prompted
pag.press('tab')
time.sleep(1)
pag.press('space')
time.sleep(1)

# close window
pag.keyDown('altleft')
pag.keyDown('space')
pag.keyUp('space')
pag.keyUp('altleft')
time.sleep(1)
pag.typewrite('c')
