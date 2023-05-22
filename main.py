import menu
import os
import funcoes as fc
import csv
# planilha_gastos=fc.incluir_gastos(nome='planilha_gastos.csv', cabecalho='Nome;Categoria;Valor Gasto ')
# lerPlanilha = fc.ver_planilha(nome='planilha_gastos.csv')
os.system('clear')
while True:
    resposta = menu.navegacao('Natália - Despesas Pessoais', ['Criar Planilha','Ver Planilha', 'Incluir gastos','Atualizar gastos', 'Deletar gastos', 'Pesquisar'])
    if resposta > 6:
        os.system('clear')
        print('\33[31mInsira algum valor de acordo com o menu de navegação\33[m')
    else:
        break
if resposta == 1: 
        if not fc.arquivoExiste("planilha_gastos.csv"):
            fc.criarArquivo("planilha_gastos.csv")
        else: 
             print("Arquivo já existe")
elif resposta == 2:
    print('ola2')
