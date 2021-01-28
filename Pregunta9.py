'''
Hacer un programa que genere un array y que imprima los numeros que no son iguales
'''
import random
#Generar Array de n números de rango a - b
def generarArray(n, a, b):
    numeros = []
    for i in range(n):
        numeros.append(random.randint(a, b))
    return numeros
#Imprimir números diferentes
def imprimirDiferentes(A):
    #Verificar para cada elemento si existe un duplicado
    print("No duplicados:", end=" ")
    for i in range(len(A)):
        duplicado = False
        for j in range(len(A)):
            if i != j and A[i]==A[j]:
                duplicado = True
                break
        if not duplicado:
            print(A[i], end=" ")

def main():
    #Array de 10 elementos con numeros entre 0 a 5
    A = generarArray(10, 0, 5)
    print("Lista {0}".format(A))
    imprimirDiferentes(A)

if __name__ == '__main__':
    main()
