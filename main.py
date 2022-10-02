import os.path
import sys
from pprint import pprint
import tkinter
from tinytag import TinyTag
from tkinter import Tk
from tkinter import filedialog

form = tkinter.Tk()
form.title("FrameToPhoto")
form.geometry("300x400")
lblInfo = tkinter.Label(form, text="Movie to Photo app",
                        font=("Times New Roman", 20), fg="#8A32F3")

lblInfo.grid(row=0, column=5, sticky="we")


def set_video_name(filename1):
    vid = TinyTag.get(f"UploadVideoHere/{filename1}")
    print("Duration: " + str(vid.duration) + " seconds")


name2 = ""


def browse_button():
    global name2
    filename = filedialog.askopenfilename(
        initialdir="C:\\Users\\kubeczek\\PycharmProjects\\FrameToPhoto\\UploadVideoHere")
    filename1 = os.path.basename(filename)
    split_tup = os.path.splitext(filename1)
    file_name = split_tup[0]
    file_extension = split_tup[1]
    name2 = filename1
    if file_extension == ".mp4":
        print(file_name)
        set_video_name(filename1)
    else:
        print("Please select mp4 file")
def open_folder():
    path = "C:/Users/kubeczek/PycharmProjects/FrameToPhoto/UploadVideoHere"
    path = os.path.realpath(path)
    os.startfile(path)

button2 = tkinter.Button(text="Select file", command=browse_button, bg="#8A32F3", fg="white", activebackground="#321356", activeforeground="white")
button2.grid(row=5, column=1, columnspan=5)
button2.place(relx=0.5, rely=0.5, anchor='center')
button3 = tkinter.Button(text="Open folder", command=open_folder, bg="#8A32F3", fg="white", activebackground="#321356", activeforeground="white")
button3.grid(row=5, column=1, columnspan=6)
button3.place(relx=0.5, rely=0.5)
tkinter.mainloop()
