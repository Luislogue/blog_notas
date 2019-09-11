'''

RAIZ CUADRADA

'''
import os
import math

def cuadrada(dato):
    if dato < 0:
        raise ValueError('El numero no puede ser negativo')
    else:
        return math.sqrt(dato)


if __name__ == "__main__":
    dato = float(input('Introduce un numero: '))
    try:
        print(cuadrada(dato))
    except ValueError as NumeroInvalido:
        print(NumeroInvalido) 
        
    print('programa terminado')