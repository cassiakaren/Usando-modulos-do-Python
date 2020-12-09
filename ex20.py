'''o mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.'''
from random import shuffle
n1=str(input('primeiro aluno:'))
n2=str(input('segundo aluno:'))
n3=str(input('terveiro aluno:'))
n4=str(input('quarto aluno:'))
lista=[n1,n2,n3,n4]
shuffle(lista)#shuffle para embaralhar
print('A ordem de apresentação será:')
print(lista)