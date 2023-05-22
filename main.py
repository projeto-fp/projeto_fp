import menu
import os
import funcoes as fc
import csv
# planilha_gastos=fc.incluir_gastos(nome='planilha_gastos.csv', cabecalho='Nome;Categoria;Valor Gasto ')
# lerPlanilha = fc.ver_planilha(nome='planilha_gastos.csv')
# criar_arq = fc.criarArquivo(nome="planilha_gastos.csv", cabecalho='Nome;Categoria;Valor Gasto ')
nome = 'planilha_gastos.csv'
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
            fc.criarArquivo(nome="planilha_gastos.csv", cabecalho='Nome;Categoria;Valor Gasto ')
        else: 
             print("Arquivo já existe")
elif resposta == 2:
    fc.ver_planilha(nome)
elif resposta == 3:
    fc.incluir_gastos()
elif resposta == 4:
    fc.ver_planilha(nome)
    fc.atualizar_gastos()
elif resposta == 6:
     fc.filtrar()
