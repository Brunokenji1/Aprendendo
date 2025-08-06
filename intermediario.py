##19/06/2025
#random ------------------------------------------------------------------------------------------------------------------
#randint - um numero aleatorio inteiro 
print()
import random
for i in range(9):
    nove_digitos = ''
    nove_digitos += str(random.randint(0, 9))
print(nove_digitos)


#20/06/2025
#função -----------------------------------------------------------------------------------------------------------------
#função retorna nada um None
def soma(n1, n2):
    print(f'{n1=} + {n2=} | n1 + n2 = ', n1+n2)

soma(4, 2)
soma(5, n2=5)
#soma(n1=5, 5) #vai dar erro, apartir do momento que voce nomeia um argumento todos os proximos precisao estar nomeados
print(soma(4,2))

#27/06/2025
#escopo--------------------------------------------------------------------------------------
# TODA VEZ QUE DECLARO UMA NOVA VARIAVEL COM O MSM NOME EM UMA FUNÇÃO ELA VAI SER UMA NOVA VARIAVEL
x = 1
def escopo():
    x=10 #não é o mesmo x que esta fora
    def outra_funcao():  #essa função so existe quando eu chamo a fucao que esta fora, escopo()
        x=20
        y = 2
        print(x, y)
    outra_funcao()
    #print(y) o de fora não consegue pegar variavel mais interna
    print(x)
print(x)
escopo()
print(x)

y = 1
def escopo1():
    global y  # muda em todos os lugares a partir desse escopo e os anteriores, o escopo dentro não muda
    y=10
    def outra_funcao1():  
        y=20
        
        print(y)
    outra_funcao1()
  
    print(y)
print(y)
escopo1()
print(y)

#30/06/2025
#def return ---------------------------------------------------------------------------------------------

def soma01(x, y):
    return x + y
soma1 = soma01(2, 2)
soma2 = soma01(3, 3)
print(soma1 + soma2)

#03/07/2025
#  *args

def soma02(*args):
    #print(args, type(args), list(args))
    total02=0
    for numero in args:
        print('Total', total02, numero)
        total02 = total02 + numero
        print('TTotal', total02)
        print(total02)
soma02(1, 2, 3, 4, 5, 6)

#04/072025
# sum ----------------------------------------------------------------------------------------------
print()
numeros01 = 1, 2, 4, 5, 6, 7, 78
print(sum(numeros01))  #faz a soma tbm

#exercicio função --------------------------------------------------------------------------------
#função de multiplicar
print()
def multi (*args):
    multiplicacao=1
    for m in args:
        multiplicacao*=m
    return multiplicacao
    
res=multi(1*2*3*4*5)
print(type(res))
print(res)

#função que verifica se é par ou impar
def imparPar(num):
    if num%2==0:
        return True
    elif num%2==1:
        return False
#__________________________________________________________
# def imparPar(num):
#     if num%2==0:
#         return True    #quando o colando ja passa por um return ele sai da função
#     return False
#__________________________________________________________   
# def imparPar (numero):   #tambem serve 
#     return numero%2 ==0

if(imparPar(res)):
    print('numero par')
else:
    print('numero impar')

#mais função ---------------------------------------------------------------------------------------------------------------------
print()
def saudacao(msg):
    return msg
saudacao_2=saudacao  #  'saudacao_2' vai apontar para a mesma função 'saudacao'
print(saudacao_2('oiiiii'))
def executa(funcao, texto):
    return funcao(texto)
v=executa(saudacao, 'bom dia')
print(v) 


def saudacao_01(msg, nome, idade):
    return f'{msg} {nome} você tem {idade}'
def executa_01(funcao, *args):
    return funcao(*args)
print(executa_01(saudacao_01, 'bom dia', 'chaves', 22)) 

# closure ----------------------------------------------------------------------------------------------------------------
#e funções que retornam outras funções
#ele salva as variaveis na memoria, pega e depois fecha


#opcao com o parametro tudo junto
# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome} !'
#     return saudar

