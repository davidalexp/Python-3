#Faça um programa que leia um número inteiro qualquer e mostre na tela sua tabuada
n1 = int(input(' Digite um número que deseja ser tabuado: '))
#n2 = n1 * 1
#n3 = n1 * 2
#n4 = n1 * 3
#n5 = n1 * 4
#n6 = n1 * 5
#n7 = n1 * 6
#n8 = n1 * 7
#n9 = n1 * 8
#n10 = n1 * 9
#n11 = n1 * 10
print('='*30)
print('A tabuada do seu número: {}, é:'.format(n1))
print('{:10} x {:2} = {}.'.format(n1, 1, n1*1))
print('{:10} x {:2} = {}.'.format(n1, 2, n1*2))
print('{:10} x {:2} = {}.'.format(n1, 3, n1*3))
print('{:10} x {:2} = {}.'.format(n1, 4, n1*4))
print('{:10} x {:2} = {}.'.format(n1, 5, n1*5))
print('{:10} x {:2} = {}.'.format(n1, 6, n1*6))
print('{:10} x {:2} = {}.'.format(n1, 7, n1*7))
print('{:10} x {:2} = {}.'.format(n1, 8, n1*8))
print('{:10} x {:2} = {}.'.format(n1, 9, n1*9))
print('{:10} x {} = {}.'.format(n1, 10, n1*10))
print('='*30)
#print('A tabuada do seu número é: {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {} \n {}'.format(n2, n3, n4, n5, n6, n7, n8, n9, n10, n11))
#Dessa forma acima dá certo, porém não fica formatado