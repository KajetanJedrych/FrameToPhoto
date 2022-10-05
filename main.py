import os.path
import sys
import cv2
from pprint import pprint
import tkinter
from tinytag import TinyTag
from tkinter import *
from tkinter import filedialog

form = tkinter.Tk()
form.title("FrameToPhoto")
form.geometry("300x400")
lblInfo = tkinter.Label(form, text="Movie to Photo app",
                        font=("Times New Roman", 20), fg="#8A32F3")
lblInfo.pack(pady=20)
class Test:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.button2 = Button(master, text="Select file", command=self.browse_button, bg="#8A32F3", fg="white",
                                 activebackground="#321356", activeforeground="white", )
        self.button2.pack(pady=10)
        self.button3 = Button(master, text="Select file", command=self.test, bg="#8A32F3", fg="white",
                              activebackground="#321356", activeforeground="white", )
        self.button3.pack(pady=40)


    def browse_button(self):
        filename = filedialog.askopenfilename(
            initialdir="C:\\Users\\kubeczek\\PycharmProjects\\FrameToPhoto\\UploadVideoHere")
        self.filename1 = os.path.basename(filename)
        split_tup = os.path.splitext(self.filename1)
        file_name = split_tup[0]
        file_extension = split_tup[1]
        if file_extension == ".mp4":
            print(file_name)
            set_video_name(self.filename1)
        else:
            print("Please select mp4 file")
    def test(self):
        print(self.filename1)

e = Test(form)

def set_video_name(filename1):
    vid = TinyTag.get(f"UploadVideoHere/{filename1}")
    print("Duration: " + str(vid.duration) + " seconds")


def open_folder():
    path = "C:/Users/kubeczek/PycharmProjects/FrameToPhoto/UploadVideoHere"
    path = os.path.realpath(path)
    os.startfile(path)

tkinter.mainloop()
