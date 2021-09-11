import ast

f = open("Diccionario.txt", "a")
f.close()

f = open("Diccionario.txt", "r")
contenido = f.read()

if len(contenido) == 0:
    diccionario = dict(contenido)
    print(diccionario)
else:
    diccionario = ast.literal_eval(contenido)
    print(diccionario)
f.close()

f = open("Diccionario.txt", "w")
clave = input ("Ingrese una clave:\n")
valor = input ("Ingrese un valor:\n")
diccionario.update({clave:valor})
f.write(str(diccionario))
f.close()

f = open("Diccionario.txt", "r")
print(diccionario)
f.close()