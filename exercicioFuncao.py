def multiplicador(multiplo):
    def mult(numero):
        return multiplo*numero
    return mult

multiplicador_por_2 = multiplicador(2)
multiplicador_por_3 = multiplicador(3)
multiplicador_por_4 = multiplicador(4)
for numero in [2, 3, 4, 5, 6, 7]:
    print('Numero multiplicado por 2 x', numero ,' = ', multiplicador_por_2(numero))
for numero in [2, 3, 4, 5, 6, 7]:
    print('Numero multiplicado por 3 x', numero ,' = ', multiplicador_por_3(numero))
for numero in [2, 3, 4, 5, 6, 7]:
    print('Numero multiplicado por 4 x', numero ,' = ', multiplicador_por_4(numero))