#faça um programa que leia um ano qualquer e mostre se ele é
#BISSEXTO ou não.
ano  = int(input('\nDigite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: #se o resto da divisão for 0, ele é bissexto
    print('O ano {}, é um ano BISSEXTO.'.format(ano))
else:
    print('O ano {}, não é um ano BISSEXTO.'.format(ano))