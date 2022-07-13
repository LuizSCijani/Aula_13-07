from Classe_Compra import *
from Classe_Venda import Venda


class Menu:
    def __init__(self):
        estoque_prod = Estoque()
        compra = Compra()
        venda = Venda()

        venda.entrada = estoque_prod
        compra.entrada = estoque_prod

        ##iniciar menu
        while True:
            print('Menu de operações'
                  '\n1 - Cadastrar fabricante'
                  '\n2 - Cadastrar produtos'
                  '\n3 - Listar todos'
                  '\n4 - Alterar produto'
                  '\n5 - Alterar fabricante'
                  '\n6 - Entrada de Produtos'
                  '\n7 - Saida de Produtos'
                  '\n8 - Excluir cadastro do produto'
                  '\n9 - Excluir cadastro do fabricante'
                  '\n0 - Sair')
            entrada = input('Informe a operação desejada: ')

            if entrada == '1':
                id = None
                nome = input('Informe o nome: ')
                cnpj = input('informe o cnpj: ')
                estoque_prod.cadastro_fabct(id, nome, cnpj)

            elif entrada == '2':
                idP = None
                id_fabct = input('Informe o id do fabricante: ')
                nome = input('Informe o nome: ')
                quat = 0
                estoque_prod.cadastro_prod(idP, nome, id_fabct, quat)

            elif entrada == '3':
                estoque_prod.lista_produtos()

            elif entrada == '4':
                idP = input('Informe o codigo do produto: ')
                valor = input('Informe o novo nome: ')
                atributo = 'nome'
                estoque_prod.alterar_nprod(atributo, valor, idP)

            elif entrada == '5':
                id = input('Informe o codigo do fabricante: ')
                valor = input('Informe o novo nome: ')
                atributo = 'nome'
                estoque_prod.alterar_nfabct(atributo, valor, id)

            elif entrada == '6':
                compra.comprar()

            elif entrada == '7':
                venda.vender()

            elif entrada == '8':
                idP = input('Informe o codigo do produto: ')
                estoque_prod.excluir_prod(idP)

            elif entrada == '9':
                id = input('Informe o codigo do fabricante: ')
                estoque_prod.excluir_fabct(id)

            elif entrada == '0':
                break
            else:
                print('opção errada!')
