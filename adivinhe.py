#Codigo para adivinhar um numero

palpite = 0
numero = 9

while True:  # Executamos sem verificar
    print('Adivinhe qual o numero correto: ')
    palpite = int(input()) #int transforma o input que e o texto em numero inteiro
    if palpite == numero: #verificar o codigo 
        print('Parabens voce acertou')
        break 
    else:
        print('Voce errou')
else: 
     print('Erro na aplicacao')
     print(bool(palpite))
     