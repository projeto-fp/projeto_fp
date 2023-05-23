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
    for linha in file:
        dado = linha.split(',')
        dado[2] = dado[2].replace('\n', '')
        print(f'{dado[0]:^12}{dado[1]:^12}{dado[2]:^12}')
    print(file.read())
    file.close()


def incluir_gastos(): 
    nome=input('Digite o nome do gasto: ')
    categoria=input('Qual a categoria que ele pertence: ')
    valor=float(input('Qual valor gasto: '))
    file= open('planilha_gastos.csv', 'a')
    linha = f'\n{nome},{categoria},{valor}'
    file.write(linha)
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

def filtrar(nome):
    try:
        filtro = input("O que deseja pesquisar? ")
        file = open(nome, "r")
        for linha in file:
            dado = linha.lower().split(',')
            for j in dado:
                if j == filtro:
                    dado[2] = dado[2].replace('\n', '')
                    print(f'{dado[0]:^12}{dado[1]:^12}{dado[2]:^12}')
    except ValueError:
        print("Entrada inválida")
    file.close()

def deletar(nome):
    arr_arq = []
    with open(nome, "r+") as file:
        for indice, linha in enumerate(file):
            dado = linha.lower().split(',')
            arr_arq.append(dado)
            dado[2] = dado[2].replace('\n', '')
            print(f'{indice:^12}{dado[0]:^12}{dado[1]:^12}{dado[2]:^12}')
    
    delecao = int(input("Digite o número da linha que deseja deletar: "))

    if delecao < len(arr_arq):
        arr_arq.pop(delecao)
    else:
        print("O número da linha é inválido.")

    with open("planilha_gastos.csv", "w") as file:
        for linha in arr_arq:
            file.write(','.join(linha) + '\n')
    return