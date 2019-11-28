from validar import *
from utils import *

class deposito():
    
    def entrada():
        """
            Pede para o usuario o valor a ser depositado
            e retorna o valor de deposito
        """
        valor = input("Digite quanto deseja depositar? R$")
        valor = utils.srtToInt(valor)
        return valor
    
    def atualizadb(valor, cpf):
        """
            Atualiza o valor do saldo no banco de dados,
            soma o valor depositado ao saldo atual \n
            valor = valor a ser depositado \n
            cpf = cpf da conta do cliente 
        """
        try:
            #comando do mysql (mariadb)
            sql = "UPDATE clientes SET saldo = saldo + %s WHERE cpf = %s"
            #variaveis do comando do mysql (mariadb)
            var = (valor, cpf)

            mysql.alterdata(sql, var)
            
            print("Saldo atualizado!!")
        except:
            print("Erro ao fazer o deposito!!!")