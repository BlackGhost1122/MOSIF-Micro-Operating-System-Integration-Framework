from tkinter import *
from PIL import Image, ImageTk
import subprocess
import pygame
import time
import webbrowser
import sys
from tkinter import messagebox

class DesktopGUI(Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master
        self.master.protocol("WM_DELETE_WINDOW", self.closing_os)
        self.master.attributes('-fullscreen', True)
        #self.master.geometry("1150x650")
        self.master.resizable(width=False, height=False)
        self.master.title("M.O.S.I.F GUI")
        self.master['bg'] = 'black'
        self.master.overrideredirect(True)
        self.background_image()
        self.os_widgets()
        pygame.mixer.init()
        pygame.mixer.music.load("musics\\Welcome.mp3")
        pygame.mixer.music.play()
        self.on_start = None

    def os_widgets(self):
        """Кнока пуск"""
        start_lbl = Label(self.master, text="", bg="white", font="Arial 9 bold", padx=1000, pady=8)
        start_lbl.place(relx=0.0, rely=0.96)


        """Кнопка пуск"""
        self.IconStart = ImageTk.PhotoImage(file="images\\logom.jpg")
        self.start_btn = Button(self.master, bg="black", font="Arial 10 bold", image=self.IconStart, compound=CENTER, padx=17, pady=8, command=self.start_function)
        self.start_btn.place(relx=0.48, rely=0.96)

        """Кнопка на выхода время"""
        self.exit_os_btn = Button(self.master, text="Exit", bg="black", fg="white", font="Arial 10 bold", padx=10, pady=8, command=self.exit_os)
        self.exit_os_btn.pack()

    def background_image(self):
        image = Image.open("images\\SystemImage.jpg")
        image = image.resize((1550, 900))
        self.background_image = ImageTk.PhotoImage(image)
        background_lbl = Label(self.master, image=self.background_image)
        background_lbl.place(relwidth=1, relheight=1)

    def closing_os(self):
        if messagebox.askokcancel('Shut Down', 'Shut Down?'):
            self.master.destroy()
            pygame.mixer.music.load("musics\\ExitShut.mp3")
            pygame.mixer.music.play()
            time.sleep(3)
            print("OS Destroy...")

    def exit_os(self):
        self.master.destroy()
        print("PROGRAM DESTROY...")

    def start_function(self):
        if self.on_start and self.on_start.winfo_exists():
            self.on_start.destroy()
            self.on_start = None
        else:
            self.on_start = Toplevel(self.master)
            self.start = Start(self.on_start)

class Start(Frame):
    def __init__(self, start=None):
        super().__init__(start)
        self.start = start
        self.start.geometry("400x400+555+428")
        self.start.resizable(width=False, height=False)
        self.start.overrideredirect(True)
        self.start_widgets()

    def start_widgets(self):
        pass

if __name__ == '__main__':
    root = Tk()
    mosif = DesktopGUI(root)
    mosif.mainloop()
