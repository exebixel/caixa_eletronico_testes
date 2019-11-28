from operaçoes import *
from utils import *

class interface():
    
    def __init__(self, cpf):
        self.cpf = cpf
    
    def start(self):
        """
            Gerencia a interface de usuario
        """
        op = self.menu()
        self.opcoes(op)
        if op != "q" and op != "w":
            self.start()
    
    def menu(self):
        """ 
            Menu do usuario, 
            aqui o usuario escolhe as operações \n
            cpf = identificador do usario logado 
        """
        op = 0
        print("a - Consulta de saldo")
        print("s - Saque")
        print("d - Deposito")
        print("w - Log out")
        print("q - Sair do programa")
        op = input("Digite uma operação: ")
        return op
        
           
    def opcoes(self, op):
        """
            Redireciona o usuario conforme a opção digitada pelo mesmo \n
            a = consulta de saldo \n
            s = saque \n
            d = deposito \n
            q = sair do programa \n
            w = log out
        """
        #consulta de saldo
        if op == "a":
            operacoes.saldo(self.cpf)

        #saque
        elif op == "s":
            operacoes.saque(self.cpf)                               
                
        # deposito
        elif op == "d": 
            operacoes.deposito(self.cpf)
        
        #sair
        elif op == "q":
            print("Volte sempre!!!")
        
        #log out
        elif op == "w":
            print("Volte sempre!!!")
            utils.pause()
            utils.clear()
        
        # fundo do poço
        else:
            print("Digite uma operação valida!!!")
            utils.pause()

    