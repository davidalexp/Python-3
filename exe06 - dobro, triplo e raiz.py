#crie um alg. que leia um número e mostre o seu
#dobro, triplo e raíz quadrada.
n = int(input('Digite um valor: '))
n1 = n * 2
n2 = n * 3
n3 = n ** (1/2)
print('O dobro do valor de: {}, é: {}; o seu triplo é: {} e a sua raíz quadrada é: {:.3f}'.format(n, n1, n2, n3))
#outra resolução é:
#.format((n, (n*2), (n*3), (n**(1/2))))
