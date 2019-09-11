'''

    EDAD

'''


def edades(edad):
    if edad < 0:
        raise TypeError('No puedes tener menos de 0 años tonto')
    elif edad < 20:
        return 'Eres muy joven'
    elif edad < 40:
        return 'Eres joven'
    elif edad < 70:
        return 'Eres maduro'
    elif edad < 120:
        return 'Cuidate yayo'
if __name__ == "__main__":
    
    print(edades(-8))