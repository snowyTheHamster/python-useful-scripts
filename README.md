# youtube show navbar during fullscreen mode

A python script that uses the pyautogui library to move the mouse constantly at to keep the youtube navbar open during fullscreen mode.

## How to use this script

- Install python
- Create a project folder and clone this repo:

```
git clone https://github.com/snowyTheHamster/youtube-fullscreen-navbar.git .
```

- Set up a virtual environment:

```
virtualenv .venv
```

- activate the virtual environment:

```
source .venv/bin/activate
```

or for windows:

```
source .venv/script/activate
```

- install the required packages from the requirements.txt file:

```
pip install -r requirements.txt
```

(linux user may need to also install xlib)

- Run the script:

```
python begin.py
```

The mouse should move to near the top left corner of the screen and keep moving.

### How to edit

To edit the script, open begin.py and change the settings such as time or mouse location.


### How to stop the script

You can stop the script by:

- push the mouse to the top left corner of the screen
- open the terminal running the script and press ctrl+c

Enjoy watching Youtube in Fullscreen mode with the navbar.