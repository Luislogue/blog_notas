'''

Comprehension
----------------------
Constructos que permiten generar una secuencia a partir de otra secuencia

'''
# usuario inserta casa=> string('casa')
# comprehension => ['c', 'a', 's', 'a']

cadena = input('escribe algo: ')

Comprehension = [i for i in cadena]

print(Comprehension)