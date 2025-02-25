#o professor quer sortear um dos seus quatro alunos
#para apagar o quadro. Faça um programa que ajude ele
#lendo o nome deles e escrevendo o nome escolhido
import random
aluno1 = str(input('Nome do primeiro aluno: '))
aluno2 = str(input('Nome do segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
alunoescolhido = random.choice(lista)
print('O aluno sorteado entre os 4 nomes foi: {}'.format(alunoescolhido))
#o código acima foi corrigido com string

#--------------------------------------------------

#Não cometer o erro de fazer o código sem ver o início
#do código que o Gustavo quer
'''import random
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice (lista)
só fazer o format do "escolhido" '''