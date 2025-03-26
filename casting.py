# Faz a conversão de int, float e strings.

# Conversão para int
x = int(2)       # converte o número 2 para inteiro
y = int(2.8)     # converte o número 2.8 para inteiro, truncando a parte decimal
z = int('2')     # converte a string '2' para inteiro

print(x, y, z)   # imprime os valores convertidos para inteiros

# Conversão para float
a = float(2)     # converte o número 2 para float
b = float(2.8)   # mantém o número 2.8 como float
c = float('2')   # converte a string '2' para float

print(a, b, c)   # imprime os valores convertidos para float

# Conversão para string
d = str(2)       # converte o número 2 para string
e = str(2.8)     # converte o número 2.8 para string
f = str('s1')    # mantém a string 's1' como string

print("a variável d é do tipo: ", type(d))
print("a variável e é do tipo: ", type(e))
print("a variável f é do tipo: ", type(f))
