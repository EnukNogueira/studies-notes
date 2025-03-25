#bloco externo
nome = "Enuk" #variavel global

def minha_funcao():
    #bloco interno *bloco interno de uma funcao é conhecido como corpo da funcao
    nome = 'NUNUK'
    tupla = 2, 5, 6, 7
    print(nome)
    print(tupla)
    if nome == 'Enola':
        print('impressao do bloco interno da condicao if')
    for x in  tupla: 
        print(x)

print(nome)
minha_funcao()



lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop() #esta retornando ou removendo o ultimo item. RETORNANDO
var1= print('ola mundo')
print(lista)
print('RETORNO DA FUNCAO POP', retorno)
print('retorno da funcao print:', var1)

def ola_mundo():
    return 'ola mundo'
    print('ola mundo')
retorno= ola_mundo()
print(retorno)

def par_impar():
    numero = 23
    if(numero % 2) == 0:
        return "numero par"
    return "numero impar"
print(par_impar())



