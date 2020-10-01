import os
import glob

mylist = [f for f in glob.glob("*.m4v")]
for vid in mylist:
    vidorig = vid
    vid = vid.split('-')[-1]

    if len(vid) < 6:
        vid = "0" + vid
        # print(vidorig)
        # print(vid)
        os.rename(vidorig, vid)
    else:
        # print(vidorig)
        # print(vid)
        os.rename(vidorig, vid)