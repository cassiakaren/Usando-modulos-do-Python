'''faça um programa que leia um angulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente desse angulo.'''
from math import radians, cos, sin, tan
angulo=float(input('digite um angulo qualquer: '))
sen=sin(radians(angulo))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo,sen))
coss=cos(radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo,coss))
tang=tan(radians(angulo))
print('o angulo de {} tem a tangente de {:.2f}'.format(angulo,tang))

