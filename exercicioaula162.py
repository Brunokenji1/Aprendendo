#01/08/2025
def cria_funcao(funcao, x):
    def interna(y):
        return funcao(x, y)
    return interna

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

soma_5 = cria_funcao(soma, 5)
print(soma_5(3))

multiplica_por_dez = cria_funcao(multiplica, 10)
print(multiplica_por_dez(3))