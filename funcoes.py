import csv
def arquivoExiste(nome):
    try:
        file = open(nome, 'r')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome, cabecalho):
    try:
        file = open(nome, 'w', newline='', encoding='utf-8')
        file.write(f'{cabecalho}')
        file.close()
    except:
        print("Erro ao criar arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")

def ver_planilha(nome):
    file=open(nome,"r")
    print(file.read())
    file.close()




def incluir_gastos(): 
    nome=input('Digite o nome do gasto: ')
    categoria=input('Qual a categoria que ele pertence: ')
    valor=float(input('Qual valor gasto: '))
    with open('planilha_gastos.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome,categoria,valor])
        file.close()
    print('Gasto incluído com sucesso.')


def atualizar_gastos():
    nome=input("Antigo nome:")
    novo_nome=input("Digite o novo nome: ")
    categoria=input("Antiga categoria")
    nova_categoria=input("Nova categoria: ")
    atualize = open("planilha_gastos.csv", "r") 
    atualize = ''.join([i for i in atualize])  
    atualize = atualize.replace(nome, novo_nome)  
    atualize = atualize.replace(categoria,nova_categoria) 
    atualize_arq = open("planilha_gastos.csv","w") 
    atualize_arq.writelines(atualize) 
    atualize_arq.close()
    file=open("planilha_gastos.csv","r")
    print(file.read())
    file.close()
    print("Gastos atualizados com sucesso.")

