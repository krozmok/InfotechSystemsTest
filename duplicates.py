import os, sys
import hashlib
 
def encontrarDuplicados(directorio):
    #Diccionario de duplicados
    dups = {}
    for dirName, subdirs, fileList in os.walk(directorio):
        for filename in fileList:
            #Obtener la ruta para el archivo
            path = os.path.join(dirName, filename)
            #Calcular el hash
            file_hash = hashfile(path)
            #Primer caso si existe una llave "file_hash" se agrega al final
            if file_hash in dups:
                dups[file_hash].append(path)
            #Segundo caso no existe la llave se crea agrega la llave y ruta
            else:
                dups[file_hash] = [path]
    return dups
 
 
# Unir diccionarios
def joinDiccs(dicc1, dicc2):
    for key in dicc2.keys():
        if key in dicc1:
            dicc1[key] = dicc1[key] + dicc2[key]
        else:
            dicc1[key] = dicc2[key]
 
#Funcion para calcular el Hash MD5 de un archivo dado y retornar el HEX Digest
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
#Imprimir resultados duplicados
def imprimirResultados(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Resultados duplicados:')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
    else:
        print('No se encontraron duplicados')
 
def DuplicatesMain():
    #Diccionario de duplicados
    dups = {}
    #Ruta principal
    folders = input("Ingrese ruta de archivo (Vacio = Ruta de Script): ")
    folders = folders.split()
    if folders == "":
        folders = '.'
    for i in folders:
        #Iterar sobre la ruta ingresada
        if os.path.exists(i):
            #Encontrar los archivos duplicados y agregarlos al diccionario de duplicados
            joinDiccs(dups, encontrarDuplicados(i))
        else:
            print('Ingrese una ruta valida. (Ejm: D:\Test)')
            sys.exit()
    imprimirResultados(dups)

if __name__ == '__main__':
        main()