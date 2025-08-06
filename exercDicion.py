perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
qtd=0
for lista in perguntas:
    print("Pergunta: ",lista['Pergunta'] )
    print()
    print("Opções: ")
    opcoes=lista['Opções']
    for  i, alternativa in enumerate(opcoes):
        print(f'{i}) ', alternativa)
    resposta=input("Escolha uma opção: ")
    resposta_int=None
    qtd_opcoes=len(opcoes)
    acertou = False
    if resposta.isdigit():
        resposta_int=int(resposta)
    if resposta_int is not None:
        if  resposta_int>=0 and resposta_int<qtd_opcoes:
            if opcoes[resposta_int] == lista['Resposta']:
                acertou= True
    
    if acertou:
        print('acertou :) ')
    else:
        print('Errou :( ')


print("Você acertou ", qtd, " de 3 questões")
print()