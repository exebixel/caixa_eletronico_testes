from mysql import *

class saldo():
    
    def get_saldo(cpf):
        """
            Retorna o valor do saldo atual do cliente
        """
        try:
            sql = "SELECT saldo FROM clientes WHERE cpf = %s"
            result = mysql.select(sql, cpf)
            for saldo in result:
                return saldo
        except:
            print("Erro ao pesquisar saldo!!!")
        
    def print_saldo(cpf):
        """
            Imprime o saldo atual do cliente na tela
        """
        valor = saldo.get_saldo(cpf)
        print("Saldo atual: R$%.2f \n" %(valor))
        