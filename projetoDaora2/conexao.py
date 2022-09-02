import mysql.connector  # Elemento qie faz a conexão com o bando de dados
from mysql.connector import errorcode


class conexao:
    def __init__(self):
        pass

    def conectar(self):
        try:
            self.db_connection = mysql.connector.connect(host='localhost', user='root', password='',
                                                         database='LibrasProjeto')

            print('Conectado com sucesso!')
            return self.db_connection
        except mysql.connector.Error as erro:
            if erro.errno == errorcode.ER_BAD_DB_ERROR:  # Caso banco de dados não exista
                print('Banco de dados não existe! erro: {}'.format(erro))
            elif erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print('Nome de usuário ou senha inválido: \n Erro: {}'.format(erro))
            else:
                print(erro)
        else:
            self.db_connection.close()  # Fechando a conexão com o banco de dados
