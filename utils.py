import os
import platform

class utils():
    
    def clear():
        """
            Limpa a tela do console
        """
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        
    def pause():
        """
            Para o fluxo do codigo por um momento para 
            o usuario ver a saida de dados
        """
        print("\n Digite enter para continuar")
        input()
    
    def srtToInt(string):
        """
            Converte uma String em inteiro
        """
        try:
            num = int(string)
            return num
        except:
            print("ENTRE COM NÚMEROS INTEIROS!!!")