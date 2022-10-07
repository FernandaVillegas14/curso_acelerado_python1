'''
***** Curso de programacion acelerada en python *****
Date 07-10-2022
File : sesion1/ejercicio3.py
Autor: Maria Fernanda Martine Villegas
Action: Indice de masa corporal peso en kg/estatura mtrs cuadrados
'''

peso=input("¿Cual es tu peso en kg?:")
estatura = input("¿Cual es tu estatura en metros?:")
imc = round (float(peso)/float(estatura)**2,2)
print("Tu indice de masa corporal es" + str(imc))