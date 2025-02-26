#crie um programa que leia um número inteiro e mostre na tela se ele é
#PAR ou ÍMPAR
numero = int(input('\nDigite um número: '))
if numero % 2 == 0: #se o resto da divisão for 0, ele é par
    print('O número {}, é PAR.'.format(numero))
else:
    print('O número {}, é ÍMPAR.'.format(numero))