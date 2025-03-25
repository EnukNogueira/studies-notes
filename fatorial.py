#4! significa 4x3x2x1
numero = int(input('insira um numero: '))
fatorial = 1

if numero < 0:
    print('nao existe fatorial de numeros negativos')
elif numero == 0:
    print(f'O fatorial de {numero} e 1')
else:
    for x in range(1,numero+1):
        fatorial = fatorial*x
    print(f'o fatorial de {numero} e: {fatorial}')

