from mysql import *

class values():
    
    def get_saldo(cpf):
        """ 
            Retorna o valor do saldo do cliente especificado \n
            resotna o valor não tratado
        """
        try:
            sql = "SELECT saldo FROM clientes WHERE cpf = %s"
            result = mysql.select(sql, cpf)
            for i in result:
                saldo = i[0]
            return saldo
        except:
            print("Erro ao obter saldo!!!")

    
    def get_cpfs():
        """
            Retorna todos os cpf's cadastrados
        """
        try:
            sql = "SELECT cpf FROM clientes"
            var = None
            result = mysql.select(sql, var)
            return result
        except:
            print("Erro ao obter o cpf!!!")
            

    def get_nome(cpf):
        """
            Retorna o nome do cliente especificado pelo cpf
        """
        try:
            sql = "SELECT nome FROM clientes WHERE cpf = %s"
            result = mysql.select(sql, cpf)
            return result
        except:
            print("Erro ao obter o nome!!!")
            