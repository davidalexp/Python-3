#O mesmo professor do desafio anterior quer sortear
#a ordem de apresentação de trabalho dos alunos.
#Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada

#fazer o mesmo código do exe19, porém mostrando a 
#ordem aleatória gerada

import random
a1 = str(input(' Digite o nome do aluno 1: '))
a2 = str(input('Digite o nome do aluno 2: '))
a3 = str(input('Digite o nome do aluno 3: '))
a4 = str(input('Digite o nome do aluno 4: '))
lista = [a1, a2, a3, a4]
escolhido = random.choice (lista)
visualização = random.sample ((lista), k=4)
print('Dentre os 4 alunos, o sorteado foi: {}. \nA ordem aleatória gerada foi: {}'.format(random.choice([a1, a2, a3, a4]), visualização))

#--------------------------------------------------
#nenhum detalhe extra para esse exercício