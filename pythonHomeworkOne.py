print('\n### Numbers List ###')

lista = []
sum = 0;

while True:

    try:
        numbers = int(input('Enter a number: '))
        if numbers >= 0:
            lista.append(numbers)
        else:
            break

    except:
        print('Please, enter a valid number!\n')



for i in lista:
    sum = sum + i

print('\nList: ', lista)
print('Sum: ', sum)

    
    

