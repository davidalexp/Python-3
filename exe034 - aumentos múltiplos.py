#faça um programa que pergunte o salário de um funcionário e 
#calcule o valor do seu aumento. Para salários acima de R$ 1250,
#calcule um aumento de 10%. Para menores ou iguais, aumento de 15%
'''exercício 13 pode ajudar aqui'''
salario = float(input('\nDigite o salário que terá aumento: '))
if salario > 1250:
    print('O seu salário com aumento de 10% vai ser de: R$ {:.2f}'.format(salario + (salario * (10/100)))) #ordem de precedência
else:
    print('O seu salário com aumento de 15% vai ser de: R$ {:.2f}'.format(salario + (salario * (15/100))))