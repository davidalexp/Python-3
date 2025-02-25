#desenvolva um prog. que leia as duas notas de um aluno, calcule e mostre a sua média

#Atenção à ordem de precedência e aos resultados.
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) / 2
print('A média das suas notas é: {:.1f}.'.format(m))