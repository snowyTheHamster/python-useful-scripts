# Useful Python Scripts

A bunch of python scripts using pyautogui.


## youtube-fullscreen-nav.py

Display the Navbar during Youtube fullscreen mode.

Have **pyautogui** contantly move the mouse so the navigation bar remains open while watching Youtube videos in Fullscreen mode.

**You can stop the script by:**

- Move the mouse to the top left corner of the screen
- open the terminal running the script and press ctrl+c


## python download youtube video or audio

#### installation:
```
pip install youtube-dl
sudo apt-get install ffmpeg
```

#### to dl & convert to audio (replace video id):
```
python -m youtube_dl --restrict-filenames --ignore-errors -x --audio-format mp3 7ku4WbWEQPU
```

#### to get formats for vid:
```
python -m youtube_dl --restrict-filenames --list-formats 7ku4WbWEQPU
```

#### to dl vid with specific format:
```
python -m youtube_dl --restrict-filenames 7ku4WbWEQPU - 249
```

## surfacego-res

Quickly switch between screen resolutions on the surface go tablet.

convert the script to executables for quick access.

## rename_bulk.py

A short example script to bulk rename files in a directory.



# bulk delete gmail and icloud

Some simple scripts to help bulk delete messages in gmail and icloud.

Using python and pyautogui.

### note

- Use at your own risk
- Don't run script unattended
- script just follows a routine, it will delete important mails if your not careful

### delete gmails
Gmail delete script just clicks two defined locations on screen X amount of times. You need to filter the mail yourself before running the script.

### delete icloud mails
You need to provide the search terms in the icloud script.

The script will:

- Fill in the search term
- Will check whether inbox is empty or not based on certain pixel values
- If inbox not empty, will select all message for deletion and repeat check
- If inbox empty will repeat process with next search term

It's recommended to select the **From** criteria to filter emails for deletion.


### install

```
mkdir projectfolder
cd projectfolder
python -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### customize

- customize the scripts before running.

### run

```
python bulk_delete_gmail.py
python bulk_delete_icloud_mail.py
```

