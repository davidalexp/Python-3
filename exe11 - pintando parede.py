#Faça um programa que leia a largura e a altura de uma parede em metros; calcule a sua área e a quantidade de tinta necessária para pintá-la
#sabendo que cada litro de tinta, pinta uma área de 2m²
#lembrar os cálculos para achar a área
l = float(input('Digite a largura: '))
a = float(input('Digite a altura: '))
h = l * a
li = h / 2
print('Para a sua parede de {}m², precisa-se de {} litros de tinta para pintá-la.'.format(h, li))

