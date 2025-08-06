valores = input('me de numeros separados por espaços: ').split()
lista_int = [int(x) for x in valores]
#print(lista_int)
for n in lista_int:
    print(n, type(n))