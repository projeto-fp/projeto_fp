def navegacao(titulo ,componentes):
    print('•'*50)
    print(f'{titulo.center(50)}')
    print('•'*50)
    cont=1
    for i in componentes:
        print(f'\33[33m{cont} - \33[34m{i}\33[m')
        cont+=1
    print('•'*50)
    resposta = int(input('digite a operação que deseja realizar: '))
    return(int(resposta))