from Classe_Estoque import *

class Compra:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='Comercio'
        )
        self.loja = self.conexao.cursor()
        self.entrada = Estoque()
        self.list_compr = []

    def comprar(self):
        prod = 0
        entrada = input('Informe o codigo do Produto: ')
        for i in range(len(self.entrada.loja)):
            if entrada == self.entrada.loja[i].id:
                en = int(input('Informe a quantidade comprada: '))
                self.entrada.loja[i].quat += en
                self.list_compr.append(f'Entrada de {en} unidade do produto ' + self.entrada.loja[i].id)
            else:
                prod += 1
                if prod == len(self.entrada.loja):
                    print('Codigo não cadastrado!')

    def historico_compr(self):
        for i in self.list_compr:
            print('\n ', i)
            print('')
