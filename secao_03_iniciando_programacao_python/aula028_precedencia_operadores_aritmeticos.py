# Precedência de operadores:
#   1. (n + n) -> Parenteses
#   2. ** -> Exponenciação
#   3. * -> Multiplicação
#   4. / -> Divisão
#   5. // -> Divisão inteira
#   6. % -> Módulo
#   7. + -> Soma
#   8. - -> Subtração


conta_1 = 1 + 1 ** 5 + 5
print(conta_1)

conta_1 = "Qualquer coisa"
print(conta_1)

conta_1 = (1 + int(0.5 + 0.5)) ** (5 + 5)
print(conta_1)