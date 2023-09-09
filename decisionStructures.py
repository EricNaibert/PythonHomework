print('\n52### DECISION STRUCTURE IN PYTHON ###')

#Simple Decision Structure
first = 24;
second = 9;

if first > second:
    aux = first;
    first = second;
    second = aux;

print(f'Número em ordem crescente: ', first, second)

#Compound Decision Structure
number = int(input('\nDigite um número inteiro: '))
if number % 2 == 0:
    print(number, 'é par!')
else:
    print(number, 'é impar!')

#Complex Decision Structure
floatNumber = float(input('\nDigite um número: '))
if floatNumber > 0:
    print(floatNumber, ' é positivo!')
elif floatNumber < 0:
    print(floatNumber, ' é negativo!')
else:
    print('O Número é zero!')