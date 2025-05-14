import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

print('Possuo?[1]\nCriar conta[2]\nEntrar como visitante[3]')

tipo_log = int(input('Digite uma opção: '))

limpar_tela()

print('opção escolhida: ', tipo_log)
print()



