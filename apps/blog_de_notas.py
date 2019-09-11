'''

    Blog de notas de Luis
    --------------------
    v1.0
    ====================
    Ejercicio que puntua 3 puntos del final

'''

def escribir_nota(nota):
    f=open("notas.txt", "a")
    f.write(nota)
    f.close()


def leer_nota():
    f=open("notas.txt", "r")
    contenido =f.read()
    return contenido


def borrar_nota():
    f=open("notas.txt", "r+")
    f.truncate(0)
    print("" + '\n' + "NOTA BORRADA" + '\n')


def menu():
    while True:
        dato = input("Que desea hacer?" + '\n' + "[A]ñadir nota" + '\n' + "[V]er notas" + '\n' "[B]orrar" + '\n' + '\n' "[S]alir" + '\n'+ '\n')
        if dato == "A" or dato == "a":
            titulo = input('Titulo nota: ')
            contenido = input('Contenido nota: ')
            nota = ("------------------"+ '\n' + "Titulo: " + titulo + '\n' + "Descripcion: " '\n' + contenido + '\n'"------------------")
            print(nota)
            escribir_nota(nota)
        elif dato == "V" or dato == "v":
            print(leer_nota())
        elif dato == "B" or dato == "b":
            borrar_nota()
        elif dato == "S" or dato =="s":
            break


if __name__ == "__main__":
   menu()