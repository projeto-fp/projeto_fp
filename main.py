import menu
import os
# planilha_gastos=lc.criararquivo(nome='planilha_gastos.csv', cabeçalho='Nome da Conta|Valor Gasto ')
os.system('clear')
while True:
    resposta = menu.navegacao('Natália - Despesas Pessoais', ['Ver Planilha', 'Incluir gastos','Atualizar gastos', 'Deletar gastos', 'Pesquisar'])
    if resposta > 5:
        os.system('clear')
        print('\33[31mInsira algum valor de acordo com o menu de navegação\33[m')
    else:
        break
