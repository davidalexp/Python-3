#Faça um prog. que pergunte a quantidade de km rodados por um carro
#e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60/dia
#e R$ 0,15 km rodado.
km = float(input(' Quantos quilômetros foram rodados? '))
dias = int(input(' Quantos dias de locação? '))
locação = (km * 0.15 + dias * 60)
print('Sua locação de {:.0f} dia(s) com {} quilômetros rodados, teve o custo total de {:.2f}.'.format(dias, km, locação))
#