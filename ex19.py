'''um professor quer sortear um dos seus quatro alunos para apagar um quadro.
faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.'''
import random
nome=('paulo','gustavo','matheus','cassia')
sorteio=random.choice(nome)
print('o aluno sorteado para apagar o quadro é: {}'.format(sorteio))