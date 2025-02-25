#Escreva um programa que converta uma temp. digitada em °C para °F
tc = float(input(' Digite uma temperatura em °C: '))
gf = tc * 1.8 + 32
print('Sua temperatura convertida para Fahrenheit é: {:.2f}.'.format(gf))
#outra forma: gf = 9 * tc / 5 + 32