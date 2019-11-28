from acesso import *
from menu import *
from utils import *

utils.clear()

def main():
    op = 0
    while True:
        print("Digite 'q' para sair")
        op = input("Já tem login? (s/n): ")
        
        if op == "s":
            cpf = acesso.login()
            if cpf != 0:
                cti = interface(cpf)
                cti.start()
                """    main()
                else:
                    break """
                
        elif op == "n":
            acesso.cadastro()           
            
        elif op == "q":
            print("Volte sempre!!!")
            break
        
        else:
            print("Digite uma opção valida!!!")

main()