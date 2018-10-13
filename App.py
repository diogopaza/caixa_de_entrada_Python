from tkinter import *

class Application:
    
    def __init__(self, master=None):

        self.container1 = Frame(master)
        self.container1["pady"]=10
       
        self.container1.pack()

        self.container2 = Frame(master)
        self.container2["padx"]=20
        self.container2["pady"]=5
        self.container2.pack()

        self.container3 = Frame(master)
        self.container3["padx"]=20
        self.container3["pady"]=5
        self.container3.pack()

        self.container4 = Frame(master)
        self.container4["padx"]=20
        self.container4["pady"]=5
        self.container4.pack()

        self.container5 = Frame(master)
        self.container5["padx"]=20
        self.container5["pady"]=5
        self.container5.pack()

        self.container6 = Frame(master)
        self.container6["padx"]=20
        self.container6["pady"]=5
        self.container6.pack()

        self.container7 = Frame(master)
        self.container7["padx"]=20
        self.container7["pady"]=5
        self.container7.pack()

        self.container8 = Frame(master)
        self.container8["padx"]=20
        self.container8["pady"]=5
        self.container8.pack()

        self.container9 = Frame(master)
        self.container9["padx"]=20
        self.container9["pady"]=5
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados: ")
        self.titulo.pack()

        self.lblidusuario = Label( self.container2, text="idUsuario", width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidusuario = Entry(self.container2)
        self.txtidusuario["width"] = 10
        self.txtidusuario.pack( side=LEFT )
        
        self.btnBuscar = Button(self.container2, text="Buscar", width=10)
        
        self.btnBuscar["command"]=self.buscarUsuario
        self.btnBuscar.pack(side=LEFT)

        self.lblnome = Label( self.container3, text="Nome: ", width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"]=25
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label( self.container4, text="Telefone: ", width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"]=25
        self.txttelefone.pack(side=LEFT)

        self.lblemail = Label( self.container5, text="Email: ", width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"]=25
        self.txtemail.pack(side=LEFT)

        self.lblusuario = Label( self.container6, text="Usuário: ", width=10)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container6)
        self.txtusuario["width"]=25
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label( self.container7, text="Senha: ", width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"]=25
        self.txtsenha["show"]="*"
        self.txtsenha.pack(side=LEFT)

        self.btnInserir = Button(self.container8, text="Inserir", width=12)
        self.btnInserir["command"] = self.inserirUsuario
        self.btnInserir.pack(side=LEFT)
        
        self.lblmensagem = Label( self.container9, text="")
        self.lblmensagem.pack()

    def buscarUsuario(self):
          print("buscando")
        
    def inserirUsuario(self):
        self.txtidusuario.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)


  

janela = Tk()
Application( janela )
janela.mainloop()
