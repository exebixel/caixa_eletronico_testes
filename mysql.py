import pymysql

class mysql():
    
    def conn():
        """ Inicia uma conexão com o bando de dados mysql ou mariadb \n
            host= localhost \n
            user=root \n
            banco de dados=caixa"""
        try:
            bd = pymysql.connect(
                host='localhost', 
                user='root', 
                password='toor', 
                db='caixa')
            return bd
        except:
            print("Erro ao conectar com o banco de dados: " )
            
            
    def close(bd):
        """ Fecha uma conexão com o banco de dados \n
            bd = "banco de dados a ser fechado" """
        try:
            if bd != None:
                bd.close()
        except:
            print("Erro ao fechar a  conexão: " )
            
            
    
    def alterdata(sql, var):
        """ metodo para alterar os dados do bd 
        sql = variavel com o comando sql
        var = variaveis do comando sql
        exemplo:
            sql = "UPDATE table SET column = %s"
            var = ("teste")
            %s é o teste """
        try:
            #cria a conexão com o banco de dados
            bd = mysql.conn()
            #isso eu não sei pra que serve mas sei que precisa
            cursor = bd.cursor()
            
            #executa o comando com as variaveis
            cursor.execute(sql, var)
            #torna as mudanças persistentes
            bd.commit()
            
            #fecha a conexão com o banco de dados
            mysql.close(bd)
            
        except:
            #comando que avisa que deu merda e mostra o erro
            print("Erro ao conectar com o banco de dados: \n " )
            # desfaz as mudanças do comando digitado acima
            bd.rollback()
            input()
            
    def select(sql, var):
        """ Executa strings sql select e retorna o resultado da pesquisa \n
            sql = string sql \n
            var = variaveis da string sql \n
            exemplo: \n
            sql = "SELECT * FROM table WHERE columns = %s" \n
            var = ("dado usado no %s da string sql") """
        try:
            bd = mysql.conn()
            cursor = bd.cursor()
            
            cursor.execute(sql, var)
            
            result = cursor.fetchall()
            
            mysql.close(bd)
            
            return result
            
        except:
            print("Erro ao recuperar os dados!!! \n ")