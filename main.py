import menu
import os
import funcoes as fc
# planilha_gastos=fc.incluir_gastos(nome='planilha_gastos.csv', cabecalho='Nome;Categoria;Valor Gasto ')
# lerPlanilha = fc.ver_planilha(nome='planilha_gastos.csv')
# criar_arq = fc.criarArquivo(nome="planilha_gastos.csv", cabecalho='Nome;Categoria;Valor Gasto ')
nome = 'planilha_gastos.csv'
os.system('clear')
while True:
    resposta = menu.navegacao('Natália - Despesas Pessoais', ['Criar Planilha','Ver Planilha', 'Incluir gastos','Atualizar gastos', 'Deletar gastos', 'Pesquisar', 'Soma Gastos', 'Criar Meta', 'Ver Meta'])
    if resposta > 9:
        os.system('clear')
        print('\33[31mInsira algum valor de acordo com o menu de navegação\33[m')
    elif resposta == 0:
        print('\33[31mPrograma encerrado\33[m')
        break
    elif resposta == 1: 
            if not fc.arquivoExiste(nome):
                fc.criarArquivo(nome="planilha_gastos.csv", cabecalho='Nome,Categoria,Valor Gasto ')
            else: 
                print("Arquivo já existe")
    elif resposta == 2:
        fc.ver_planilha(nome)
    elif resposta == 3:
        fc.incluir_gastos()
    elif resposta == 4:
        fc.atualizar_gastos()
    elif resposta == 5:
        fc.deletar(nome)
    elif resposta == 6:
        fc.filtrar(nome)
    elif resposta == 7:
        fc.soma_categoria()
    elif resposta == 8:
        fc.criar_meta()
    elif resposta == 9:
        fc.ver_meta()
