import pyautogui as pag
import time

pag.FAILSAFE = True

# list of search terms
search_terms = [
    'vpn',
    'amazon',
    'drop',
    'zalora',
    'asiaxpat',
    'adobe',
    'uber',
    'flipboard',
    'apple',
    'dhl',
    'twitter',
    'ubuy',
    'groupon',
    'carousell',
    'facebook',
    'paperless',
    'quora',
    'digitalocean',
    'serverpilot',
    'golf',
    'tor',
    'massdrop',
    'getty',
    'bodbot',
    'storyblock',
    'percona',
    'hotels',
    'asana',
    'trip',
    'magento',
    'reward',
    'foodie',
]

# locations to click on
search_bar = (361, 191)
first_msg_area = (281, 285)
trash_btn = (782, 124)

# pixels to check whether inbox is empty or not
xpos = 281
ypositions = [ 270, 275, 280, 285, 290, 295, 300, 305, 310, 315 ]


def checker():
    count = 0
    while count < 1:
        for ypos in ypositions:
            pag.moveTo(xpos, ypos) # move mouse for fun

            # check if pixel area is blank or has text
            if pag.pixelMatchesColor(xpos, ypos, (249, 249, 249) ): # bg color of icloud-mail is #f9f9f9 or rgb(249, 249, 249)
                print(f'testing... pixel is white... empty ?')
                count = 1 # set count to 1, will goto next search_term if loop ends here
            else:
                print('pixel not white, delete messages and repeat \n')

                pag.click(first_msg_area) # click on first message area
                time.sleep(0.5)

                pag.hotkey('ctrl', 'a') # type ctrl+a to select all messages
                time.sleep(2)

                pag.click(trash_btn) # click the trash can button
                time.sleep(10)

                count = 0 # set count to 0, the while loop will continue
                break # break out of current loop

def main():
    for term in search_terms:
        pag.click(search_bar) # click the search bar area
        time.sleep(0.5) # need a slight delay here

        pag.hotkey('ctrl', 'a') # type ctrl+a to select all the text
        time.sleep(0.3)

        pag.typewrite(term) # paste in the search term
        time.sleep(8)

        checker() # run the above checker function


# main() #Uncomment to run
