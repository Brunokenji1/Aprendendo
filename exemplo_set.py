letras=set()
while True:
    letra=input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letra:
        print('Parabens')
        break

    print(letras)