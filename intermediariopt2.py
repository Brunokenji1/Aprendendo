#22/07/2025
#Dictionary comprehension e set comprehension
#isinstance - ele vai verificar se ele é de determinado tipo 
produto = { 
    'nome' : 'Caneta',
    'preco' : '2.5',
    'categoria' : 'Escritorio'
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor  #nesse caso ele vai verificar se valor  é str, se for ele executa o for se não ele da o valor sem ter o 'upper'
    for chave, valor in produto.items()

}
print(dc)
# dc = {
#     chave: valor
#     if isinstance(valor, (int, float)) else valor.upper()  #nesse caso ele vai verificar se valor  é int ou float, se for ele executa o for se não ele da o valor.upper()
#     for chave, valor in produto.items()
# }

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),

]
dc = {
    chave: valor 
    for chave, valor in lista
}
print(dc)

s1 = {i ** 2 for i in range(10)}
print(s1)
print(set(range(10)))

#isinstace ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#para saber se objeto é de determinado tipo
print('\nISINSTACE')
lista = []
lista = [
    'a', 1, 1.2, True, [0, 1, 2], {0, 1}, {'nome': 'ped'}
]
for item in lista:
    if isinstance(item, set):
        print(item, isinstance(item, set))
print()

for item in lista:
    print(item, isinstance(item, set))
print()

for item in lista:
    if isinstance(item, set):
        print('SET')
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print('STR')
        print(item.upper())

    elif isinstance(item, (int, float)):
        print('NUM')
        print(item, item * 2)
    else:
        print('OUTRO')
        print(item)
print()

#valores Truthy e Falsy, Tipo mutáveis e imutáveis---------------------------------------------------------------------------------------------------------------------------------------
#mutáveis []  {}  set()
#imutáveis ()  ""  0  0.0  None  False  range(0, 10)
#todo esses são falsy, se não estiver ai ja é truthy
lista = [] 
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)
def falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE', falsy('TESTE'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteiro=}', falsy(inteiro))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo))

#dir, hasattr e getattr em python -------------------------------------------------------------------------------------------------------------------
#dir - mostra todos os nomes definidos dentro de string
#hasattr - vai checar dinamicamente se o objeto tem esse atributo, vai verificar se determinado obj tem determinado nome
#getattr - posso executar ou pegar o valor desse produto

print('\ndir, hasattr e getattr em python')
string = 'Luz'
#hasattr
if hasattr(string, 'upper'): # o nome do metodo sempre vai vim em string 'upper'
    print('Existe upper')
    print(string.upper())

metodo = 'upper'
if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
    print(string)
else:
    print('Não existe o método', metodo)

#  Iterables e Iterators em python aula145-------------------------------------------------------------------------------------------------------
print('\n Iterables e Iterators em python')
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) #tem__iter__e__next__
print(next(iterator))
print(next(iterator))
print(next(iterator))

#Generator expression aula146 -----------------------------------------------------------------------------------------------------------------------------
#generator é uma função que pausa em um determinado lugar que voc~e der e volta, pausa
# a lista vai salvando todos os dados na memoria ja, mas o generator não, o generator ele so te entrega um valor por vez, é uma função que pausa
#o generator os dados não estão na memoria, ele fica esperando você pedir um valor para ele
print('\nGenerator expression')
import sys
generator01 = (n for n in range(1000))
print(sys.getsizeof(generator01))  #sys.getsizeof --> você ve o tamanho por bytes
lista = []
# lista = [n for n in range(1000)]
# print(sys.getsizeof(lista))

#generator functions aula 147 -------------------------------------------------------------------------------------------------------------------------------------
#introdução às Generator Functions em Python
# generator = (n for n in range(100000))

def generator(n=0):
    yield  1  # toda função generator usa 'yield', que ele pausa | vc executa a função e pausa aqui
    print('Continua....')
    yield 2  # Pausa
    print('Mais uma ....')
    yield 3 # Pausa
    print('Fim')
    yield 4
    return 'ACABOU'  # quando ja tem 'yield' o return muda o funcionamento, agora ele levanta uma exeção de stopinteration com o valor que você coloca no return

gen = generator(n=0)
print(next(gen))
print(next(gen))
print(next(gen))

def exibirvaloresiteraveis(m):
    for n in m:
        print(n)
# for n in gen:
#     print(n)
print()
def generator02(n=0, maximum=10):
    while True:

        yield n

        n += 1
        if n > maximum:
            return

gen02 = generator02()
exibirvaloresiteraveis(gen02)

gen04 = generator02(n=2, maximum=30)
exibirvaloresiteraveis(gen04)

#23/07/2025 
# Yield from aula148 -----------------------------------------------------------------------------------------------------------------------------------------------
def gen1():
    print('COMECOU GEN1')
    yield 1
    yield 2
    yield 3
    print('ACABOU GEN1')


def gen3():
    print('COMECOU GEN3')
    yield 10
    yield 20
    yield 30
    print('ACABOU GEN3')


