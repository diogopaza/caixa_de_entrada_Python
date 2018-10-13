from Banco import Banco

class Usuarios( object ):

    def __init__(self, idusuario=0, nome="",telefone="",email="",usuario="",
                 senha=""):
        print("criando usuario")
        self.info={}
        self.idusuario = idusuario
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.usuario = usuario
        self.senha = senha
        

    def listar(self):
        print( self.nome)

user = Usuarios()

    
