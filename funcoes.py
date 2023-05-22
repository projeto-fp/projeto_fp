def arquivoExiste(nome):
    try:
        file = open(nome, 'r')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        file = open(nome, 'w+')
        file.close()
    except:
        print("Erro ao criar arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")

# criarArquivo('planilha_gastos.csv')

# def incluir_gastos(): 
#     nome=input('Nome: ')
#     categoria=input('categoria: ')
#     valor=float(input('valor gasto: '))
#     import csv
#     with open('arquivo.csv', 'r+', newline='') as file:
#         writer = csv.writer(file)
#         file.seek(0,2)
#         writer.writerow([nome, categoria, valor])
#         file.close()
# incluir_gastos()
