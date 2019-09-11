'''

    DIVIDIR

'''

def dividir(dato, dato1):
    try: 
        return dato/dato1
    except ZeroDivisionError:
        print('No se puede divir entre 0 retardado')
        return 'El valor es erroneo'
    

if __name__ == "__main__":
    try:
        dato = float(input('Num1: '))
        dato1 = float(input('Num2: '))
    except ValueError:
        print('Debes introducir Numeros')
    except NameError:
        print('Debes introducir un numero')

    print(dividir(dato, dato1))