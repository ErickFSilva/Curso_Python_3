"""
Tipos int e float.

int: Número inteiro.
O tipo int representa qualquer número positivo ou negativo.
Int sem sinal é considerado positivo.

float: Número com ponto flutuante.
O tipo float representa qualquer número positivo ou negativo com ponto flutuante.
Float sem sinal é considerado positivo.

A função(classe) type mostra o tipo que o Python inferiu ao valor.
Obs.: Tudo em python é um objeto.
"""


# Int - inteiro
print(11)
print(-11)
print(0)


# Float - flutuante
print(1.1, 10.11, sep=', ')
print(0.0, -1.5, sep=', ')


# Type - retorna tipo do valor inserido
print(type(11))
print(type('Otávio'))
print(type(11.11), type(-1.1), type(0.0))