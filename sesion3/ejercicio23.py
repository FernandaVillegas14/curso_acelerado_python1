'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion3/ejercicio23.py
Autor: ..............

'''



a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
product += a[i]*b[i]
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str
(product))