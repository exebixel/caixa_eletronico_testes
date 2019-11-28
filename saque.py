from validar import *
from utils import *

class saque():
    
    def entrada():
        """
            Pede para o usuario digitar os dados para o saque
            no caso o valor a ser sacado
            e converte para inteiro o valor digitado
        """
        saque = input("Digite quanto deseja sacar: R$")
        saque = utils.srtToInt(saque)
        return saque
        
    def calculo_notas(valor):
        """
            Calcula o valor minimo de notas necessario para efetuar o saque
        """
        valorNotas = [100, 50, 20, 10, 5 ,2]
        for vn in valorNotas:
            notas = 0
            while True:
                if (valor - vn >= 0 and 
                    valor - vn != 1 and 
                    valor - vn != 3):
                        
                    if valor % 2 == 0 and vn == 5:
                        break
                    else:
                        valor -= vn
                        notas += 1
                else:
                    if notas > 0:
                        print("Notas de R$%d: %d" %(vn, notas))
                    break
                
                
    def atualizardb(valor, cpf):
        """
            Retira o valor sacado da conta do usuario no banco de dados
            valor = valor sacado
            cpf = cpf da conta do cliente
        """
        try: # saque no banco de dados
            sql = "UPDATE clientes SET saldo = saldo - %s WHERE cpf = %s"
            var = (valor, cpf)
            mysql.alterdata(sql, var)
                                
        except pymysql.Error as e:
            #se der errado mostra o erro
            print("Erro ao sacar!! \n ")