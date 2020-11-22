from __future__ import unicode_literals

from tkinter import *
import os
import subprocess
import youtube_dl
import getpass
from sys import platform

class youtubeDl:
    def __init__(self):

        # create a window and set title
        self.mainWindow = Tk()
        #self.mainWindow.configure(background='black')

        self.width_of_window = 250
        self.height_of_window = 125
        screen_width = self.mainWindow.winfo_screenwidth()
        screen_height = self.mainWindow.winfo_screenheight()
        xCord = screen_width/2 - self.width_of_window/2
        yCord = screen_height/2 - self.height_of_window/2
        self.mainWindow.geometry("%dx%d+%d+%d" % (self.width_of_window,self.height_of_window,xCord,yCord))

        self.mainWindow.title('YouTube Downloader')

        # URL box
        self.urlLabel = Label(self.mainWindow, text= 'Enter the URL : ')
        self.urlTextBox = Entry(self.mainWindow, width=10)
        self.urlLabel.grid(row=0, column=0)
        self.urlTextBox.grid(row=0, column=1)



        # create buttons

        self.button1 = Button(self.mainWindow, text='YouTube to mp3', command=self.mp3,width = 13)
        self.button2 = Button(self.mainWindow, text='YouTube to mp4', command=self.mp4,width = 13)
        self.button3 = Button(self.mainWindow, text='Open Folder', command=self.success,width = 10)
        self.button4 = Button(self.mainWindow, text='Open Folder', command=self.success,width = 10)

        self.exitButton = Button(self.mainWindow, text='Close', command=self.mainWindow.destroy)

        # place buttons
        self.button1.grid(row=1, column = 0)
        self.button2.grid(row=2, column = 0)
        self.button3.grid(row=1, column = 1)
        self.button4.grid(row=2, column = 1)

        self.exitButton.grid(row=3, column=0)

        # enter the main loop
        self.mainWindow.mainloop()



    def success(self):
        file_to_show = "/Users/ezulq/Desktop/youtube-dl/ignoreMe"
        subprocess.call(["open", "-R", file_to_show])





    def mp3(self):
        url = str(self.urlTextBox.get())

        ydl_opts = {
            'outtmpl': '/Users/ezulq/Desktop/youtube-dl_ME/%(title)s.%(ext)s',
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }],
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print('\nDownload Complete')

    def mp4(self):
        url = str(self.urlTextBox.get())

        ydl_opts = {
            'format': 'bestvideo+140',
            'preferredquality': '256',
            'outtmpl': '/Users/ezulq/Desktop/youtube-dl_ME/%(title)s.%(ext)s',
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print('\nDownload Complete')

def fileBool(username):
        path = sysCheck(username)  + '/youtube-dl_ME'
        return os.path.isdir(os.path.join(path))

def sysCheck(username):
    if platform == "linux" or platform == "linux2": # linux
        print('Sorry there is no support for this system yet!')

    elif platform == "darwin":  # mac
        parent_dir = '/Users/' + username + '/Desktop/'

    elif platform == "win32": # windows
        parent_dir = 'C:/Users/' + username + '/Desktop/'

    return parent_dir

def mkDir(username):
    directory = "youtube-dl_ME" # name of the new dir
    parent_dir = sysCheck(username)
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)

def main():
        username = getpass.getuser()  # get username of system
        if not fileBool(username):    # if file does not exist already
            mkDir(username)
main()

youtubeDl()
