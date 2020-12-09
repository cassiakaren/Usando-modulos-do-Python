#crie um programa que leia um numero real qualquer pelo teclado e mostre 
#na tela a sua porção inteira
from math import trunc
num=float(input('digite um numero real: '))
apbaixo=trunc(num)#funçao trunc deixa o numero real, inteiro
print('o valor digitado foi {} e sua porçao inteira é: {}'.format(num,apbaixo))
