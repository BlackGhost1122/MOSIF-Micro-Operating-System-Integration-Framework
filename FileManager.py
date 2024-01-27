from tkinter import *
from tkinter import filedialog
import os

class FileListApp:
    def __init__(self, master=None):
        self.master = master
        self.master.geometry("720x350")
        self.master.resizable(width=False, height=False)
        self.master.title("File Manager OS")
        self.master.protocol('WM_DELETE_WINDOW')
        self.master['bg'] = 'black'
        self.manager_widgets()

    def manager_widgets(self):

        message_lbl = Label(self.master, text="File Manager M.O.S.I.F", bg='black', fg='white', font='Arial 12 bold')
        message_lbl.pack()

        message_mp3_lbl = Label(self.master, text="MP3 FILES", bg="black", fg='white', font='Arial 9 bold')
        message_mp3_lbl.place(relx=0.09, rely=0.1)

        self.message_mp4_lbl = Label(self.master, text="MP4 FILES", bg='black', fg='white', font='Arial 9 bold')
        self.message_mp4_lbl.place(relx=0.27, rely=0.1)

        self.message_docx_lbl = Label(self.master, text="DOCX FILES", bg='black', fg='white', font='Arial 9 bold')
        self.message_docx_lbl.place(relx=0.44, rely=0.1)

        self.message_exe_lbl = Label(self.master, text="EXE FILES", bg='black', fg='white', font='Arial 9 bold')
        self.message_exe_lbl.place(relx=0.63, rely=0.1)

        self.message_pptx_lbl = Label(self.master, text="PPTX FILES", bg='black', fg='white', font='Arial 9 bold')
        self.message_pptx_lbl.place(relx=0.80, rely=0.1)

        self.file_mp3_listbox = Listbox(self.master, selectmode=SINGLE, bg='black', fg='white')
        self.file_mp3_listbox.place(relx=0.05, rely=0.2)

        self.file_mp4_listbox = Listbox(self.master, selectmode=SINGLE, bg='black', fg='white')
        self.file_mp4_listbox.place(relx=0.23, rely=0.2)

        self.file_exe_listbox = Listbox(self.master, selectmode=SINGLE, bg='black', fg='white')
        self.file_exe_listbox.place(relx=0.59, rely=0.2)

        self.file_docx_listbox = Listbox(self.master, selectmode=SINGLE, bg='black', fg='white')
        self.file_docx_listbox.place(relx=0.41, rely=0.2)

        self.file_pptx_listbox = Listbox(self.master, selectmode=SINGLE, bg='black', fg='white')
        self.file_pptx_listbox.place(relx=0.77, rely=0.2)

        add_mp3_button = Button(self.master, text="add mp3 file", bg='black', fg='white', font='Arial 10 bold', padx=18, pady=5, command=self.add_mp3_file)
        add_mp3_button.place(relx=0.05, rely=0.67)

        delete_mp3_button = Button(self.master, text="delete mp3 file", bg='black', fg='white', font='Arial 10 bold', padx=10, pady=5, command=self.delete_mp3_file)
        delete_mp3_button.place(relx=0.05, rely=0.87)

        open_mp3_button = Button(self.master, text="open mp3 file", bg='black', fg='white', font='Arial 10 bold', padx=14, pady=5, command=self.open_mp3_file)
        open_mp3_button.place(relx=0.05, rely=0.77)

        add_mp4_button = Button(self.master, text="add mp4 file", bg='black', fg='white', font='Arial 10 bold', padx=18, pady=5, command=self.add_mp4_file)
        add_mp4_button.place(relx=0.23, rely=0.67)

        delete_mp4_button = Button(self.master, text="delete mp4 file", bg='black', fg='white', font='Arial 10 bold', padx=10, pady=5, command=self.delete_mp4_file)
        delete_mp4_button.place(relx=0.23, rely=0.87)

        open_mp4_button = Button(self.master, text="open mp4 file", bg='black', fg='white', font='Arial 10 bold', padx=14, pady=5, command=self.open_mp4_file)
        open_mp4_button.place(relx=0.23, rely=0.77)

        add_docx_button = Button(self.master, text="add docx file", bg='black', fg='white', font='Arial 10 bold', padx=16, pady=6, command=self.add_docx_file)
        add_docx_button.place(relx=0.41, rely=0.67)

        open_docx_button = Button(self.master, text="open docx file", bg='black', fg='white', font='Arial 10 bold', padx=12, pady=6, command=self.open_docx_file)
        open_docx_button.place(relx=0.41, rely=0.77)

        delete_docx_button = Button(self.master, text="delete docx file", bg='black', fg='white', font='Arial 10 bold', padx=8, pady=5, command=self.delete_docx_file)
        delete_docx_button.place(relx=0.41, rely=0.87)

        add_exe_button = Button(self.master, text="add exe file", bg='black', fg='white', font='Arial 10 bold', padx=19, pady=6, command=self.add_exe_file)
        add_exe_button.place(relx=0.59, rely=0.67)

        open_exe_button = Button(self.master, text="open exe file", bg='black', fg='white', font='Arial 10 bold', padx=15, pady=5, command=self.open_exe_file)
        open_exe_button.place(relx=0.59, rely=0.77)

        delete_exe_button = Button(self.master, text="delete exe file", bg='black', fg='white', font='Arial 10 bold', padx=11, pady=5, command=self.delete_exe_file)
        delete_exe_button.place(relx=0.59, rely=0.87)

        add_pptx_button = Button(self.master, text="add pptx file", bg='black', fg='white', font='Arial 10 bold', padx=17, pady=6, command=self.add_pptx_file)
        add_pptx_button.place(relx=0.77, rely=0.67)

        open_pptx_button = Button(self.master, text="open pptx file", bg='black', fg='white', font='Arial 10 bold', padx=13, pady=5, command=self.open_pptx_file)
        open_pptx_button.place(relx=0.77, rely=0.77)

        delete_pptx_button = Button(self.master, text="delete pptx file", bg='black', fg='white', font='Arial 10 bold', padx=9, pady=5, command=self.delete_pptx_file)
        delete_pptx_button.place(relx=0.77, rely=0.87)

        console_button = Button(self.master, text="Console", bg='black', fg='white', font='Arial 8 bold', padx=8, pady=1, command=self.open_console)
        console_button.place(relx=0.00, rely=0.0)

        exit_button = Button(self.master, text="Exit", bg='black', fg='white', font='Arial 8 bold', padx=8, pady=1, command=self.exit_manager)
        exit_button.place(relx=0.95, rely=0.0)


    def add_mp3_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 FILES", "*.mp3")])
        if file_path:
            self.file_mp3_listbox.insert(END, file_path)

    def delete_mp3_file(self):
        selected_index = self.file_mp3_listbox.curselection()
        if selected_index:
            self.file_mp3_listbox.delete(selected_index)

    def open_mp3_file(self):
        selected_index = self.file_mp3_listbox.curselection()
        if selected_index:
            file_path = self.file_mp3_listbox.get(selected_index)
            try:
                os.startfile(file_path)
            except Exception as e:
                print(f"Error open file: {e}")

    def add_mp4_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP4 FILES", "*.mp4")])
        if file_path:
            self.file_mp4_listbox.insert(END, file_path)

    def delete_mp4_file(self):
        selected_index = self.file_mp4_listbox.curselection()
        if selected_index:
            self.file_mp4_listbox.delete(selected_index)

    def open_mp4_file(self):
        selected_index = self.file_mp4_listbox.curselection()
        if selected_index:
            file_path = self.file_mp4_listbox.get(selected_index)
            try:
                os.startfile(file_path)
            except Exception as e:
                print(f"Error open file: {e}")

    def add_exe_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("EXE FILES", "*.exe")])
        if file_path:
            self.file_exe_listbox.insert(END, file_path)

    def delete_exe_file(self):
        selected_index = self.file_exe_listbox.curselection()
        if selected_index:
            self.file_exe_listbox.delete(selected_index)

    def open_exe_file(self):
        selected_index = self.file_exe_listbox.curselection()
        if selected_index:
            file_path = self.file_exe_listbox.get(selected_index)
            try:
                os.startfile(file_path)
            except Exception as e:
                print(f"Error open file: {e}")

    def add_docx_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("DOCX FILES", "*.docx")])
        if file_path:
            self.file_docx_listbox.insert(END, file_path)

    def delete_docx_file(self):
        selected_index = self.file_docx_listbox.curselection()
        if selected_index:
            self.file_docx_listbox.delete(selected_index)

    def open_docx_file(self):
        selected_index = self.file_docx_listbox.curselection()
        if selected_index:
            file_path = self.file_docx_listbox.get(selected_index)
            try:
                os.startfile(file_path)
            except Exception as e:
                print(f"Error open file: {e}")

    def add_pptx_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("PPTX FILES", "*.pptx"), ("PNG FILES", "*.png"), ("JPG FILES", "*.jpg")])
        if file_path:
            self.file_pptx_listbox.insert(END, file_path)

    def delete_pptx_file(self):
        selected_index = self.file_pptx_listbox.curselection()
        if selected_index:
            self.file_pptx_listbox.delete(selected_index)

    def open_pptx_file(self):
        selected_index = self.file_pptx_listbox.curselection()
        if selected_index:
            file_path = self.file_pptx_listbox.get(selected_index)
            try:
                os.startfile(file_path)
            except Exception as e:
                print(f"Error open file: {e}")

    def open_console(self):
        csharp_file_path = "C:\\Users\\Admin\\Desktop\\System Files\\bin\\Debug\\net8.0\\ConsoleOS.exe"
        try:
            os.startfile(csharp_file_path)
        except Exception as e:
            print(f"Error open file: {e}")

    def exit_manager(self):
        self.master.destroy()

if __name__ == '__main__':
    root = Tk()
    app = FileListApp(root)
    root.mainloop()
