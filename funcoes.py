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
    except Exception:
        print("\33[31mErro ao criar arquivo\33[m")

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
        print('\33[31mPlanilha não existe. Escolha a opção 1 para criar a planilha.\33[m')

def incluir_gastos(nome):
    try:
        nome_ = input('Digite o nome: ')
        categoria = input('Qual a categoria que ele pertence: ')
        valor = float(input('Qual valor gasto: '))
        file = open(nome, 'a')
        linha = f'\n{nome_},{categoria},{valor}'
        file.write(linha)
        file.close()
        print('\33[31mGasto incluído com sucesso.\33[m')
    except FileNotFoundError:
        print('\33[31mPlanilha não encontrada\33[m')
    except ValueError:
        print('\33[31mErro: Valor inválido. Certifique-se de digitar um número válido para o valor gasto.\33[m')

def atualizar_gastos(nome):
    try:
        file = open(nome, "r")
        linhas = list(file.readlines())
        file.close()
        for indice, linha in enumerate(linhas):
            dado = linha.strip().split(',')
            print(f'{indice}{dado[0]:^12}{dado[1]:^12}{dado[2]:^12}')

        linha_at = int(input("Qual linha você deseja atualizar? "))
        qnt_at = int(input("Quantas partes você quer atualizar? "))
        for i in range(qnt_at):
            coluna = input("Qual coluna você deseja atualizar? (nome, categoria ou valor) ")
            nova_palavra = input("O que você deseja colocar? ")
            atualizado= linhas[linha_at].strip().split(',')
            if coluna=="nome":
                atualizado[0] = nova_palavra
            if coluna=="categoria":
                atualizado[1] = nova_palavra
            if coluna=="valor":
                atualizado[2] = (nova_palavra)
            linhas[linha_at] = ','.join(atualizado) + '\n'
            file = open(nome, "w")
            file.writelines(linhas)
            file.close()
            print("Gastos atualizados com sucesso.")
    except FileNotFoundError:
        print("\33[31mArquivo não encontrado.\33[m")

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
        file.close()
        
        delecao = int(input("Digite o número da linha que deseja deletar: "))

        if delecao < len(arr_arq):
            arr_arq.pop(delecao)
        else:
            print("O número da linha é inválido.")

        with open("planilha.csv", "w") as file:
            for linha in arr_arq:
                file.write(','.join(linha) + '\n')
        file.close()
        print("\33[31mLinha deletada.\33[m")
    except ValueError:
         print("\33[31mEntrada inválida. Certifique-se de digitar um número inteiro.\33[m")

def soma_categoria(nome):
    cont=0
    filtro = input("Qual categoria você deseja ver a soma? ")
    try:
        file = open(nome, "r")
        for linha in file:
            i=0
            dado = linha.split(',')
            dado[i] = dado[i].replace('\n', '')
            i+=1
            for j in dado:
                if j == filtro:
                    print(f'{dado[0]:^12}{dado[1]:^12}{dado[2]:^12}')
                    inteiro=float(dado[2])
                    cont=cont+inteiro
        print(f'A soma total da categoria {filtro} R${cont}')
    except FileNotFoundError:
        print("\33[31mArquivo não encontrado.\33[m")
    finally:
        if 'file' in locals():
            file.close()

def criar_meta():
    try:
        nome_cofrinho=input("Digite um título para sua meta(sugestão: o nome do objeto): ")
        preco_cofrinho=float(input("Digite o valor da sua meta: \n"))
        file=open("meta.csv","w")
        file.write(f"{nome_cofrinho}\n")
        file.write(f"{preco_cofrinho}")
        file.close()
    except Exception:
        print("Erro ao criar arquivo")

def ver_meta():
    try:
        linhas_cofre=[]
        file=open("meta.csv","r")
        for linha in file:
            linhas_cofre.append(linha.strip())
        file.close()

        nome_cofrinho_arq=str(linhas_cofre[0])
        preco_cofrinho_arq=float(linhas_cofre[1])

        cont=0
        file=open("planilha.csv","r")
        for linha in file:
            dados = linha.lower().split(',')
            if 'meta' == dados[1] and nome_cofrinho_arq == dados[0]:
                print(f'{dados[0]:^12}{dados[1]:^12}{dados[2]:^12}')
                valor_presente=float(dados[2])
                cont += valor_presente
        valor_que_falta = preco_cofrinho_arq-cont
        if valor_que_falta > 0:
            print("Faltam R$ ",valor_que_falta,"para completar sua meta, não desista!")
        else:
            print("Parabéns, você alcançou a sua meta! Volte para o menu e crie uma nova meta.")
    except FileNotFoundError:
        print("\33[31mArquivo não encontrado.\33[m")