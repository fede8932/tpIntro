from principal import *
from configuracion import *
import random
import math

#lee el archivo y carga en la lista diccionario todas las palabras
def lectura(diccionario):
    archivo = "./lemario.txt"  # Ruta del archivo de texto en el directorio raíz
    with open(archivo, 'r', encoding='latin-1') as file:
        for linea in file:
            palabra = linea.strip()  # Eliminar espacios en blanco al inicio y final de la línea
            diccionario.append(palabra)
    return diccionario

#Devuelve una cadena de 7 caracteres sin repetir con 2 o 3 vocales y a lo sumo
# con una consonante dificil (kxyz)
def dame7Letras():
    vocales = 'aeiou'
    consonantes_dificiles = 'kxyz'
    cadena = ''

    # Generar 2 o 3 vocales
    num_vocales = random.randint(2, 3)
    for _ in range(num_vocales):
        vocal = random.choice(vocales)
        cadena += vocal

    # Generar consonante difícil (si es posible)
    num_consonantes_dificiles = random.randint(0, 1)
    for _ in range(num_consonantes_dificiles):
        consonante_dificil = random.choice(consonantes_dificiles)
        cadena += consonante_dificil

    # Generar el resto de caracteres
    num_caracteres_restantes = 7 - len(cadena)
    caracteres_restantes = 'abcdefghijlmnopqrstuvw'
    caracteres_restantes = ''.join(set(caracteres_restantes) - set(vocales) - set(consonantes_dificiles))
    for _ in range(num_caracteres_restantes):
        caracter = random.choice(caracteres_restantes)
        cadena += caracter

    # Mezclar los caracteres
    cadena = ''.join(random.sample(cadena, len(cadena)))

    return cadena

def dameLetra(letrasEnPantalla):
    letra = random.choice(letrasEnPantalla)
    return letra

#si es valida la palabra devuelve puntos sino resta.
def procesar(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    if esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
        return Puntos(candidata)
    else:
        return -1

#chequea que se use la letra principal, solo use letras de la pantalla y
#exista en el diccionario
def esValida(letraPrincipal, letrasEnPantalla, candidata, diccionario):
    # comprueba que letraPrincipal esté en la palabra candidata, que candidata se pueda formar con las letras de letrasEnPantalla y que esté en el diccionario
    if letraPrincipal in candidata and all(letra in letrasEnPantalla for letra in candidata) and candidata in diccionario:
        return True
    return False

#devuelve los puntos
def Puntos(candidata):
    longitud=len(candidata)
    if longitud==3:
        return 1
    elif longitud==4:
        return 2
    elif longitud ==5:
        return 5
    elif longitud==6:
        return 6
    elif longitud==7:
        return 10

#busca en el diccionario paralabras correctas y devuelve una lista de estas
def dameAlgunasCorrectas(letraPrincipal, letrasEnPantalla, diccionario):
    combinaciones_correctas = []
    for palabra in diccionario:
        if all(letra in letrasEnPantalla for letra in palabra) and letraPrincipal in palabra:
            combinaciones_correctas.append(palabra)
    print("palabras", combinaciones_correctas)
    return combinaciones_correctas