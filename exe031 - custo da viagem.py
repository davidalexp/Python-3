#faça um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200km e R$ 0,45 para viagens mais longas.
'''exercício 15 pode ajudar aqui'''
distancia = int(input('\nDigite a distância percorrida na viagem: '))
if distancia <= 200:
    print('O preço da passagem vai ser de R$ {:.2f}'.format(distancia * 0.50))
else:
    print('A passagem vai custar: {:.2f}'.format(distancia * 0.45))