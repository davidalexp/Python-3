#Faça um programa que leia um número de 0 a 9999 e
#mostre na tela cada um dos dígitos separados
'''Ex.: Digite um número: 1834
Unidade: 4
Dezenas: 3
Centenas: 8
Milhar: 1

pode tentar fazer na forma matemática ou str'''
'''import string
número = int(input('Digite um número de 0 até 9999: ')) #resolução guanabara
limite = str(input([:9999])) #usei o raciocínio quase igual; a partir da linha 18, será meu código com o do Guanabara
print('Analisando o número: {}, temos: '.format(limite))
print('Unidade (s): {}, '.format(limite.find('0001, 0002, 0003, 0004, 0005, 0006, 0007, 0008, 0009', [0, 5])))
print('Dezena (s): {}'.format())
print('Centena (s): {}'.format())
print('Milhar (es): {}'.format())'''

'''import string
número = int(input('\nDigite um número de 0 até 9999: '))
n = str(número)
#refaz os prints que tinha feito
print('Analisando o número: {}, temos: '.format(número))
#importante listar as casas de string que os números estão (0 a 3)
print('Unidade (s): {},'.format(n[3]))
print('Dezena (s): {},'.format(n[2]))
print('Centena (s): {},'.format(n[1]))
print('Milhar (es): {}.'.format(n[0]))'''
#Dessa forma a string vai pegar cada uma das 4 casas e trabalhar nelas, mas um número de 3 dígitos apresentará erro

import string
número = int(input('\nDigite um número de 0 até 9999: '))
#refaz os prints que tinha feito
print('Analisando o número: {}, temos: '.format(número))
#para essa solução, será feito o cálculo de cada casa do algarísmo para a conversão desejada.
u = número // 1 % 10 #cada cálculo será feito de acordo com sua unidade.
d = número // 10 % 10
c = número // 100 % 10
m = número // 1000 % 10
print('Unidade (s): {},'.format(u))
print('Dezena (s): {},'.format(d))
print('Centena (s): {},'.format(c))
print('Milhar (es): {}.'.format(m))