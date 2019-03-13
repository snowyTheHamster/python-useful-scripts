import pyautogui as pag
import time

# click and activate hiragana input
pag.click(1760, 16)
time.sleep(0.2)
pag.click(1760, 140)
time.sleep(0.2)
pag.click(1760, 198)
pag.moveTo(81, 772)