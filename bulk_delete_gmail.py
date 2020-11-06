import pyautogui as pag
import time

pag.FAILSAFE = True # always set FAILSAFE to True

print('\n To stop the script, press ctrl+C or jam mouse to top-left of pc screen \n')
print(f'Current coordinate of your mouse pointer: {pag.position()}')
print('replace location A and location B below with it \n')


def runit():
    for i in range(30): # repeat 30 times

        pag.click(504, 251) # location A
        time.sleep(1)

        pag.click(655, 255) # location B
        time.sleep(3)

        print(f'deleting page no.: {i + 1}...')


# runit() #uncomment this line to run full script