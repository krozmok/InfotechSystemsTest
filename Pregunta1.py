#Generar un codigo en python que sume 10 numeros aleatorios de la siguiente forma: los 5 mas bajos y los 5 mas altos
import random

#Generador de n aleatorios
def generateRandom(n):
    randList = []
    for i in range (n):
        randList.append(random.randint(0,100))
    return randList
#Sumador de 5 Bajos y 5 Altos de la lista A
def addRandom(A):
    A.sort()
    n = len(A)
    altos = 0
    bajos = 0
    print("Bajos: ")
    for i in range(0,int(n/2)):
        print(A[i], end=" ")
        bajos += A[i]
    print("\nSuma bajos: ", bajos)
    print("Altos: ")
    for i in range(int(n/2),n):
        print(A[i], end=" ")
        altos += A[i]
    print("\nSuma altos: ", altos)

def main():
    A = generateRandom(10)
    print("Lista generada: {}".format(A))
    addRandom(A)
if  __name__=="__main__":
    main()