from tkinter import *
from PIL import Image, ImageTk
import subprocess
import messagebox

class OfficeManager(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.iconbitmap(default="images\\OfficeIcon.ico")
        self.master.geometry("1150x650")
        self.master.resizable(width=False, height=False)
        self.master.protocol("WM_DELETE_WINDOW", self.closing_manager)
        self.master.title("Microsoft Office Manager")
        self.master['bg'] = 'red'
        self.background_image()
        self.triggerOperation()

    def triggerOperation(self):
        self.ImageOneDrive = ImageTk.PhotoImage(file="images\\MicrosoftOneDrive.png")
        self.one_drive_btn = Button(self.master, font="Arial 15 bold", image=self.ImageOneDrive, compound=CENTER, bg="black", padx=15, pady=15, command=self.open_one_drive)
        self.one_drive_btn.place(relx=0.86, rely=0.0)

        one_drive_lbl = Label(self.master, text="Microsoft OneDrive", font="Arial 10 bold", padx=4, pady=5)
        one_drive_lbl.place(relx=0.86, rely=0.2)

        self.ImageOneNote = ImageTk.PhotoImage(file="images\\MicrosoftOneNote.png")
        self.one_note_btn = Button(self.master, font="Arial 15 bold", image=self.ImageOneNote, compound=CENTER, bg="black", padx=15, pady=15, command=self.open_one_note)
        self.one_note_btn.place(relx=0.74, rely=0.0)

        one_note_lbl = Label(self.master, text="Microsoft OneNote", font="Arial 10 bold", padx=6, pady=5)
        one_note_lbl.place(relx=0.74, rely=0.2)

        self.ImageAccess = ImageTk.PhotoImage(file="images\\MicrosoftAccess.png")
        self.access_btn = Button(self.master, font="Arial 15 bold", image=self.ImageAccess, compound=CENTER, bg="black", padx=15, pady=15, command=self.open_access)
        self.access_btn.place(relx=0.62, rely=0.0)

        access_lbl = Label(self.master, text="Microsoft Access", font="Arial 10 bold", padx=12, pady=5)
        access_lbl.place(relx=0.62, rely=0.2)

        self.ImageWord = ImageTk.PhotoImage(file="images\\MicrosoftWord.png")
        self.word_btn = Button(self.master, font="Arial 15 bold", image=self.ImageWord, compound=CENTER, bg="black", padx=15, pady=15, command=self.open_word)
        self.word_btn.place(relx=0.50, rely=0.0)

        word_lbl = Label(self.master, text="Microsoft Word", font="Arial 10 bold", padx=17, pady=5)
        word_lbl.place(relx=0.50, rely=0.2)

        self.ImagePowerPoint = ImageTk.PhotoImage(file="images\\MicrosoftPowerPoint.png")
        self.power_point_btn = Button(self.master, font="Arial 15 bold", image=self.ImagePowerPoint, compound=CENTER, bg="black", padx=15, pady=15, command=self.open_powerpoint)
        self.power_point_btn.place(relx=0.38, rely=0.0)

        power_point_lbl = Label(self.master, text="Microsoft PowerPoint", font="Arial 9 bold", padx=3, pady=5.4)
        power_point_lbl.place(relx=0.38, rely=0.2)

        self.ImageOutLook = ImageTk.PhotoImage(file="images\\MicrosoftOutLook.png")
        self.out_look_btn = Button(self.master, font="Arial 15 bold", image=self.ImageOutLook, compound=CENTER, bg="black", padx=15, pady=15, command=self.open_outlook)
        self.out_look_btn.place(relx=0.26, rely=0.0)

        out_look_lbl = Label(self.master, text="Microsoft OutLook", font="Arial 10 bold", padx=7, pady=5)
        out_look_lbl.place(relx=0.26, rely=0.2)

        self.ImageTeams = ImageTk.PhotoImage(file="images\\MicrosoftTeams.png")
        self.teams_btn = Button(self.master, font="Arial 15 bold", image=self.ImageTeams, compound=CENTER, bg="black", padx=15, pady=15, command=self.open_teams)
        self.teams_btn.place(relx=0.14, rely=0.0)

        teams_lbl = Label(self.master, text="Microsoft Teams", font="Arial 10 bold", padx=13, pady=5)
        teams_lbl.place(relx=0.14, rely=0.2)

        self.ImageExcel = ImageTk.PhotoImage(file="images\\MicrosoftExcel.png")
        self.excel_btn = Button(self.master, font="Arial 15 bold", image=self.ImageExcel, compound=CENTER, bg="black", padx=15, pady=15, command=self.open_excel)
        self.excel_btn.place(relx=0.02, rely=0.0)

        excel_lbl = Label(self.master, text="Microsoft Excel", font="Arial 10 bold", padx=16, pady=5)
        excel_lbl.place(relx=0.02, rely=0.2)

        mosif_lbl = Label(self.master, text="M.O.S.I.F", bg="black", fg="white", font="Arial 8 bold", padx=10, pady=8)
        mosif_lbl.place(relx=0.00, rely=0.95)

    def background_image(self):
        image = Image.open("images\\MicrosoftOfficeImage.jpg")
        image = image.resize((1150, 650))
        self.background_image = ImageTk.PhotoImage(image)
        background_lbl = Label(self.master, image=self.background_image)
        background_lbl.place(relwidth=1, relheight=1)
    def closing_manager(self):
        if messagebox.askokcancel('Closing', 'Are you sure you want to leave the manager?'):
            self.master.destroy()
            print("Program Destroy...")

    def open_word(self):
        subprocess.Popen(["start", "winword"], shell=True)
        print("Word Opened")

    def open_powerpoint(self):
        subprocess.Popen(["start", "powerpnt"], shell=True)
        print("PowerPoint Opened")

    def open_outlook(self):
        subprocess.Popen(["start", "outlook"], shell=True)
        print("OutLook Opened")

    def open_teams(self):
        teams_path = r'C:\Users\Admin\AppData\Local\Microsoft\Teams\current\Teams.exe'
        subprocess.Popen([teams_path], shell=True)
        print("Teams Opened")

    def open_excel(self):
        subprocess.Popen(["start", "excel"], shell=True)
        print("Excel Opened")

    def open_access(self):
        subprocess.Popen(["start", "msaccess"], shell=True)
        print("Access Opened")

    def open_one_note(self):
        subprocess.Popen(["start", "onenote"], shell=True)
        print("One Note Opened")

    def open_one_drive(self):
        onedrive_path = r'C:\Program Files (x86)\Microsoft OneDrive\OneDrive.exe'
        subprocess.Popen([onedrive_path], shell=True)
        print("OneDrive Opened")

if __name__ == '__main__':
    root = Tk()
    MicrosoftOffice = OfficeManager(root)
    MicrosoftOffice.mainloop()