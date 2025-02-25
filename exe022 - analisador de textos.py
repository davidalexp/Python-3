#crie um programa que leia o nome completo de uma pessoa
#e mostre: 1) o nome com todas as letras maiúsculas
#2) com todas minúsculas
#3) quantas letras ao todo (sem contar os espaços)
#4) quantas letras tem o primeiro nome
import string
nome = str(input('\n Digite seu nome completo: '))
maiúsculas = str.upper(nome)
minúsculas = str.lower(nome)
quantidadeletras = len(nome.strip()) - nome.count(" ")
nomecortado = nome.split()[0]
quantidadeprimeiro = len(nomecortado)
print('\n Analisando seu nome...')
print('\n Seu nome em caixa alta: {} '.format(maiúsculas))
print('\n Seu nome em minúsculas: {}'.format(minúsculas))
print('\n Seu nome tem {} letras '.format(quantidadeletras))
print('\n Seu primeiro nome é: {}'.format(nomecortado))
print('\n E, {} tem {} letras.'.format(nomecortado, quantidadeprimeiro))

#--------------------------------------- Solução do Guanabara
'''
nome = str(input('\n Digite seu nome completo: '))
print('\n Analisando seu nome...')
print('\n Seu nome em caixa alta: {} '.format(nome.upper()))
print('\n Seu nome em minúsculas: {}'.format(nome.lower()))
print('\n Seu nome tem {} letras '.format(len(nome)-nome.count(' ')))
print('\n Seu primeiro nome tem {} letras.'.format(nome.find(' '))) #outra forma de fazer a mesma coisa da linha de cima

--------Dessa forma, o exercício já pode ser finalizado

separa = nome.split()
print('\n Seu primeiro nome tem {} letras.'.format(separa[0], len(separa[0])))

-------- formas mais práticas de resolver o exercício
''' 