#opcao com o parametro tudo junto
# s1 = criar_saudacao('bom dia', 'bru')
# s2 = criar_saudacao('boa noite', 'bru')
# print(s1())
# print(s2())


#posso criar uma função que cria outras
print()
def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome} !'
    return saudar

falar_bom_dia = criar_saudacao('bom dia')  #-> saudacao vai receber o bom dia
falar_boa_noite = criar_saudacao('boa noite')  #-> saudacao vai receber o boa noite
 # assim meio que crio duas funções, uma para bom dia e outra para boa noite
print(falar_bom_dia('bru'))
print(falar_boa_noite('bruno'))

for nome in ['Br', 'Isa', 'Ped', 'Mur']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))

#dicionários em Python (tipo dict)  ----------------------------------------------------------------------------------------
#dicionários são estruturas de dados do tipo par de "chave" e "valor"
#Usamos as chaves- {} - ou a classe dict para criar dicionários

print()
print("dicionários em Python (tipo dict)...")
pessoa = {
    'nome' : 'Bebe',
    'sobrenome' : 'linda',
    'idade' : 19,
    'altura' : 1.5,
    'endereços' : [  #UMA LISTA COM OUTROS DICIONARIOS DENTRO
        {'rua': 'taltal', 'numero' : 123},  
        {'rua': 'outra rua', 'numero' : 890},
    ],

}
# pessoa = dict(nome='Amor')
# print(pessoa)

print(pessoa)
print(pessoa['nome'])
print(pessoa['altura'])
print()
for chave in pessoa:
    print(chave)
    print(chave, pessoa[chave])
    print()

#11/07/2025
# MANIPULANDO CHAVES E VALORES EM DICIONARIOS ------------------------------------------------------------------------------------
print("MANIPULANDO CHAVES E VALORES EM DICIONARIOS...")
pessoa02 = {}

chave02 = 'nome'
pessoa02[chave02] = 'tokyo drift'
pessoa02['sobrenome'] = 'japan'

print(pessoa02)
print(pessoa02[chave02])
pessoa02[chave02] = 'drift'

print(pessoa02[chave02])
print(pessoa02['nome'])

del pessoa02['sobrenome']
print(pessoa02)
#print(pessoa02['sobrenome'])  #não existe mais

print(pessoa02.get('sobrenome', None))  # O 'get' tenta obter uma chave, se não conseguir ele retorna None
if pessoa02.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa02['sobrenome'])
print()

#Métodos
#len - quantidade de chaves
#keys - retorna as chaves, que no caso daqui o nome e o sobrenome
#values - retorna os valores que estão nas chaves
#items - ele retorna o valor da chave e a do valor 
#setdefault - adiciona calor se a chave não existir
#copy - retorna uma cópia rasa (shallow copy), ela copia os valores imutaveis e linca os mutaveis(lista, etc)
#get - vai verificar se existe tal chave, se não existir ele retorna None ou o valor que você der, se existir ele so puxa o valor
#pop - Apaga um item com a chave especificada (del)
#popitem - Apaga a ultima chave do cicionario
#update - Cria uma nova chave ou altera uma ja existente

print('metodos...')
pessoa03 = {
    'nome' : 'arroz',
    'sobrenome' : 'feijão',
}

#len
print(pessoa03.__len__())  #__len__()  retorna a quantidade de chaves
print(len(pessoa03)) #mesma coisa de __len__
print()

#keys
print(pessoa03.keys())  #retorna as chaves
print(tuple(pessoa03.keys()))
print(list(pessoa03.keys()))
for chave03 in pessoa03.keys():
    print (chave03)
print()

#values
print(pessoa03.values())
print(tuple(pessoa03.values()))
print(list(pessoa03.values()))
for valor03 in pessoa03.values():
    print(valor03)
print()

# items
print(pessoa03.items())
print(tuple(pessoa03.items()))
print(list(pessoa03.items()))
for chave, valor in pessoa03.items():
    print("A CHAVE É: ", chave, "|| E O VALOR É:", valor)
print()