def gen2(gen=None):
    print('COMECOU GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('ACABOU GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()
for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()

# (Parte1) try e except para tratar exceções aula149 e 150-------------------------------------------------------------------------------------------------------------------------
# a = 18
# b = 0
# c = a / b

try:
    a = 18
    b = 0
    # print(b[0])
    print('Linha 1'[1000])
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:  #eu posso fazer uma tuple de except
    print('TypeError + IndexError')
    print('MSG: ', error)
    print('NOME: ', error.__class__.__name__)  #para saber qual error 
except Exception:  #o maior
    print('ERRO DESCONHECIDO.')

print('CONTINUAR')

# try, except, else e finally aula151 -------------------------------------------------------------------------------------------------------------------------------------------------------------
try:
    print('Abrir arquivo')
    print(8/0)
except ZeroDivisionError as erro:
    print('DIVIDIU ZERO')
    print(erro)
except (TypeError, NameError) as e:
    print(e.__class__.__name__)
except Exception:
    print("ERRO DESCONHECIDO")
else:
    print("NÃO DEU ERRO") # se o codigo foi executado com sucesso ele acessa o else
finally:   # É UM BLOCO QUE SEMPRE SERA EXECUTADO   
    print('FECHAR ARQUIVO')

# RAISE - LANÇANDO EXCEÇÕES ( ERROS ) AULA152 -------------------------------------------------------------------------------------------------------------------------------------------------------------
print('\nRAISE')
print(123)
#raise ValueError('deu errooo')
print(345)

def divide(n, d):
    try:
        return n / d
    except ZeroDivisionError:
        return n
        #print('----')
        #raise #posso relançar o erro

def nao_pode_ser_zero(d):
    if d == 0:
        raise ZeroDivisionError('Voce esta dividindo por zero')  
        #estou criando o meu proprio erro
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float.'
            f'"{tipo_n.__name__}" enviado'
        )
    return True

def divide01(n, d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_pode_ser_zero(d)
    return n / d

#print(divide(8, 0))
print(divide01(8, 2))

#24/07/2025
#muda o nome de um modulo ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import sys as s # muda o nome do modulo para 's'

# importar parte do modulo e trocar o nome de alguns objetos do modulo
from sys import exit as ex, platform as pf

# Modularização - Entendendo os seus próprios módulos Python -------------------------------------------------------------------------------------------------------------------------------------------------------
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

#estou importando uma psta para a main
print('\nImport')
import testimpor_m
try:
    import sys
    sys.path.append('/home')
except ModuleNotFoundError:
    ...
print('Este módulo se chama', __name__)
print(*sys.path, sep='\n')

#25/07/2025
#recarregando modulos, importlib e singleton aula98 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
print('\nrecarregando modulos, importlib e singleton')
import aula98_m # os modulos do python são singleton, ou seja ele so entrega uma vez
print(aula98_m.variavel)
for i in range(10):
    print(i)
    import aula98_m
print('fim')
# aqui eu recarrego esse modulo e cosigo mostrar mais vezes
import importlib
for i in range(10):
    importlib.reload( aula98_m)
    print(i)
print('fim')

# introdução a package, olhas aula99_package---------------------------------------------------------------------------------------------------------------------------------------------------------------


# Variáveis livres + nonlocal (locals, globals) aula164-----------------------------------------------------------------------------------------------------------------------------------------------------------
# print(globals())  #mostra tudo que esta definido
# def fora(x):
#     a = x

#     def dentro():
#         # print(locals())  #mostra tudo que esta definido naquele lugar e que pode ser acessado naquele lugar

#         return a
#     return dentro


# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())
def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar=''):
        nonlocal valor_final  # eu busco essa var5iavel no escopo da função, pois sem isso ele não puxa uma variavel que esta no local da função anterior
        #nonlocal consigo mudar o valor
        valor_final += valor_a_concatenar
        return valor_final
    return interna


c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print(final)


# Funções decoradoras e decoradores -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao01(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


inverte_string_checando_parametro = criar_funcao01(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)

# Decoradores são "Syntax Sugar" (Açúcar sintático)
#usando o decorador


# def criar_funcao(func):
#     def interna(*args, **kwargs):
#         print('Vou te decorar')
#         for arg in args:
#             e_string(arg)
#         resultado = func(*args, **kwargs)
#         print(f'O seu resultado foi {resultado}.')
#         print('Ok, agora você foi decorada')
#         return resultado
#     return interna


# @criar_funcao  #decorador--------------
# def inverte_string(string):
#     print(f'{inverte_string.__name__}')
#     return string[::-1]


# def e_string(param):
#     if not isinstance(param, str):
#         raise TypeError('param deve ser uma string')


# invertida = inverte_string('123')  # fica bem mais simples de chamar a função
# print(invertida)

#04/08/2025
# Decoradores com parametros --------------------------------------------------------------------------------------------------------------------------------------------------------------
def fabrica_de_decoradores(a=None, b=None, c=None):   #posso usar esses parametros a, b, c para configurar meu decorador, aqui no caso eles estão recebendo nada
    def fabrica_de_funcoes(func):
        print('decoradora 1')
        def aninhada(*args, **kwargs):
            print('Parametros do decorador, ', a, b, c)
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes

# def fabrica_de_decoradores(a=None, b=None, c=None):  #posso usar esses parametros a, b, c para configurar meu decorador, aqui no caso eles estão recebendo nada
#     return fabrica_de_funcoes

@fabrica_de_decoradores()
def soma(x, y):
    return x+y


multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

soma_10_com_5 = soma(10,5)
print(soma_10_com_5)
print(multiplica(5,10))

# Ordem dos decoradores  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------
def parametros_decorador(nome):
    def decorador(func):
        print('Decorador:', nome)

        def sua_nova_funcao(*args, **kwargs):
            res = func(*args, **kwargs)
            final = f'{res} {nome}'
            return final
        return sua_nova_funcao
    return decorador


@parametros_decorador(nome='5')
@parametros_decorador(nome='4')
@parametros_decorador(nome='3')
@parametros_decorador(nome='2')
@parametros_decorador(nome='1')  # é de baixo para cima
def soma01(x, y):
    return x + y


dez_mais_cinco = soma01(10, 5)
print(dez_mais_cinco)
