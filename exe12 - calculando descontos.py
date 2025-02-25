#Faça um alg. que leia o preço de um produto e mostre seu novo preço com 5% de desconto
p = float(input(' Digite um preço: R$ '))
de = p * (5/100)
d1 = p - de
print('O valor do seu produto com 5% de desconto é: {:.2f}.'.format(d1))
#outra forma: di = preço - (preço * 5 / 100)