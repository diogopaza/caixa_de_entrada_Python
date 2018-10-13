from tkinter import *

class Application:
    def __init__(self, master=None):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label( self.widget1, text="Primeiro widget" )
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri","10")
        self.sair["width"] = 5
        self.sair["command"] = self.widget1.quit
        self.sair.bind("<Button-1>", self.mudarTexto)
        self.sair.pack(side=RIGHT)

    def mudarTexto(self, event):
        if  self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"
        
    
minha_janela = Tk()
Application( minha_janela )
minha_janela.mainloop()

