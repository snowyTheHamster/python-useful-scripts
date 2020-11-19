import pyautogui as pag
import time

pag.FAILSAFE = True # always set FAILSAFE to True

# This script selects one image for each product attribute in Shopify
# You need to define no. of loops & screen position of each img as arguments when running the function

# Define locations of buttons/images on screen
img_loc12 = (884, 446)  # row col 1:2
img_loc13 = (1030, 446) # row col 1:3
img_loc14 = (1168, 446) # row col 1:4
img_loc21 = (730, 590)  # row col 2:1
img_loc22 = (884, 590)  # row col 2:2
img_loc23 = (1030, 590) # row col 2:3
img_loc24 = (1168, 590) # row col 2:4
img_loc31 = (730, 737)  # row col 3:1
img_loc32 = (884, 737)  # row col 3:2
img_loc33 = (1030, 737) # row col 3:3
img_loc34 = (1168, 737) # row col 3:4
add_btn = (1439, 378)
done_btn = (1210, 865)
save_btn = (1509, 127)
next_btn = (1520, 193)
back_btn = (1486, 193)


# arguments: loops, img locations(minimum of 1)
def run_multiple_at_once(x, *img_locs):
    time.sleep(0.2)
    count = 1
    for img_loc in img_locs:
        for i in range(x):
            pag.click(add_btn)
            time.sleep(2.0)
            pag.click(img_loc)
            time.sleep(0.5)
            pag.click(done_btn)
            time.sleep(0.5)
            pag.click(save_btn)
            time.sleep(3.3)
            pag.click(next_btn)
            print(f'added image {count} out of {x * len(img_locs)}')
            count = count + 1
            time.sleep(4)

# run_multiple_at_once(3, (img_loc12), (img_loc23)) #uncomment to run (x times, (img_location tuple), (img_location tuple))
    

# for running manually - no pause after clicking save btn
def run_manual(x, img_loc):
    time.sleep(0.2)
    for i in range(x):
        pag.click(add_btn)
        time.sleep(2.0)
        pag.click(img_loc)
        time.sleep(0.5)
        pag.click(done_btn)
        time.sleep(0.5)
        print(f'added image {i + 1} out of {x}')
        pag.click(save_btn)

# run_manual(1, (img_loc12)) #uncomment to run (x times, img_location)
