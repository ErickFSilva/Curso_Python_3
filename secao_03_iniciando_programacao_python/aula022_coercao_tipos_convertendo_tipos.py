# Conversão de tipos, coerção.
# Type convertion, typecasting, coercion: é o ato de converter um tipo em outro
# Tipos imutáveis e primitivos: str, int, float, bool.


print(1 + 1) # O interpretador do python soma os valores.
print('a' + 'b') # O interpretador do python concatena os valores.
# print('1' + 1) # Retornará um erro, não é possível concatenar um str com int. O python é de tipagem forte.


# Convertendo tipos
print('1', type('1'), sep=' -> ')
print(int('1'), type(int('1')), sep=' -> ')

print(int('1') + 1)
print(float('1') + 1)
print(bool('')) # String vazia é 'false'.
print(bool(' ')) # String com valor é 'true', um espaço é um valor inserido.
print(str(11) + 'b')