'''
Escribir un programa que tenga como input 10 numeros positivos de 3 digitos, y como output liste los que son capicuas,
 
ordenandolos de menor a mayor
'''
#Insertar x a la  lista A de manera ordenada
def insertar_ordenado(A, x):
    if A:
        #Primer caso lista con un solo elemento
        if len(A) == 1:
            if x <= A[0]:
                A.insert(0, x)
            else:
                A.append(x)
        #Segundo caso lista con más de un elemento
        else:
            for i in range(len(A)):
                if i == 0:
                    if x <= A[0]:
                        A.insert(0, x)
                        break
                else:
                    if x > A[i-1] and x <= A[i]:
                        A.insert(i, x)
                        break
                    if i == len(A)-1:
                        A.append(x)
    #Caso para la lista vacia
    else:
        A.append(x)

def main():
    numeros = input("Ingrese 10 numeros separados por espacios: ")
    numeros_list = numeros.split()
    capicuas = []
    for i in numeros_list:
        #Verificar si el número como string es igual al reves
        if i==i[::-1]:
            insertar_ordenado(capicuas, int(i))
    print("Capicuas: ", end="")
    for i in capicuas:
        print(i, end=" ")

if __name__ == '__main__':
    main()
        


