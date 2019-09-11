'''

Recursiva

'''

def recursive(intento = 1):
    respuesta = input('De que color es una naranja: ')
    if respuesta != 'naranja':
        if intento < 3:
            print('\n Fallaste retardo, prueba otra vez')
            intento += 1
            recursive(intento)
        else:
            print('\n Perdiste')
    else:
        print('\nGanaste')

if __name__ == "__main__":
    recursive()