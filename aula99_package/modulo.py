
# se eu import esse modulo, mas usando o all  =  '*'  eu posso usar esse metodo __all__ para definir oque vai ser mostrado
#quando o import é '*'
#ele determina o que esta disponivel
__all__ = [
    'variavel',
    'soma_do_modulo',
]

variavel = 'alguma coisa'

def soma_do_modulo(x, y):
    return x + y

from aula99_package.modulo_b import fala_oi