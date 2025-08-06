"""
https://docs.python.org/pt-br/3/library/stdtypes.html
estudando. começo depois da maratona da fatec de programação em 12/06/2025

"""

#data 12/06/2025
nome = 'xxxxxx'
sobrenome = 'mmmmmmmm'
idade = 14
ano_nascimento = 2004
maior_de_idade = 18<=2025-ano_nascimento
metro=1.77
dinheiro = 120000.4444
imc= ...  

print (nome, ano_nascimento)
print (nome, sobrenome, sep='-')
print (nome, sobrenome, end='-')
print (nome, sobrenome, end='\n')
print ('bruno\'arroz\' pedro ')
print (nome + sobrenome )  #concatenação
print (type(maior_de_idade))
print (maior_de_idade)
print (metro)
print (nome*3)

#f-strings     formatação   ------------------------------------------------------------------------
print()
print (f'Seu nome {nome} e seu sobrenome {sobrenome}'
       f'seu ano  {ano_nascimento} maior de idade? {maior_de_idade} '
    f'seu tamanho {metro:.2f} seu patrimonio {dinheiro:,.2f}')

#pode trocar uma variavel que tinha um numero int em um str   --------------------------------------
print()
ano_nascimento="11/00"
print (ano_nascimento)
divisao_inteiro=10//3  #3
exponencial = 2**3  #8

#format   ------------------------------------------------------------------------------------------
print()
a= 'Arroz'
b= 'Bola'
c= 11
d= 11.9
formato = 'a={}  b={}  c={} d={:.2f}'.format(a, b, c, d)
print( formato)
formato = 'a={1}  b={1}  c={2}  d={0}  e={3:.3f}'.format(a, b, c, d)
print( formato)
formato = 'a={x}  b={z}  c={z}  d={y}  e=  {w:.1f}'.format(w=d, x=a, y=b , z=c)
print( formato)

#input sempre retorna uma str   --------------------------------------------------------------------
print()
n1=input("numero1: ")
n2=input("numero2: ")
n1_int=int(n1)
n2_int=int(n2)
print(f'a soma = {n1+n2} string')
print(f'a soma = {n1_int+n2_int} int')

#if / else / elif   ---------------------------------------------------------------------------------
print()
entrada = input('quer entras: sim ou não: ').lower()
if entrada == 's':
    print('vc entrou')
elif entrada == 'n':
    print('vc saiu')
else:
    print('digite uma das opções')

#  falsy ->   0   0.0    ''  False
#  None
#  and   or   not
print()
print(True and True and True)
print(True and '' and True)
print(True and True and False)
print(True and 0 and False)

#13/06/2025
#formatação por intepolação  -----------------------------------------------------------------------
print()
nome = 'xxxxx'
preco = 1234.67890192
variavel= '%s, o meu nome' % nome
print(variavel)
variavel= '%s, o preço é R$%f' % (nome, preco)
print(variavel)
variavel= '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %x' % (15, 15))
print('O hexadecimal de %d é %04x' % (15, 15))
print('O hexadecimal de %d é %08X' % (15, 15))  #  o x maiusculo converte para letra maiuscula

#f-strings   ----------------------------------------------------------------------------------------
print()
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.') #preenche ate chegar o numero de caracteres que você deu e ainda da para colocar coisa dentro da aspas
print(f'{variavel: <10}')  
print(f'{variavel: ^10}oiiiii') 
print(f'{10000.1234567890:.1f}')
print(f'{22222.34567890:,.1f}')
print(f'{33333.34567890:+,.1f}') #esse + mostra o sinal da conta
print(f'{-44444.34567890:+,.1f}') 
print(f'{55555.34567890:0=+10,.1f}') 
print(f'{-66666.34567890:0=+10,.1f}') 
print(f'O hexadecimal de 1500 é {1500:08x}')
print(f'O hexadecimal de 15 é {15:04X}')
print(f'{variavel!r}')  #conversion flags -   !r   !s  !a

#fatiamento de strings   ----------------------------------------------------------------------------
print()
variavel = 'ola_mundo_disgraçado'
print(variavel[3])
print(variavel[3:6])
print(variavel[1:10:2]) # [inicio : final : passo]
print(variavel[4:]) # quando eu omito o final ele vai ate o fim
print(variavel[:7])
print(variavel[::3])
print(variavel[:-10])
print(variavel[::-1])
print(len(variavel))
print(variavel[0:len(variavel):3])
 
#OBSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS   ------------------------------------------------------
#  .isdigit()   --> vai verificar se é um numero, se for retorna True
# try except
# CONSTANTE = "Variáveis" que não vão mudar, variaveos em maiusculo
# is None     is not None
#  função startswith('')  ---> vai verificar se começa com a letra que voce colocar no parenteses

# posso quebrar linha de codigo usando a '\'   -----------------------------------------------------
print()
numero =1
if (numero == 1) and (numero !=0) and \
    (numero>0):
    print('arroz')

