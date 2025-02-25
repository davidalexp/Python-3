#Faça um programa que leia um ângulo qualquer e mostre na tela
#o valor do seno, cosseno e tangente desse angulo
#eixo vertical: senos; horizontal: cossenos
import math
a = float(input('Digite o ângulo desejado: '))
r = math.radians(a)
tan = math.tan(r)
sen = math.sin(r)
cos = math.cos(r)
print('O valor da Tangente do ângulo: {} é: {:.2f}tan, \n do Seno é: {:.2f}sen,\n e do Cosseno é: {:.2f}cos.'.format(a, tan, sen, cos))

#--------------------------------------------------
#quando houver a dificuldade no código, importante sempre
#consultar o manual em: python.org
#outra forma de se fazer:
'''from math import radians, sin, cos, tan
angulo = float(input('...'))
seno = sin(radians(angulo))
cos = cos(radians(angulo))
tangegnte = tan(radians(angulo))
print('....')'''