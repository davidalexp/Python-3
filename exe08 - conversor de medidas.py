#escreva um prog. que leia um valor em metros e o exiba convertido em Cm e MM.
n1 = float(input(' Digite um valor em metros: '))
n2 = n1 / 1000
n3 = n1 / 100
n4 = n1 / 10
n5 = n1 * 1
n6 = n1 * 10
n7 = n1 * 100
n8 = n1 * 1000

print('O tamanho digitado, corresponde à: {}km (quilômetro(s)), \n{:.3f}hm (hectômetro(s)), \n{}dam (decâmetro(s)), \n{}m (metro(s)), \n{:.2f}dm (decímetro(s)), \n{:.2f}cm (centímetros) e \n{:.2f}mm (milímetros).'.format(n2, n3, n4, n5, n6, n7, n8))