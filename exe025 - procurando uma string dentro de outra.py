#Crie um programa que leia o nome de uma pessoa e
#diga se ela tem "SILVA" no nome. Mostrando True or False
import string
nome = str(input('\nDigite seu nome: ')).strip()
nomemaiusculo = nome.upper()
#procurasilva = nomemaiusculo.find('SILVA')
print('Seu nome tem "Silva"? ', 'SILVA' in nomemaiusculo)

#------------solução
'''nome = str(input('Digite o seu nome: )).strip()
print('Seu nome tem "Silva"? {}.format('silva' in nome.lower()))'''