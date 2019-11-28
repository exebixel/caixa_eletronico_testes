from mysql import *
from values import *
from saldo import *
from menu import *
from utils import *
from saque import *
from validar import *
from deposito import *

class operacoes():
    """
        Gerencia todas a operações bancarias feitas pelos usuarios
    """

    def saldo(cpf):
        """ Consulta o saldo do cliente no banco de dados \n"""
        saldo.print_saldo(cpf)
        utils.pause()
        

    def saque(cpf):
        """ 
            Efetua um saque na conta de um cliente,
            imprimindo na tela o número minimo de 
            notas necessarias para o caixa entregar ao cliente \n
            saque = valor a ser sacado
            cpf = cpf da conta do cliente 
        """
        try:
            valor = saque.entrada()
            if validar.saque(valor, cpf):
                saque.atualizardb(valor, cpf)
                saque.calculo_notas(valor)
                saldo.print_saldo(cpf)
        except:
            print("Algo deu errado!!!")
        utils.pause()

    # deposito
    def deposito(cpf): 
        """ deposita um valor na conta de um cliente \n
            cpf = cpf da conta do cliente 
        """
        try:
            valor = deposito.entrada()
            if validar.deposito(valor):
                deposito.atualizadb(valor, cpf)   
                saldo.print_saldo(cpf)
        except:
            print("Algo deu errado!!!")
        utils.pause()