#escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi
#multado. A multa vai custar R$ 7 por cada KM excedido.
'''o exercício 15 pode ajudar aqui'''
import math
velocidade = float(input('\nQual a velocidade do carro? '))
if velocidade > 80:
    print('Você será multado! A multa vai custar R$ {:.2f}'.format((velocidade - 80)*7))
else:
    print('Boa sorte! Você não será multado!')