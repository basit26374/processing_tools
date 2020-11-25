from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

ffmpeg_extract_subclip(filename, 1, 50, targetname="test.avi")