from tkinter import *



class Application:
    def __init__(self, master=None):
        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()
        
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20  
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
        
        self.quartoContainer = Frame(master)
        self.quartoContainer["padx"] = 20
        self.quartoContainer.pack()
        
        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "10", "bold")
        self.titulo.pack()

        self.nomeLabel = Label( self.segundoContainer, text="Nome")
        self.nomeLabel.pack( side=LEFT )

        self.nome = Entry( self.segundoContainer )
        self.nome["width"]=30
        self.nome.pack( side=LEFT )

        self.senhaLabel = Label( self.terceiroContainer, text="Senha")
        self.senhaLabel.pack( side=LEFT )

        self.senha = Entry( self.terceiroContainer )
        self.senha["width"]=30
        self.senha["show"]="*"
        self.senha.pack( side=LEFT )

        self.autenticar = Button( self.quartoContainer )
        self.autenticar["text"]="Autenticar"
        self.autenticar["width"]=12
        self.autenticar["command"]=self.verificaSenha
        self.autenticar.pack()

        self.mensagem = Label( self.quartoContainer, text=""  )
        self.mensagem.pack()
    
        
    def verificaSenha(self):
        print("autenticando")
        usuario = self.nome.get()
        senha = self.senha.get()
        if usuario == "123" and senha=="123":
            self.mensagem["text"] = "Autenticado"
        else:
            self.mensagem["text"] = "Erro na autenticação"


janela = Tk()
Application( janela )
janela.mainloop()
