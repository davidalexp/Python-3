#Crie um programa que leia o nome de uma cidade e
#diga se ela começa ou não com o nome "SANTO".
import string
cidade = str(input('\nDigite o nome de uma cidade: '))
primeironome = cidade[0:5].upper() == 'SANTO'
print('Sua cidade começa com "Santo"? {}'.format(primeironome))
print('Existe "Santo" no nome da sua cidade?','Santo' in cidade)
#código com detalhes do Gaunabara

#------------------ solução
'''cidade = str(input('\nEm que cidade você nasceu? ')).strip() #para tirar os espaços digitados desnecessariamente
primeironome = cidade[0:5].upper () == 'SANTO'#o 0:5 também pode ser usado e o == é para atribuição de valor
#usando o upper, obtém o resultado desejado, independentemente do que o usuário digitar, já que está forçando as maiúsculas.
print('Sua cidade {}, começa com ''Santo''? {}'.format(cidade, primeironome))
#DICA: SEMPRE PENSAR NA BESTEIRA QUE O USUÁRIO PODE FAZER.'''