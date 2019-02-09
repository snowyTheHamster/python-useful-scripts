# Display Navbar during Youtube fullscreen mode

A stupid python script using **pyautogui**.

We will have **pyautogui** contantly move the mouse so the navigation bar remains open while watching Youtube videos in Fullscreen mode.

Watch Youtube in Fullscreen while still keeping track of the time remaining on the video.

## How to use this script

- Install python
- Create a project folder
- Clone this repo:

```
git clone https://github.com/snowyTheHamster/youtube-fullscreen-navbar.git .
```

- Set up a virtual environment:

```
virtualenv .venv
```

- Activate virtual environment (mac, linux users):

```
source .venv/bin/activate
```

- Activate virtual environment (windows users):

```
source .venv/script/activate
```

- Install required packages from the requirements.txt file:

```
pip install -r requirements.txt
```

(linux user may need to also install xlib)

- Run the script:

```
python begin.py
```

The mouse should keep moving near the top left corner of the screen.

### How to edit

Open begin.py and change the settings such as the time or mouse location.

I set the loop to 9999 but you can change it to an infinite loop if you want.

I usually just interupt the script when changing clips.


### How to stop the script

You can stop the script by:

- Move the mouse to the top left corner of the screen
- open the terminal running the script and press ctrl+c

Enjoy watching Youtube in Fullscreen mode with the navbar.