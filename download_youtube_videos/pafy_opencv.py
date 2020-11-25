import pafy
import youtube_dl
import cv2
import numpy as np
import tkinter as tk
from tkinter import simpledialog
from tkinter import Checkbutton, BooleanVar, Button, IntVar

ROOT = tk.Tk()

ROOT.withdraw()

# the url input dialog
url = simpledialog.askstring(title="Enter Youtube Video URL",
                                  prompt="URL")


# url = "https://www.youtube.com/watch?v=WOn7m0_aYBw&list=PLwygboCFkeeA2w1fzJm44swdG-NnyB6ip&index=154&t=0s"
video = pafy.new(url)
best = video.getbest(preftype="mp4")

streams = video.streams
for i in streams:
    print(i)

# the Video size selection input dialog
video_size_selector = simpledialog.askstring(title="Enter Video size",
                                  prompt="Select using Number")

cap = cv2.VideoCapture()
cap.open(streams[int(video_size_selector)].url)

frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = cap.get(cv2.CAP_PROP_FPS)

# the Downloaded Video Name in avi input dialog
output_file = simpledialog.askstring(title="Enter Downloaded Video Name without File Format",
                                  prompt="Enter Video Nme")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter("{}.avi".format(output_file),fourcc,
                      fps, (frame_width, frame_height))

print("Video Downloading Start...")
while True:
    ret, frame = cap.read()

    if ret != True:
        continue

    # resized = cv2.resize(frame, (480,640))

    # cv2.imshow('frame',frame)

    out.write(frame)
    print(ret)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()