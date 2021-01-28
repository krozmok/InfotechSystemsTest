'''
Escribir un codigo en python que sume y multiplique respectivamente todos los numeros de una lista, ejemplo;
 
Numeros=1 2 3 4, suma 10, multiplicacion 24.
'''
#Suma los elementos de la lista A
def suma(A):
    resultSuma = 0
    for i in A:
        resultSuma += i 
    return resultSuma
def mult(A):
    resultMult = 1
    for i in A:
        resultMult *= i
    return resultMult

def main():
    numeros_string = input("Ingrese números (ej: 1 3 4 5): ")
    numeros_list = list(map(int, numeros_string.split()))
    print("Suma: {0}".format(suma(numeros_list)))
    print("Multiplicación: {0}".format(mult(numeros_list)))

if __name__ == '__main__':
    main()