from tkinter import Tk, Text, Menu, filedialog

def open_file():
    file = filedialog.askopenfile(initialdir="./", title="Open File")
    if file is not None:
        editor.delete('1.0', 'end')
        editor.insert('1.0', file.read())

def save_file():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if file is not None:
        text = editor.get('1.0', 'end-1c')
        file.write(text)
        file.close()

def exit_editor():
    window.quit()

window = Tk()
window.title("Simple Text Editor")

editor = Text(window)
editor.pack()

menu_bar = Menu(window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=exit_editor)
menu_bar.add_cascade(label="File", menu=file_menu)

window.config(menu=menu_bar)
window.mainloop()
