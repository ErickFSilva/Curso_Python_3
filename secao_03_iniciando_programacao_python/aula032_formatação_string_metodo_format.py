a = 'AAA'
b = 'BBB'
c = 1.1

string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

# Parâmetro nomeado. Tudo que vier após um parâmetro nomeado, precisa ser nomeado.
formato = string.format(
    # Parâmetro=Argumento
    nome1=a, 
    # Parâmetro=Argumento
    nome2=b, 
    # Parâmetro=Argumento
    nome3=c
    )

print(formato)