#string---------------------------------------------------------------------------------------------
print()
string= 'oiMundodadisgraça'
outra_string = f'{string[:3]}AAAA{string[4:]}'
print(string)
print(outra_string)
print(string.capitalize()) # capitalize retorna uma copia da string com a primeira letra em maiusculo
print(string.zfill(20))  # Ele coloca um ped, ele faz uma largura fixa aqui, colocando zeros na esquerda da string para preencher

#while  --------------------------------------------------------------------------------------------
# continue   break
print()
condicao = True
while condicao:
    nomee=input('qual o seu nome: ')
    print('seu nome é %s' % nomee)
    if nomee == 'sair':
        break
print('acabou')

#14/06/2025
#operadores de atribuição  =  +=  -=  /=  //=  **=  %= --------------------------------------------
print()
contador = 0
print(contador)
contador += 10
print(contador)
contador /= 2
print(contador)
contador //= 2
print(contador)
contador *= 5
print(contador)

#15/06/2025
# count --------------------------------------------------------------------------------------------
#conta quantas vezes tal palavra apareceu dentro do parenteses 
print()
frase = 'Oi bruno tudo certo bruno, vc é bonito bruno e joga muito bruno'
print(frase.lower().count('bruno'))
print(frase.lower().count('o'))
for i in frase:
    print (f'{i} = {frase.lower().count(i)}')

#for -----------------------------------------------------------------------------------------------
print()
novo_text = ''  #declarei primeiro
frase2 = 'arroz'
for letra in frase2:
    print(letra)
    novo_text += f'*{letra}'

print(novo_text)

#range --------------------------------------------------------------------------------------------
print()
numeros = range(10)    #qundo so tem um numero é como se fosse range(0, 10, 1)   range( inicio, fim, passo)
print(numeros)
numeros = range(5, 10)  
print(numeros)
numeros = range(2, 10, 2)  
print(numeros)
numeros = range(10, 2, -2)  
print(numeros)
numeros = range(0, -10, -2)   
print(numeros)

#16/06/2025
#lista --------------------------------------------------------------------------------------------

#  'del' tira o valor q voce escolher
# '.append()' adiciona valores ao final da lista
# '.pop()' remove o ultimo valor da lista
# '.clear()' limpa a lista
# '.inset()' ele recebe dois valores (qual o indice, qual o valor)
# metodo '.extend()' faz uma determinada ação que seria adicionar dados a lista tal, mas ela ñ retorna nada
print()
#         0     1      2      3    4
#        -5    -4     -3     -2   -1
lista = [123, True, 'Bruno', 1.2, []]
print(lista[2], type(lista[2]))
print(lista[-3], type(lista[-3]))
print(lista, type(lista))

lista2 = [10, 20, 30, 40, 'bola']
lista2.append('arroz')
numero2 = lista[2]
print(lista2[2])
lista2[2] = 1000
print(lista2[2])
print(lista2)
del lista2[1] #  'del' tira o valor q voce escolher
print(lista2)
print(lista2[1])
lista2.append(50) # '.append()' adiciona valores ao final da lista
print(lista2)
lista2.append(700)
lista2.append(800)
print(lista2)
ultimo_valor = lista2.pop()  # '.pop()' remove o ultimo valor da lista
print(lista2, 'removido', ultimo_valor)
lista2.insert(0, 5)  # '.inset()' ele recebe dois valores (qual o indice, qual o valor)
lista2.insert(0, 'oi')  
lista2.clear()  # '.clear()' limpa a lista
print(lista2)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b) # metodo '.extend()' faz uma determinada ação que seria adicionar dados a lista tal, mas ela ñ retorna nada
print(lista_a)
lista1_a = ['paula', 'marcos', 1]
lista1_b = lista1_a.copy()
lista1_a.append(500)
print(lista1_b)
print(lista1_a)

lista2_a = ['bruno', 'Breno', 'Arroz']
for nome in lista2_a:
    print(nome)

indicesssss = range(len(lista2_a))
for indice in indicesssss:
    print(indice, lista2_a[indice] )

#desempacotamento ----------------------------------------------------------------------------------------
print()
nome_1, nome_2, nome_3 = ['is', 'br', 'pe']
print(nome_1)
nome1_1, *resto = ['a', 'b', 'c', 'd', 'e']  # ---> enumerate
print(nome1_1)
print(resto)
nome1_2, *_ = ['e', 'f', 'g', 'h', 'm'] # '_' USADO PARA QUANDO VC N QUER USAR VARIAVEL

#tuple ------------------------------------------------------------------------------------------------
#tuple é imutavel
print()
nome_lista = ['arroz', 'feijão', 'carne']

nomes_tuple= 'arroz', 'feijão', 'carne'
print(nomes_tuple)
nome_lista = tuple(nome_lista)

#enumarate -------------------------------------------------------------------------------------------
#enumera iteráveis (indices)  ---> vira uma tupla
print()
nome_lista1=['pedra', 'bob', 'ano']
lista_enumerada = enumerate(nome_lista1)
for item in lista_enumerada:
    print(item)
    a,b = item  #  -->  desempacotamento
    print(a, b)

