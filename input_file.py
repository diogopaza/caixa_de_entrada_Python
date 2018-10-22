from tkinter import filedialog
from tkinter import *
import cv2

root = Tk()

def clicked():
    root.file_name =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(root.file_name)
    imagem = cv2.imread(root.file_name)
    cv2.imshow("Input", imagem)


btn = Button(root, text="Selecionar imagem", command=clicked)
btn.grid(column=1, row=0)
lbl=Label(root, text="")
lbl.grid(column=0, row=0)





