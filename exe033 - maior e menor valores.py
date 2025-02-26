#faça um programa que leia 3 números e mostre qual é o maior e
#qual é o menor
n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('\nDigite o segundo número: '))
n3 = int(input('\nDigite o terceiro número: '))
if n1 > n2 and n1 > n3:
    print('O maior número digitado foi: {}.'.format(n1))
else:
    if n2 > n1 and n2 > n3:
        print('O maior número digitado foi: {}.'.format(n2))
    else:
        print('O maior número digitado foi: {}.'.format(n3)) #se n3 for maior que n1 e n2, ele imprime n3
if n1 < n2 and n1 < n3:
    print('O menor número digitado foi: {}.'.format(n1))
else:
    if n2 < n1 and n2 < n3:
        print('O menor número digitado foi: {}.'.format(n2))
    else:
        print('O menor número digitado foi: {}.'.format(n3)) #se n3 for menor que n1 e n2, imprime n3
        
