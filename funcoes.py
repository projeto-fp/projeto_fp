def arquivoExiste(nome):
    try:
        file = open(nome, 'r')
        file.close()
    except FileNotFoundError:
        print("\33[31mArquivo não existe\33[m")
    else:
        return True

def criarArquivo(nome, cabecalho):
    try:
        file = open(nome, 'w', newline='', encoding='utf-8')
        file.write(f'{cabecalho}')
        file.close()
        print(f"Arquivo {nome} criado com sucesso")
    except OSError:
        print("Erro ao criar arquivo")

def ver_planilha(nome):
    try:
        file = open(nome,"r")
        for linha in file:
            dado = linha.split(',')
            dado[2] = dado[2].replace('\n', '')
            print(f'{dado[0]:^12}{dado[1]:^12}{dado[2]:^12}')
        print(file.read())
        file.close()
    except FileNotFoundError:
        print('\33[31mPlanilha não existe. Use a função planilha para criar.\33[m')

def incluir_gastos():
    try:
        nome = input('Digite o nome do gasto: ')
        categoria = input('Qual a categoria que ele pertence: ')
        valor = float(input('Qual valor gasto: '))
        file = open('planilha_gastos.csv', 'a')
        linha = f'\n{nome},{categoria},{valor}'
        file.write(linha)
        file.close()
        print('\33[31mGasto incluído com sucesso.\33[m')
    except ValueError:
        print('\33[31mErro: Valor inválido. Certifique-se de digitar um número válido para o valor gasto.\33[m')
    except IOError:
        print('\33[31mErro: Ocorreu um problema ao abrir ou gravar o arquivo.\33[m')
    except Exception as e:
        print('\33[31mOcorreu um erro inesperado:\33[m', e)


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
        filtro = str(input("Qual categoria deseja pesquisar? "))
        file = open(nome, "r")
        print(f'{"Nome":^12}{"Categoria":^12}{"Valor Gasto":^12}')
        for linha in file:
            dado = linha.lower().split(',')
            for j in dado:
                if j == filtro:
                    dado[2] = dado[2].replace('\n', '')
                    print(f'{dado[0]:^12}{dado[1]:^12}{dado[2]:^12}')
        file.close()
    except TypeError as e:
        print("\33[31mErro: Entrada inválida.\33[m,", e)

def deletar(nome):
    try:
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
    except ValueError:
         print("\33[31mEntrada inválida. Certifique-se de digitar um número inteiro.\33[m")
    