#Faça um programa que leia uma frase pelo teclado e
#mostre: 1) quantas vezes aparecee a letra "A";
#2) Em que posição ela aparece a primeira vez
#3) Em que posição ela aparece a última vez.
import string
frase = str(input('\nDigite uma frase: ')).upper().strip()#adicionado o upper e o strip para cortar espaços indesejados
contaa = frase.lower().count('a')
print('A letra A, aparece {} vezes na frase.'.format(contaa))
posicaoa0 = frase.find('A')
print('A primeira vez que "A" aparece, é na posição: {}'.format(posicaoa0+1))#adicionado o +1
ultimaposição = frase.lower().rfind('a')
print('A última posição da letra "A", é: {}'.format(ultimaposição))

#------------- correção
#lembrando que pode ser a forma mais simples de se fazer.
'''frase = str(input('Digite uma frase: )).upper().strip()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))'''