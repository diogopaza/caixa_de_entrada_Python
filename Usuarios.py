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
        print( self.telefone)

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            #c.execute("insert into usuarios( nome, telefone, email, usuario, senha) values ( '"+ self.nome +"', '"+self.telefone+"','"+self.email+"','"+self.usuario+"','"+self.senha + "' ))
            c.execute("insert into usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" + self.telefone + "', '" + self.email + "', '" + self.usuario + "', '" + self.senha + "' )")
  
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso"
        except:
            return "Ocorreu um erro na inserção do usuário"

        
            
        



    
