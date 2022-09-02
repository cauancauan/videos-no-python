import mysql.connector
from conexao import conexao
import webbrowser as wb


class model:
    def __init__(self):
        self.db_connection = conexao() #Abrindo conexão com o banco de dados
        self.db_connection = self.db_connection.conectar()#Método que realiza a conexão com o BD
        self.con = self.db_connection.cursor()#Navegação no banco de dados
        self.opcao = -1
        self.resultado = 0

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("Escolha uma das opções abaixo: \n" +
              "0.Sair\n"
              "===================================== Libras =====================================\n" +
              "1.Alfabeto\n"
              "2.Frutas\n"
              "3.33 Frases essenciais!\n"
              "4.Números\n"
              "5.Verbos")

        self.setOpcao(int(input()))

    def inserir(self, nome, senha):
        try:
            sql = "insert into pessoa(codigo, nome, senha) values('','{}','{}')".format(nome, senha)
            self.con.execute(sql)
            self.db_connection.commit()#Insere o dado no banco de dados
            return "{} linhas afetadas".format(self.con.rowcount)
        except Exception as erro:
            return erro

    def selecionar(self):
        try:
            sql = "Select * from pessoa"
            self.con.execute(sql)
            msg = ""
            for (codigo, nome, telefone, endereco, dataDeNascimento) in self.con:
                msg = msg + "Código: {}, Nome: {}, Telefone: {}, Endereço: {}, Data de Nascimento: {}".format(codigo, nome, telefone, endereco, dataDeNascimento)
            return msg
        except Exception as erro:
            return erro

    def atualizar(self, campo, novoDado, cod):
        try:
            sql = "update pessoa set {} = '{}' where codigo = '{}'".format(campo, novoDado, cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "Informações alteradas com sucesso!"
        except Exception as erro:
            return erro

    def excluir(self, cod):

        try:

            sql = "delete from pessoa where codigo = '{}'".format(cod)
            self.con.execute(sql)
            self.db_connection.commit()
            return "{} linha afetada!".format(self.con.rowcount)

        except Exception as erro:

            return erro

    def logar(self, nome, senha):
            achar = "Select * from pessoa where nome = '{}' and senha = '{}'".format(nome, senha)
            self.con.execute(achar)
            self.resultado = self.con.fetchall()
            if len(self.resultado) != 0:
                print('Logado com Sucesso!')
                print(f'===================================== Bem vindo {nome} =====================================')
                while self.getOpcao() != 0:
                    self.menu()
                    if self.getOpcao() == 0:
                        print("Obrigado!")
                    elif self.getOpcao() == 1:
                        wb.open('https://www.youtube.com/watch?v=EZxkymw426U')
                    elif self.getOpcao() == 2:
                        wb.open('https://www.youtube.com/watch?v=atwl7WDq6qE')
                    elif self.getOpcao() == 3:
                        wb.open('https://www.youtube.com/watch?v=aJqn0Z1KF5M')
                    elif self.getOpcao() == 4:
                        wb.open('https://www.youtube.com/watch?v=e7ibD6SFehE')
                    elif self.getOpcao() == 5:
                        wb.open('https://www.youtube.com/watch?v=Cq44vPemtGU')
                else:
                    print("Opção escolhida inválida! Tente novamente!")

            else:
                print('Usuário ou senha incorretos!')











