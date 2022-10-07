'''
***** Curso de programacion acelerada en python *****
Date 07-10-2022
File : sesion1/ejercicio3.py
Autor: Maria Fernanda Martine Villegas
Action: imprime capital obtenido de una inversion"


'''
import math

cantidad = float(input("Cantidad a invertir: "))
interes = float(input("interés porcentual anual:"))
años = int(input("¿Años a calcular?:"))
resultado = round(cantidad*math.pow((1+interes/100),años,) ,2)
print("Capital final: "+str(resultado))

