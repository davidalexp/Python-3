#Escreva um programa que faça o computador pensar em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo pc.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
'''tive a ideia de usar o random (exercício 19 e 20, podem ajudar)'''
import random
palpite = int(input('\nQual é o seu palpite? '))
aleatorio = random.randint(0, 5)
aleatorio = int(aleatorio)

if palpite == aleatorio:
    print('Parabéns! Você acertou o número escolhido pelo computador!')
else:
    print('My bad! O computador escolheu {}, e você: {}'.format(aleatorio, palpite))