#Faça um alg. que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Digite o valor do seu salário: R$ '))
p = s * (15/100)
sa = s + p
print('O seu salário com 15 por cento de aumento, vai ficar: R$ {}.'.format(sa))
#outra forma: sa = s + (s * 15 / 100)