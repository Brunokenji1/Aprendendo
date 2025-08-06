# from sys import path

# import aula99_package.modulo
# from aula99_package.modulo import soma_do_modulo
# from aula99_package import modulo
# from aula99_package.modulo import *

# #print(*path, sep='\n')
# print(soma_do_modulo(1, 2))  #from aula99_package.modulo import soma_do_modulo
# print(aula99_package.modulo.soma_do_modulo(12, 3))  #import aula99_package.modulo
# print(modulo.soma_do_modulo(3, 2))  #from aula99_package import modulo
# print(variavel)  #from aula99_package.modulo import *
# print(soma_do_modulo(6, 4))

# from aula99_package.modulo import fala_oi, soma_do_modulo
# fala_oi()

import aula99_package

#aula159
# print(aula99_package.duplica(3))
print(aula99_package.soma_do_modulo(2, 3))
from aula99_package import soma_do_modulo
print(soma_do_modulo(4, 5))
from aula99_package import variavel
print(variavel)
from aula99_package import fala_oi
fala_oi()