from mysql import *
import pymysql
from values import *
from utils import *
from cadastro import *

class acesso():
    """ 
        Gerencia o acesso dos usuarios \n
        Faz login e cadastro
    """

    def login():
        """
            Efetua o login de um usuario
        """
        while True:
            cpf = input("Digite seu cpf: ")
            senha = input("Digite sua senha: ")
            
            try:
                sql = "SELECT nome FROM clientes \
                    WHERE cpf = %s AND senha = md5(%s)"
                var = (cpf, senha)
                result = mysql.select(sql, var)
                
                cont = 0
                for i in result:
                    cont +=1
                    print("Bem-vindo %s!!!" %(i[0]))
                    
                if cont == 1:
                    utils.pause()
                    return cpf
                else:
                    print("cpf e/ou senha incorretos!!! \n")
                    return 0
                    
            except:
                print("Erro ao fazer login!! \n ")
                input()
                break

    def cadastro():
        """
            Faz cadastro de usuarios para poderem acessar o sistema
        """
        dadosParaCadastro = cadastro.entrada()
        #if acesso.validarcpf(dadosParaCadastro):
        try:
            cpfs = values.get_cpfs()
            erro = 0
            for i in cpfs:
                if cpf == i[0]:
                    erro+=1
            if erro == 0:    
                cadastro.atualizardb()
            else:
                print("CPF já cadastrado!!!")
                print(" ")
        except:
            print("Erro ao fazer cadastro!!! ")

    def validarcpf(cpf):
        cpffrag = []
        for i in range(11):
            cpffrag += [cpf%10]
            cpf //= 10
        
        digitoVerificador = cpffrag[0:2]
        del cpffrag[0:2]

        print(cpffrag)
        print(digitoVerificador)
        
        soma = 0
        cont = 2
        for i in cpffrag:
            soma += i * cont
            cont += 1
        
        test = []
        

        return False

