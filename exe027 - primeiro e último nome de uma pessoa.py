#Faça um programa que leia o nome completo de uma pessoa
#mostrando em seguida o primeiro e o último nome separadamente

'''Ex.: Ana Maria de Souza
Primeiro = Ana
Último = Souza '''

#tem que ser automaticamente, independente da quantidade de entradas (para qualquer tamanho de str, no caso)
import string
nome = str(input('\nEscreva seu nome completo: ')).split().strip()
firstname = nome[0]
lastname = nome[-1]
print("\nSeu primeiro nome é: {} e seu último nome é: {}.".format(firstname, lastname))