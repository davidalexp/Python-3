#faça um programa que leia um número real qualquer
#no teclado e mostre na tela, a sua porção inteira.
#ex.: digite: 6.127. O número: 6.127 tem a parte inteira: 6
from math import trunc
n = float(input('Digite um valor que deseja ser arredondado: '))
trunc_n = trunc (n)
print('O valor digitado de forma inteira fica: {}.'.format(trunc_n))
#--------------------------------------------------
#uma forma de fazer o código é: não importando o trunc (abaixo)
#import math
#n = float(input('...'))
#print('.....'.format(n, math.trunc(n))) 
#dessa forma, o trunc vai ficar dentro do código
#--------------------------------------------------
'''n = float(input('...'))
print('....'.format(n, int(n)))
Dessa forma o código vai puxar a parte inteira do número desejado também'''
