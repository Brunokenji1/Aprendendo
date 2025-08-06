import os
palavra_secreta = 'espinafre'
numero_tentativas = 0
palavras_certas = ''


while True:
 
    palavra_digitada=input('Digite uma palavra: ')
    numero_tentativas+=1
    if palavra_digitada in palavra_secreta:
        palavras_certas+=palavra_digitada
    palavra_atual = ''
    
    
    for palavra in palavra_secreta:
        if palavra in palavras_certas:
            palavra_atual+=palavra
        else:
            palavra_atual+='*'
    print('Palavra formad: ', palavra_atual)

    if palavra_atual == palavra_secreta:
        os.system('cls')
        print("VOCE ACERTOU A PALAVRA SECRETA: ", palavra_secreta)
        print('Suas tentativas: ', numero_tentativas)
        palavras_certas = ''
        numero_tentativas = 0
        break