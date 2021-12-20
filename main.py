from __future__ import unicode_literals
from playsound import playsound
from tkinter import *
import tkinter as tk
import os
import subprocess
from tkmacosx import Button

class youtubeDl:
    def __init__(self):
        # create a window and set title
        self.mainWindow = Tk()
        self.width_of_window = 475
        self.height_of_window = 125

        screen_width = self.mainWindow.winfo_screenwidth()
        screen_height = self.mainWindow.winfo_screenheight()
        xCord = screen_width/2 - self.width_of_window/2
        yCord = screen_height/2 - self.height_of_window/2
        self.mainWindow.geometry("%dx%d+%d+%d" % (self.width_of_window,self.height_of_window,xCord,yCord))
        self.mainWindow.title('YouTube Downloader')

        # URL box
        self.urlLabel = Label(self.mainWindow, text= 'Enter the URL : ')
        self.urlTextBox = Entry(self.mainWindow, width=35)
        self.urlLabel.grid(row=0, column=0)
        self.urlTextBox.grid(row=0, column=1)

        # create buttons
        self.button1 = Button(self.mainWindow, text='YouTube to mp3', command=self.mp3)
        self.button2 = Button(self.mainWindow, text='YouTube to mp4', command=self.mp4)
        self.button3 = Button(self.mainWindow, text='Open Folder', command=self.success)
        self.button4 = Button(self.mainWindow, text='Open Folder', command=self.success)
        self.button5 = Button(self.mainWindow, text='Test', command=self.test)
        self.exitButton = Button(self.mainWindow, text='Close', command=self.mainWindow.destroy)

        # place buttons
        self.button1.grid(row=1, column = 0)
        self.button2.grid(row=2, column = 0)
        self.button3.grid(row=1, column = 1)
        self.button4.grid(row=2, column = 1)
        self.button5.grid(row=3, column = 1)

        self.exitButton.grid(row=3, column=0)


        # enter the main loop
        self.mainWindow.lift()
        self.mainWindow.mainloop()

    def success(self):
        file_to_show = "/Users/ezulq/youtube-dl/loc.txt"
        subprocess.call(["open", "-R", file_to_show])

    def mp3(self):
        try:
            url = str(self.urlTextBox.get())
            command = "youtube-dl -f bestaudio --extract-audio --audio-format mp3 --audio-quality 0 " + url
            print(command)
            os.system(command)
            playsound('bamboosoundeffect.mp3')
            print('\nDownload Complete.')
            open_popup('Success')

        except Exception as e:
            playsound('error.mp3')
            open_popup(e)

    def mp4(self):
        try:
            url = str(self.urlTextBox.get())
            command = "youtube-dl -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 " + url
            os.system(command)
            playsound('bamboosoundeffect.mp3')
            print('\nDownload Complete.')
            open_popup('Success')

        except Exception as e:
            playsound('error.mp3')
            open_popup(e)

    def test(self):
        print('start')
        open_popup('success')
        print('finish')

def open_popup(result):
    win = tk.Tk()
    top = Toplevel(win)
    top.geometry('200x50')
    top.title('Result.')
    win.withdraw()
    Label(top,text=result).place(x=100,y=25,anchor=CENTER)

    wait_time = 3000 #3 seconds
    win.after(wait_time,lambda:win.destroy())

youtubeDl()