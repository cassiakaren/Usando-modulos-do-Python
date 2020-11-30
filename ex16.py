#crie um programa que leia um numero real qualquer pelo teclado e mostre 
#na tela a sua porção inteira
from math import floor
num=float(input('digite um numero real: '))
apbaixo=floor(num)
print('arrendondando o numero {} pra baixo, o resultado dará {}'.format(num,apbaixo))
