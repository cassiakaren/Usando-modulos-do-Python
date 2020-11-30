#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
#de um triangulo retangulo. calcule e mostre o comprimento da hipotenusa.
from math import hypot
coposto=float(input('Comprimento do cateto oposto: '))
cadjacente=float(input('Comprimento do cateto adjacente: '))
hi=hypot(coposto,cadjacente) #hypot calcula a hipotenusa
print('A hipotenusa vai medir:{:.2f}'.format(hi))
 #formato basico
'''co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co**2 + ca**2)**(1/2)
print('a hipotenusa vai medir:{:.2f}'.format(hi))'''
