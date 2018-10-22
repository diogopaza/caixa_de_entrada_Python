from tkinter import filedialog
from tkinter import *
import cv2

root = Tk()

def clicked():
    root.fileName =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    print(root.fileName)
    imagem = cv2.imread(root.fileName)
    cv2.imshow("Input", imagem)


btn = Button(root, text="Selecionar imagem", command=clicked)
btn.grid(column=1, row=0)
lbl=Label(root, text="")
lbl.grid(column=0, row=0)





