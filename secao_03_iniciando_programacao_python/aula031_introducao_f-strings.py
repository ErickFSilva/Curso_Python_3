nome = 'Luiz Otávio'
altura = 1.80
peso = 95
imc = peso / altura ** 2


print('f-strings')

# Formatação de strings: f-strings
linha_1 = f'{nome} tem {altura:.2f} de altura'
print(linha_1)

linha_2 = f'Pesa {peso} quilos e seu IMC é {imc:.1f}'
print(linha_2)
