#tuplas
print('\n[TUPLAS]')
tupla = (1, 2, 3, 4, 5)
print(tupla)

print(tupla[1:4])

#dicionarios
print('\n[DICIONARIOS]')
produtos = {f'Lápis': 1.50,
            f'Caderno': 12,
            f'Caneta': 2.50,
            f'Borracha': 4.25 }

print(produtos)

#lists
print('\n[LISTAS]')
x = [10, 50, 25, 40]

print(x)

#emptyLists
print('\n[EMPTY LISTS]')
lista = []
lista.append(int(input('Digite um número para adicionar na lista: ')))
lista.append(int(input('Digite um número para adicionar na lista: ')))
lista.append(int(input('Digite um número para adicionar na lista: ')))

print(lista)
print(f'first number: ', lista[0])
print(f'second number: ', lista[1])
print(f'third number: ', lista[2])
