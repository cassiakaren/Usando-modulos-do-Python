'''um professor quer sortear um dos seus quatro alunos para apagar um quadro.
faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''
'''import random
nome=('paulo','gustavo','matheus','cassia')
sorteio=random.choice(nome)
print('o aluno sorteado para apagar o quadro é: {}'.format(sorteio))'''
#correção
from random import choice
n1=str(input('primeiro aluno:'))
n2=str(input('segundo aluno:'))
n3=str(input('terveiro aluno:'))
n4=str(input('quarto aluno:'))
lista=[n1,n2,n3,n4]
sorteio=choice(lista)#choice serve para nomes 
print('aluno pra apagar o quadro: {}'.format(sorteio))