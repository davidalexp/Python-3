#Faça um programa que leia o comprimento do cateto
#oposto e do cateto adjacente de um triângulo
#retângulo, calcule o comprimento da hipotenusa
#cateto oposto é o eixo x e o adjacente é o y
from math import sqrt, ceil
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
h = (co ** 2) + (ca ** 2)
hi = h ** (1/2)
print('O valor da hipotenusa de {} e {} (com duas casas decimais arredondadas), é: {:.2f}.'.format(co, ca, hi))

#--------------------------------------------------
#outra forma de resolver (sem importações):
'''co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
h = (co ** 2 + ca ** 2) ** (1/2)'''
#--------------------------------------------------
'''from math
co = float(input('Digite o comprimento do Cateto Oposto: '))
ca = float(input('Digite o comprimento do Cateto Adjacente: '))
h = math.hypot (co, ca)'''
#nesse mesmo caso acima, pode-se tirar o math.hypot da linha 21 e colocar de importação na linha 18