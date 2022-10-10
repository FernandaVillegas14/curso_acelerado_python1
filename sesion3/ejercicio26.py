'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion3/ejercicio23.py
Autor: ..............

'''


monedas = {'Euro':'€', 'Dollar':'$', 'peso':'MXN'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")