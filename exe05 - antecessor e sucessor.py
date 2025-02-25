#Faça um programa que leia um número inteiro e mostre na tela
#seu sucessor e seu antecessor
#ex.: leia um valor e seu antecessor é x e seu sucessor é y.
n1 = int(input('Digite um número: '))
a = n1 - 1
s = n1 + 1
print('O Antecessor de {} é: {} e o seu Sucessor é: {}.'.format(n1, a, s))
#outra forma de fazer é a abaixo:
#.format(n1, (n1-1), (n1+1)))
#dessa segunda forma, economiza mais memória porque usa-se menos variáveis