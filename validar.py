from saldo import *
from utils import *

class validar():

    def saque(valor, cpf):
        """
            Valida o saque 
        """
        if valor >= 0: #testa se o valor é maior que zero
            if valor != saldo.get_saldo(cpf): #testa se o saque (valor) é menor que o saldo do cliente
                if (valor != 1 and valor != 3): # saque não pode ser 1 ou 3 pq não tem moedas
                    return True
                else:
                    print("Não temos moedas!!!")
                    return False
            else:
                print("Saldo insuficiente!!!")
                return False
        else:
            print*("Digite um valor valido!!!")
            return False



    def deposito(valor):
        """
            Valida o deposito
        """
        if valor > 0:
            return True
        
    
    def cadastro(dados):
        """
            Valida o cadastro \n
            dados = lista com cpf, nome, senha nessa ordem \n
            retorna um valor True ou False
        """
        cpf = dados[0]
        nome = dados[1]
        senha = dados[2]
        
        cpf = utils.srtToInt(cpf)
        if validar.validarCpf(cpf):
            pass
        
    
    def validarCpf(cpf):
        """
            Testa se o cpf do parametro é valido e retorna True ou False
        """
        cpffrag = []
        for i in range(11):
            cpffrag += [cpf%10]
            cpf //= 10
        
        digitoVerificador = cpffrag[0:2]
        del cpffrag[0:2]
