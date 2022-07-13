from Classe_Estoque import *

class Venda:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host='localhost',
            user='root',
            password='q1w2e3',
            database='Comercio'
        )
        self.loja = self.conexao.cursor()
        self.entrada = Estoque()
        self.list_vend = []

    def vender(self):
        prod = 0
        entrada = input('Informe o codigo do Produto: ')
        for i in range(len(self.entrada.loja)):
            if entrada == self.entrada.loja[i].id:
                en = int(input('Informe a quantidade vendida: '))
                self.entrada.loja[i].quat -= en
                self.list_vend.append(f'Entrada de {en} unidade do produto ' + self.entrada.loja[i].id)
            else:
                prod -= 1
                if prod == len(self.entrada.loja):
                    print('Codigo não cadastrado!')

    def historico_vend(self):
        for i in self.list_vend:
            print('\n ', i)
            print('')
