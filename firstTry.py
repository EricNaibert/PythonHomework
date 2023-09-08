nome = input('Digite seu nome:')

try:
    idade = int(input('Digite sua idade:'))
except:
    print('Digite um número válido!')
    idade = int(input('Digite sua idade:'))

endereco = input('Digite seu endereço: ')

print(f'Nome: ', nome)
print(f'Idade: ', idade)
print(f'Endereço: ', endereco)