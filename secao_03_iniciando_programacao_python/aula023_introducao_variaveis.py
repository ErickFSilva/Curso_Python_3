# Variáveis são usadas para salvar algo na memória do computador.
# PEP8: Inicie variáveis com letras minúsculas podendo acrescentar números e underline (_) após o início.
# O sinal de '=' é o operador de atribuição. Ele é usado para atribuir um valor a um nome (uma variável).
# Uso: nome_variavel = expressao.
# Os nomes das variáveis precisam expressar os seus propósitos.


# Variáveis
nome_completo = 'Luiz Otávio Miranda'
print(nome_completo)

soma_dois_mais_dois = 2 + 2
print(soma_dois_mais_dois)

print(int('1'), type(int('1')))
int_um = int('1')
print(int_um, type(int_um))

int_dois = bool('2') # nome da variável que não condiz com a expressão recebida
print(int_dois, type(int_dois))

nome = 'Luiz'
idade = 30
maior_de_idade = idade >= 18
print('Nome: ', nome, ', Idade: ', idade, sep='')
print('É maior?', maior_de_idade)