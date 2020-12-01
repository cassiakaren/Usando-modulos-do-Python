'''faça um programa que leia um angulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente desse angulo.'''
from math import cos, sin, tan
angulo=float(input('digite um angulo qualquer: '))
sen=sin(angulo)
coss=cos(angulo)
tang=tan(angulo)
print('o valor do seno é {:.2f}°, cosseno {:.2f}° e tangente {:.2f}° '.format(sen,coss,tang))