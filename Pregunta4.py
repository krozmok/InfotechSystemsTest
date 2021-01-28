'''
Hacer un programa que tenga la funcion de listar las carpetas y archivos y ordenar por tamaño o fecha, y que muestre
 
si hay archivos duplicados en contenido
'''
import os

#Funcion para listar archivos de un directorio
def listar_directorio(ruta):
    for file in os.listdir(ruta):
        yield file
ruta = "."
#ruta = input("Ingrese la ruta: ")

for file in listar_directorio(ruta):
    print(file)

