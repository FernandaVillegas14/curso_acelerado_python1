'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion3/ejercicio23.py
Autor: ..............

'''


persona = {}
continuar = True
while continuar:
clave = input('¿Qué dato quieres introducir? ')
valor = input(clave + ': ')
persona[clave] = valor
print(persona)
continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"