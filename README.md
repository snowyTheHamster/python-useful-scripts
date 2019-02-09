# Display Navbar during Youtube fullscreen mode

A stupid python script using **pyautogui**.

Mouse keeps moving so the Youtube navbar stays open during fullscreen Playback.

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


### How to stop the script

You can stop the script by:

- Move the mouse to the top left corner of the screen
- open the terminal running the script and press ctrl+c

Enjoy watching Youtube in Fullscreen mode with the navbar.