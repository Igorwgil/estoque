from functions.untils import limpar_tela

limpar_tela()

estoque_total = 0

try:
    opcao = int(input('[1] Repor estoque'))
except ValueError:
    print('Valor inválido. Somente números')
except:
    print('Erro inesperado.')

'''fazer vendas
repor estoque
consultar vendas
fechar programa
'''








