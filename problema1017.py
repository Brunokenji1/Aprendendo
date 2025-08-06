try:
    h = int(input())
    vm = int(input())
    d = h*vm
    gasto = d/12
    print(f'{gasto:.3f}')
except ValueError:
    print('coloque numeros inteiros')


