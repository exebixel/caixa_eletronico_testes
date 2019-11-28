

class cadastro():
    
    def entrada():
        print("CADASTRO")
        cpf = int(input("Digite seu CPF: "))
        nome = input("Digite seu NOME: ")
        senha = input("Digite sua SENHA: ")
        dadosParaCadastro = (cpf, nome, senha)
        return dadosParaCadastro
    
    
    def atualizardb():
        """
            Efetua o cadastro do cliente no banco de dados
        """
        try:
            sql = "INSERT INTO clientes VALUES(%s, %s, md5(%s), 0)"
            var = (cpf, nome, senha)
            mysql.alterdata(sql, var)
        except:
            print("Erro ao efetuar cadastro!!!")
    
    