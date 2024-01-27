# Activation M.O.S.I.F Operating System
from tkinter import *
from tkinter.messagebox import *


class Activation_Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("250x100")
        self.master.resizable(width=False, height=False)
        self.master.protocol("WM_DELETE_WINDOW", self.closing_activation)
        self.master.title("Activation M.O.S.I.F")
        self.master.iconbitmap("C:\\Users\\Admin\\Downloads\\codeico.ico")
        self.master['bg'] = 'white'
        self.activation_script()

    def activation_script(self):
        activation_code_lbl = Label(self.master, text="Activation product", font="Arial 9 bold", bg='white', fg='black')
        activation_code_lbl.pack()

        self.code_product_entry = Entry(self.master, font="Arial 9 bold", bg='white', fg='black')
        self.code_product_entry.pack()

        self.activate_product_code_btn = Button(self.master, text="activate", font="Arial 9 bold", bg='white', fg='black', padx=1, pady=2, command=self.activation_code_script)
        self.activate_product_code_btn.place(relx=0.21, rely=0.4)

        self.skip_activation_btn = Button(self.master, text="skip", font="Arial 9 bold", bg='white', fg='black', padx=10, pady=2, command=self.skip_activation)
        self.skip_activation_btn.place(relx=0.42, rely=0.4)

        self.help_activation_btn = Button(self.master, text="help", font="Arial 9 bold", bg='white', fg='black', padx=5, pady=2, command=self.help_activation)
        self.help_activation_btn.place(relx=0.62, rely=0.4)

    def activation_code_script(self):
        self.code_product = self.code_product_entry.get()
        if self.code_product == "KEYE-LOKE-KODE-MOSIF":
            showinfo("Success!", "The activation key has arrived! M.O.S.I.F activated")
            self.master.destroy()
        else:
            showerror("Error", "Error! The product key did not match")

    def closing_activation(self):
        showerror("Activation", "Enter your product key or skip this activation!")
        pass

    def skip_activation(self):
        self.master.destroy()

    def help_activation(self):
        showinfo("HELP CENTER", "Activate M.O.S.I.F to gain full access to the operating system")

if __name__ == '__main__':
    root = Tk()
    activation = Activation_Window(root)
    activation.mainloop()