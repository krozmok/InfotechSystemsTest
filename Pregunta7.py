'''
Desarrollar una funcion que me devuelva el n-esimo fibonacci
 
Recordar que la serie fibonacci inicia en uno, es decir que fibonacci(1) = 1, ademas que
 
el fibonacci(3) = fibonacci(2) + fibonacci(1)
 
 
 
Nota: Implementarlo de modo iterativo.
'''

def fibonacci(n):
    if  n == 1 or n == 2:
        return 1
    else:
        primero = 1
        siguiente = 1
        temporal = 0
        for i in range(n-2):
            temporal = siguiente
            siguiente = primero + siguiente
            primero = temporal
    return siguiente


def main():
    n = int(input("Ingrese n: "))
    print("Fibonacchi({0}) = {1}".format(n, fibonacci(n)))

if __name__ == '__main__':
    main()