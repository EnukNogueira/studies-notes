# Código para adivinhar um número

palpite = 0
numero = 9

while True:
    try:
        palpite = int(input('Adivinhe qual o número correto: '))  # transforma a entrada em número inteiro
        if palpite == numero:
            print('Parabéns, você acertou!')
            break
        else:
            print('Você errou. Tente novamente.')
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")
