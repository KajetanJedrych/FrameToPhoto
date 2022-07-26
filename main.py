import os.path
import sys
from pprint import pprint
import tkinter
from tinytag import TinyTag
from tkinter import Tk
from tkinter import filedialog
form = tkinter.Tk()
form.title("FrameToPhoto")
form.geometry("1000x600")
lblInfo = tkinter.Label(form, text="Movie to Photo app",
font=("Times New Roman",20),fg="blue")

lblInfo.grid(row=0, column=0, sticky="we")
def set_video_name(filename1):
    vid = TinyTag.get(f"UploadVideoHere/{filename1}")
    print("Duration: " + str(vid.duration) + " seconds")

def browse_button():
    filename = filedialog.askopenfilename(initialdir="C:\\Users\\kubeczek\\PycharmProjects\\FrameToPhoto\\UploadVideoHere")
    filename1 = os.path.basename(filename)
    split_tup =os.path.splitext(filename1)
    file_name = split_tup[0]
    file_extension = split_tup[1]
    if file_extension == ".mp4":
        print(file_name)
        set_video_name(filename1)
    else:
        print("Please select mp4 file")


button2 = tkinter.Button(text="Browse", command=browse_button)
button2.grid(row=1, column=0)
tkinter.mainloop()