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
        print( telefone)

    def insertUser(self):
        banco = Banco()
        try:
            c = banco.conexao.cursor()

            c.execute("insert into usuarios( nome, telefone, email, usuario, senha) values ( '"+ self.nome +"', '"+self.telefone+"','"+self.email+"','"+self.usuario+"','"+self.senha + "' )")
            
  
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso"
        except:
            return "Ocorreu um erro na inserção do usuário"

    def selectUser(self, nome):
        banco = Banco()
        try:
            
            c=banco.conexao.cursor()
            c.execute("select * from usuarios where idusuario = " +idusuario + " ")

            for linha in c:
                self.idusuario = linha[0]
                self.nome = linha[1]

            c.close()
  
            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do usuário"
            



    
