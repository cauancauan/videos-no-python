from model import model
import mysql.connector
from conexao import conexao

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = model()
        self.db_connection = conexao()  # Abrindo conexão com o banco de dados
        self.db_connection = self.db_connection.conectar()  # Método que realiza a conexão com o BD
        self.con = self.db_connection.cursor()  # Navegação no banco de dados

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("Escolha uma das opções abaixo: \n"+
              "0.Sair\n" +
              "1.Cadastrar\n" +
              "2.Logar\n" +
              "3.Atualizar Usuário\n"
              "4.Atualizar Senha\n" +
              "5.Excluir")
        self.setOpcao(int(input()))

    def menu2(self):
        print("Escolha uma das opções abaixo: \n" +
              "0.Sair\n" +
              "1.Cadastrar\n")
        self.setOpcao(int(input()))


    def operacoes(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print("Informe o Usuário: ")
                nome = input()
                print("Informe a Senha: ")
                senha = input()
                print(self.modelo.logar(nome, senha))
            elif self.getOpcao() == 3:
                self.atualizarNome()
            elif self.getOpcao() == 4:
                self.atualizarSenha()
            elif self.getOpcao() == 5:
                self.excluir()
            else:
                print("Opção escolhida inválida! Tente novamente!")




    def cadastrar(self):
        print("Informe o seu usuário: ")
        usuario = input()
        print("Informe sua senha: ")
        senha = input()
        print(self.modelo.inserir(usuario, senha))


    def atualizarNome(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe seu usuário atual: ")
        nome = input()
        print("informe sua senha atual: ")
        senha = input()

        achar = "Select * from pessoa where nome = '{}' and senha = '{}'".format(nome, senha)
        self.con.execute(achar)
        resultado = self.con.fetchall()
        if len(resultado) != 0:
            print("Informe o novo usuário")
            name = input()
            print(self.modelo.atualizar("nome", name, codigo))
        else:
            print("Usuário ou senha incorretos!")


    def atualizarSenha(self):
        print("Informe o código do dado que será atualizado!")
        codigo = int(input())
        print("Informe seu usuário atual: ")
        nome = input()
        print("informe sua senha atual: ")
        senha = input()

        achar = "Select * from pessoa where nome = '{}' and senha = '{}'".format(nome, senha)
        self.con.execute(achar)
        resultado = self.con.fetchall()
        if len(resultado) != 0:
            print("Informe a nova senha")
            senha = input()
            print(self.modelo.atualizar("senha", senha, codigo))
        else:
            print("Usuário ou senha incorretos!")

    def excluir(self):
        print("Informe o código do dado que deseja excluir!")
        cod = int(input())
        print("Informe seu usuário atual: ")
        nome = input()
        print("informe sua senha atual: ")
        senha = input()
        achar = "Select * from pessoa where nome = '{}' and senha = '{}'".format(nome, senha)
        self.con.execute(achar)
        resultado = self.con.fetchall()
        if len(resultado) != 0:
            print(self.modelo.excluir(cod))
        else:
            print("Usuário ou senha incorretos!")