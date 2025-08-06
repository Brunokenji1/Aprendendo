while True:
    n1=input('Digite o primeiro numero: ')
    n2=input('Digite o segundo numero: ')

    try:
        n1_float = float(n1)
        n2_float = float(n2)
    except:
        print('DIGITE UM NUMERO')
        opcao=input("Quer sair :[S]im  [N]ão \n").lower()
        if opcao.startswith('s') is True:
            break
        continue

    math=input('Qual conta matematica:  +   -   *  /  %: ')

    if math == '+':
        print(f'A soma dos numero é: {n1_float+n2_float}')
    elif math == '-':
        print(f'A substração de n1 por n2 é: {n1_float-n2_float}')
    elif math == '*':
        print(f'A multiplicação de n1 por n2 é: {n1_float*n2_float}')
    elif math == '/':
        print(f'A divisão de n1 por n2 é: {n1_float/n2_float}')
    elif math == '%':
        print(f'o resto de n1 por n2 é: {n1_float%n2_float}')
    else:
        print('DIGITE UMA DAS OPÇÕES')
        break

    opcao=input("Quer sair :[S]im [N]ão: ").lower()
    if opcao.startswith('s') is True:
        break
    elif opcao.startswith('n') is True:
        continue

    print()