#setdefault
pessoa03.setdefault('idade', '10') # se essa chave não existe no dicionario, ela define um valor padrão, mas se ja tiver essa chave ela não é alterada
print(pessoa03['idade'])
print()

#copy
#no copy ele copia a mesma lista, copia os valores imutaveis e linca os valores mutaveis
d1 = {
    'c1' : 1,
    'c2' : 2,
    'l1' : [0, 1, 2],
}

#d2 = d1  #o d2 esta apontando para o dicionario d1, entao se eu altero um eu vou acabar alterando o outro

d2 = d1.copy()
d2['c1'] = 1000
d2['l1'][1]=999999

print(d1)
print(d2)
print()

import copy # modulo que faz uma copia profunda  deepcopy
d2=copy.deepcopy(d1)
d2['c1'] = 22222
d2['l1'][1]=4444
print(d1)
print(d2)
print()

#get
print(pessoa03.get('nome'))
print(pessoa03.get('nome meio'))
print(pessoa03.get('nome meio', 'não existe'))
print()

#pop
nome03=pessoa03.pop('nome') #apaga a chave especificada, nesse caso a variavel nome03 resebe o valor da chave nome e depois e apagado do dicionario
print(nome03)
print(pessoa03)
print()

#popitem
ultima_chave = pessoa03.popitem() # não passa a chave
print(ultima_chave)
print(pessoa03)
print()

#update
#ela cria uma nova chave ou altera uma ja existente
pessoa03.update({
    'nome' : 'novo valor',
    'sobrenome' : 'feijoada'
})
print(pessoa03)

pessoa03.update(nome= 'bom dia', altura='170')
print(pessoa03)
tupla = (('nome', 'novo valor001'), ('idade', '30'))
#lista03 =[['nome', 'novo valor99'], ['idade', '111']]
pessoa03.update(tupla)
print(pessoa03)
#pessoa03.update(lista03)
#print(pessoa03)

#16/07/2025
#set ----------------------------------------------------------------------------------------------------
#sets em python são mutaveis, porem aceitam apenas tipos imutaveis com valor inteiro
#set remove os valores duplicados
#não garantem ordem
#não tem indice


s1 = set() #set vazio
s1 = {'brun', 1, 2, 3}
print(s1, type(s1))

s2 = {1, 2, 3, 3, 3, 3, 3, 1, 2, 'oi', 'oi'}
print(s2)


s3 = set()
s3.add("henrique")
s3.add(1)
s3.update(('arroz', 1, 2, 3, 4)) #aqui estou enviando uma tuple pq é imutavel  ) 

#21/07/2025
#sort / lambda --------------------------------------------------------------------------------------------------------------------
#ordena minha lista

lista = [4, 32, 35, 63, 1, 7, 23, 8]
lista.sort() #ordena minha lista
print(lista)
lista.sort(reverse= True) #muda a ordem da minha lista
print(lista)

lista2 = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
def exibir(lista):
    for item in lista:
        print(item)
    print()

#crianando uma função
# def ordena(item):
#     return item['nome']
# lista2.sort(key=ordena)  #a gente passou uma fução usando o key
#exibir(lista2)

#usando a função lambda
#lista2.sort(key=lambda item: item['nome']) #isso mexe na ordem da lista
#exibir(lista2)

#usando o sorted, que cria uma copia rasa, sem alterar a lista original
l1=sorted(lista2, key=lambda item: item['nome'])
l2=sorted(lista2, key=lambda item: item['sobrenome'])
exibir(l1)
exibir(l2)

#lambda mais complexa ------------------------------------------------------------------------------------
# no lambda é essencial usar uma função antes
def executa2(funcao, *args):
    return funcao(*args)


def soma4(x, y):
    return x + y

print(
    executa2(
        lambda x, y: x + y,  #isso é como se eu criasse a função soma(x, y)
        2, 3
    ),
    executa2(soma4, 2, 3),
    soma4(2, 3),
    executa2(
        lambda *args: sum(args),
        1,2,3,4,5,6,7,8,9
    )
)



# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return numero * multiplicador
#     return multiplica
# duplica=cria_multiplicador(2)
# print(duplica(3))

duplica = executa2(
    lambda m:lambda n: n * m,
    2
)
print(duplica(3))

# empacotamento e desempacotamento de dicionarios --------------------------------------------
#args (ja vimos)
#kwargs - keyword arguments (argumentos nomeados), eles vão ser empacotados usando os **
pessoa04 = {
    'nome' : 'Pedro',
    'sobrenome' : 'Chavinho',
}

a, b = pessoa04
print(a, b)

a, b = pessoa04.values()
print(a, b)

(a1, a2), (b1, b2) = pessoa04.items()
print(a1, a2)
print(b1, b2)

for chave, valor in pessoa04.items():
    print(chave, valor)

dados_pessoa04 = {
    'idade' : 22,
    'altura' :  1.79,
}

pessoa_completa04  = {**pessoa04, 'chave' : 1, **dados_pessoa04}  #para eu extrair os valores de um dicionario eu uso '**dicionario'

print()
def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS: ', args)
    print(kwargs)
    for chave, valor in kwargs.items():
        print(chave, valor)
    print()

mostro_argumentos_nomeados(1,2,3,4, nome= 'Jo', qlq=123) # o 'nome= 'Jo', qlq=123' são kwargs
mostro_argumentos_nomeados(**pessoa_completa04)

# list comprehension python ----------------------------------------------------------------
lista = []
# for numero in range(10):
#     lista.append(numero)

lista=[numero for numero in range(10)]
print(lista)

lista = []
lista=[numero*2 for numero in range(7)]
# lista=[
#     numero*2
#     for numero in range(7)
# ]
print(lista)

#mapeamento de dados em list comprehension ------------------------------------------------------------
# eu ja tenho uma lista e eu quero gerar uma nova lista e talvez mudar os dados, mas mantendo a quantidade de itens
produtos = [
    {'nome':'p1', 'preco': 20,},
    {'nome':'p2', 'preco': 10,},
    {'nome':'p3', 'preco': 30,},
]

# novo_produtos = [
#     produto['nome']   #-----> ['preco'] ou sem nada[]
#     for produto in produtos
# ]

# novo_produtos = [
#     {'nome': produto['nome'], 'preco': produto['preco']}
#     for produto in produtos
# ]

#aqui podemos mudar o valor 
# novo_produtos = [
#     {**produto, 'preco': produto['preco'] * 1.05}
#     for produto in produtos
# ]
print('\nmapeamento de dados')
novo_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}  # esse if é usado para mapeamento, minha lista nova dever ter a mesma quantidade da minha lista antiga
    for produto in produtos
]
print(*novo_produtos, sep='\n')

#o filtro--------------------------------------------------------------------------------------------------------
# eu tenho uma lista e eu qeuro que determinada coisa não seja incruida na minha nova lista
# oque vem na esquerda do 'for' é mapeamento e o que vem na direita é filtro
import pprint
print('\nOrdena de dados')
def p(v):
    pprint.pprint(novo_produtos, sort_dicts=False, width=40)
    # sort_dicts : ele ordena as chaves  |  width ? largura da linha

lista03 = [n for n in range(10) if n < 5] # o if depois do for é o filtro
print(lista03)

# mapeamento e filtro
print('\nmapeamento e filtro')
novo_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto}  #mapeamento
    for produto in produtos
    if (produto['preco'] >= 20 and produto['preco'] *1.05) > 10  #filtro
]
p(novo_produtos)

# com mais de um for
print()
print('\ncom mais de um for')
lista04 = []
for x in range(3):
    for y in range(3):
        lista04.append((x, y))
print(lista04)

print()
print('exemplo2')
lista04 = []
lista04 = [
    (x, y)
    for x in range(2)
    for y in range(2)
]
print(lista04)

print()
print('exmoplo3')
lista04 = [
    [(x, letra) for letra in 'liv']
    for x in range(3)
]
print(lista04)