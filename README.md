# Useful Python Scripts ?


# youtube-fullscreen-nav.py

Display the Navbar during Youtube fullscreen mode.

A stupid python script using **pyautogui**.

We'll have **pyautogui** contantly move the mouse so the navigation bar remains open while watching Youtube videos in Fullscreen mode.

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
python youtube-fullscreen-nav.py
```

The mouse should keep moving near the top left corner of the screen.

### How to edit

Open youtube-fullscreen-nav.py and change the settings such as the time or mouse location.

I set the loop to 9999 but you can change it to an infinite loop if you want.

I usually just interupt the script when changing clips.


### How to stop the script

You can stop the script by:

- Move the mouse to the top left corner of the screen
- open the terminal running the script and press ctrl+c

Enjoy watching Youtube in Fullscreen mode with the navbar.


# ubuntu-digital-output.py

An **pyautogui** script that toggles the sound settings in Ubuntu.

### The Problem

When I boot up my Ubuntu distro, the sound doesn't work properly.

Going into the sound menu and disabling the digital output fixes this but Ubuntu doesn't remember the setting everytime.

Rather than doing this manually, I made a script and ported it as an executable file that resides on my desktop.

Now I just need to double click on this file each time I need to change this setting.

### How to use this script

- Run the script:

```
python ubuntu-digital-output.py
```

### Save script as an executable

To save the script as an executable we can use pyinstaller:

```
pip install pyinstaller
```

To save the script as a single executable file:

```
pyinstaller --onefile ubuntu-digital-output.py
```

This will create a single file in a **dist** folder.

Note: running this on linux will create a linux executable file, running this on Windows will create an exe file.

Note: I ran the pyinstaller command whilst my virtualenv was activated.

I created an executable file for the above youtube fullscreen navbar script too.

Note: (linux) If you get errors about libpython, try running these commands:

```
sudo apt-get install libpython3.7
sudo apt-get install python3-dev
```

You can now run the script by double clicking on the newly made file.