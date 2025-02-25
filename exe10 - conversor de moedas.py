#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos US ela pode commprar
#US$ 1 = R$3,27
d = int(input('Qual a quantia você tem em Reais? '))
u = d / 3.27
print('Com R${}, você pode comprar: US${:.2f}.'.format(d, u))
#dá para ser feito em float também