""""
conjunto = {'item1', 3, True}
print(type(conjunto))
print(conjunto)
print(len(conjunto))

tupla = (3, 7, 9, 5)
conjunto = set(tupla)
print(conjunto)
print(type(conjunto))

teste = {'item1', 'item2' 'item3'}
print(teste)
teste.add("item5")
"""
set1 = {4, 5, 6, 7, 8, 9, 1, 'item6'}
print(set1)

set.discard("item6")
set1.remove('7')
set1.pop(1)


conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 7, 6}

conjunto3 = conjunto1.union(conjunto2)
print(conjunto3)

#acha numeros repetidos
conjunto1.intersection(conjunto2)
print(conjunto1)

conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)


