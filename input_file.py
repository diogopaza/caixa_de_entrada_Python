from tkinter import filedialog
from tkinter import *


root = Tk()

def clicked():
    root.file_name =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(root.file_name)

    


btn = Button(root, text="Selecionar imagem", command=clicked)
btn.grid(column=1, row=0)
lbl=Label(root, text="")
lbl.grid(column=0, row=0)





