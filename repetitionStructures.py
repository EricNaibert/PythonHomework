print('\n### REPETITION STRUCTURES IN PYTHON ###')

#for
for i in range(11):
    print(i, end=' ')


#for II
number = int(input('\nDigite um núero para a tabuada: '))
print('tabuada do número ', number, ':')

for j in range(1,11):
    print(number, 'x', j, ' = ', number*j)


#for III
print('\nNumero Fatorial')
number3 = int(input('Enter a number: '))
f = 1
for k in range(number3, 1,-1):
    f = f * k
print('O Fatorial de ', number3, ' é ', f)


#while
print('\nSum of the numbers: ')
i = 0
sum = 0
while i <= 10:
    print(i,end=' ')
    sum = sum+i
    i=i+1

print('\nSum: ', sum)