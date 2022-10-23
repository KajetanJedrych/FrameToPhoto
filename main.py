import os.path
import cv2
import tkinter
from tinytag import TinyTag
from tkinter import *
from tkinter import filedialog

form = tkinter.Tk()
form.title("FrameToPhoto")
form.geometry("320x400")
lblInfo = tkinter.Label(form, text="Movie to Photo app",
                        font=("Times New Roman", 20), fg="#8A32F3")
lblInfo.pack(pady=20)
lblInfo1 = tkinter.Label(form, text="Wybierz film z którego chesz wyeksportować zdjęcia",
                        font=("Times New Roman", 20), fg="#8A32F3", wraplength=300)
lblInfo1.pack(pady=20)


class Test:
    def __init__(self, master):
        myFrame = Frame(master)
        myFrame.pack()

        self.button2 = Button(master, text="Wybierz Plik", command=self.browse_button, bg="#8A32F3", fg="white",
                              activebackground="#321356", activeforeground="white", )
        self.button2.pack(pady=10)
        self.button3 = Button(master, text="Wyeksportuj", command=self.test, bg="#8A32F3", fg="white",
                              activebackground="#321356", activeforeground="white", )
        self.button3.pack(pady=10)
        self.button3 = Button(master, text="Otwórz folder", command=self.open_folder, bg="#8A32F3", fg="white",
                              activebackground="#321356", activeforeground="white", )
        self.button3.pack(pady=10)

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
            lblInfo1["text"] = f"Wybrałeś {self.filename1} kliknij wyeksportuj"
        else:
            print("Please select mp4 file")

    def test(self):
        print(self.filename1)
        cam = cv2.VideoCapture(f"C:\\Users\\kubeczek\\PycharmProjects\\FrameToPhoto\\UploadVideoHere\\{self.filename1}")
        try:
            if not os.path.exists('data'):
                os.makedirs('data')
        except OSError:
            print('Error: Creating directory of data')
        currentframe = 0
        while (True):
            ret, frame = cam.read()
            if ret:
                name = './data/frame' + str(currentframe) + '.jpg'
                print('Creating...' + name)

                cv2.imwrite(name, frame)

                currentframe += 1
            else:
                break

    def open_folder(self):
        path = "C:/Users/kubeczek/PycharmProjects/FrameToPhoto/data"
        path = os.path.realpath(path)
        os.startfile(path)

e = Test(form)

def set_video_name(filename1):
    vid = TinyTag.get(f"UploadVideoHere/{filename1}")
    print("Duration: " + str(vid.duration) + " seconds")



tkinter.mainloop()