lista_enumerada = enumerate(nome_lista1)
for a, b in lista_enumerada:   #  -->  desempacotamento
    print(a, b)

lista_enumerada = list(enumerate(nome_lista1, start=19))
print(lista_enumerada)

#17/06/2025
#arredondamento -------------------------------------------------------------------------------------------
#round(variavel, a quantidade de casas dec.)arredonda o numero e retorna um ponto flutuante
print()
numero_1= 0.1
numero_2= 0.7
numero_3 = numero_1+numero_2
print(numero_3)
print(f'{numero_3:.2f}')  #  retorna uma string
print(round(numero_3, 2))  # round(variavel, a quantidade de casas dec.)arredonda o numero e retorna um ponto flutuante

import decimal
numero_1= decimal.Decimal('0.1')
numero_2= decimal.Decimal('0.7')
numero_3 = numero_1+numero_2
print(numero_3)
print(f'{numero_3:.2f}') 
print(round(numero_3, 2))

# split -----------------------------------------------------------------------------------------------------
# .split()  Ela separa a string por determinado caractere
print()
frase3 = 'Olha que coisa mais linda, mais cheia de graça' 
lista_frase = frase.split(',')   #Ela separa a string quando tiver uma ',' 
print(lista_frase)
lista_frase = frase.split()  
print(lista_frase)

#strip -----------------------------------------------------------------------------------------------------
# .strip()  tira os espaços do começo e do fim da string
# .rstrip()  tira os espaços do fim da string
# .lstrip()  tira os espaços do começo string
print()
for i, frases_1 in enumerate(lista_frase):
    print(lista_frase[1].strip())     #  .strip()  tira os espaços do começo e do fim da string
    print(lista_frase[1].rstrip())    #  .rstrip()  tira os espaços do fim da string
    print(lista_frase[1].lstrip())    #  .lstrip()  tira os espaços do começo string
print(lista_frase)

#jeito ideal de fazer é criar uma lista que voce vai poder ver o que foi alterado
# frase = '   Olha só que   , coisa interessante          '
# lista_frases_cruas = frase.split(',')

# lista_frases = []
# for i, frase in enumerate(lista_frases_cruas):
#     lista_frases.append(lista_frases_cruas[i].strip())

#join -------------------------------------------------------------------------------------------------------
#une uma string, somente strings
print()
frase_unidas = ''.join(lista_frase)   #  o separdor ''.
print(frase_unidas)
frase_unidas = '-'.join(lista_frase)   #  o separdor ''.
print(frase_unidas)
frase_unidas = ', '.join(lista_frase)
print(frase_unidas)

#lista -----------------------------------------------------------------------------------------------------
salas = [
       #0         #1     #2
    ['ricardo', 'helena', ],  #0
    ['elaine', ],             #1
    ['pedro', 'gus', 'bbds',],#2
]
print(salas[0][1])
print(salas[2][2])

# 18/06/2025
"""
Interpretador do Python

python mod.py (executa o mod)
python -u (unbuffered)
python -m mod (lib mod como script)   bibliotecas  (venv,  ...
python -c 'cmd' (comando)
python -i mod.py (interativo com mod)
"""

# desempacotamento ------------------------------------------------------------------------------------------
print()
lista_des = ['bru', 'mur', 'be', 1, 2, 3, 4, 'admir']
string18 = 'Bobao'
tupla = 'arroz', 'cuzcuz', 'feijao'
#m, l, *_ =  lista_des
for nome in lista_des:
    print(nome, end='')
print(*lista_des)
print('bru', 'mur', 'be', 1, 2, 3, 4, 'admir')
print(*string18)
print(*tupla)
print(*salas, sep='\n')

# operação ternaria (condicional de linha) --------------------------------------------------------------------
print()
# <valor> if <condição> else <outro valor>
condicao = 10 == 10
print('Valor' if condicao else 'Outro valor')
variavel02='Valor' if condicao else 'Outro valor'
print(variavel02)
print('vvvvvvvvv' if True else 'mmmmmmmmmm' if True else 'fim')
print('vvvvvvvvv' if False else 'mmmmmmmmmm' if True else 'fim')
print('vvvvvvvvv' if False else 'mmmmmmmmmm' if False else 'fim')

#19/06/2025
#replace ------------------------------------------------------------------------------------------------------------
print()
cpf= '123.456.789-90'\
.replace('.', '')\
.replace('-', '')\
.replace(' ', '')

import re
# expreção regular
cpf01 = re.sub(r'[^0-9]', '',  '512.456.789-90' )
print(cpf01)
cpf01 = re.sub(r'[^0-9]', 
               '',  
               '512adasjd356sdça123askdjla90' )
print(cpf01)
cpf01 = re.sub(r'[^0-9]', '',  '512.456.789-90' )
entrada01=input('cpf: ' )
cpf_sempontos=re.sub(r'[^0-9]',
              '',
              entrada01)