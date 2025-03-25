print("Qual é o seu nome")
nome = input()
print("Olá seu nome é ")
idade = input()
print("Sua idade é")

print("seu nome é {0} e sua idade é {0} ".format(nome,idade))#{0} é a ordem variavel, exemplo nome esta primeiro entao é 0 e a idade é 1 {1}

#Terceiro jeito de fazer
nome = input()
idade = input()

print(f'Seu nome é {nome} e Sua idade é {idade}')

