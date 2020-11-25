import cv2
from tkinter import Tk
from tkinter.filedialog import askopenfilename

def hault():
    while True:
        key = cv2.waitKey(80) & 0xFF

        if key == ord('h'):
            break

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing

file_path = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(file_path)

cam = cv2.VideoCapture(file_path)

filename = file_path.rsplit('/', 1)[1]
print(filename)

FRAME_NUM = 0

#list of crop frames
crop_frames = [155]

while True:
    ret, img = cam.read()

    if not ret:
        break

    FRAME_NUM += 1

    if FRAME_NUM in crop_frames:
        cv2.imwrite("{}_{}.jpg".format(filename, FRAME_NUM), img)

    cv2.putText(img, "{}".format(FRAME_NUM), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 2)

    cv2.imshow("frames", img)

    key = cv2.waitKey(50) & 0xFF

    if key == ord('q'):
        break

    if key == ord('h'):
        hault()

cv2.destroyAllWindows()
cam.release()


