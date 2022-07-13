import mysql.connector
from Classe_Produtos import *
from Classe_Fabricante import *

class Estoque:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='Comercio')
        self.loja = self.conexao.cursor()

    # Create
    def cadastro_fabct(self, id, nome, cnpj):
        obj_cadastro_F = Fabricante(id, nome, cnpj)
        comando_sql = f'insert into Fabricante' \
                      f'(nome, cnpj)' \
                      f' value ' \
                      f'("{obj_cadastro_F.nome}", "{obj_cadastro_F.cnpj}")'
        self.loja.execute(comando_sql)
        self.conexao.commit()
        print('Cadastro realizado com sucesso!')

    def cadastro_prod(self, idP, nome, id_fabct, quat):
        obj_cadastro_P = Produtos(idP, nome, id_fabct, quat)
        comando_sql = f'insert into Produtos ' \
                      f'(nome, id_fabct, quat) ' \
                      f' value ' \
                      f'("{obj_cadastro_P.nome}", {obj_cadastro_P.id_fabct}, {obj_cadastro_P.quat})'
        try:
            self.loja.execute(comando_sql)
            self.conexao.commit()
            print('Cadastro concluido com sucesso!')
        except:
            print('Aqui não se encontra este cadastro!!! ')

    # Read
    def lista_produtos(self):
        comando_sql = 'select * from Produtos'
        self.loja.execute(comando_sql)
        lista_p = self.loja.fetchall()
        for i in lista_p:
            print(i)

    # Update
    def alterar_nprod(self, atributo, valor, idP):
        comando_sql = f'update Produtos set {atributo} = "{valor}" where idP = {idP}'
        self.loja.execute(comando_sql)
        self.conexao.commit()

    def alterar_nfabct(self, atributo, valor, id):
        comando_sql = f'update Fabricante set {atributo} = "{valor}" where id = {id}'
        self.loja.execute(comando_sql)
        self.conexao.commit()

    # Delete
    def excluir_prod(self, idP):
        comando_sql = f'delete from Produtos where idP = {idP}'
        self.loja.execute(comando_sql)
        self.conexao.commit()

    def excluir_fabct(self, id):
        comando_sql = f'delete from fabricante where id = {id}'
        self.loja.execute(comando_sql)
        self.conexao.commit()
