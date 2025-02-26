#faça um programa que leia o comprimento de 3 retas e diga ao
#usuário se elas podem ou não fazer um triângulo
import math
reta1 = int(input('\nDigite o comprimento da primeira reta: '))
reta2 = int(input('\nDigite o comprimento da segunda reta: '))
reta3 = int(input('\nDigite o comprimento da terceira reta: '))
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    #se o comprimento da reta 1 for menor que a soma das retas 2 e 3,
    #e o comprimento da reta 2 for menor que a soma das retas 1 e 3, e o comprimento da reta 3 for menor que a soma das retas 1 e 2
    print('As retas {}, {}, e {} podem formar um triângulo.'.format(reta1, reta2, reta3))
else:
    print('As retas {}, {}, e {} não podem formar um triângulo.'.format(reta1, reta2, reta3))
