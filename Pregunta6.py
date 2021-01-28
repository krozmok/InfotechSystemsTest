'''
Crear una funcion que determine si dado una serie de parentesis, estas se encuentran en pares, es decir,
 
abierto '(' y cerrado ')'.
 
Ejm:
 
 Entrada: '(()()())()()(())'
 
 Salida: True
 
 
 
 Entrada: '(()('
 
 Salida: False

'''

class Pila:
    
    def __init__(self):
        self.items = []
    
    def cima(self):
        if self.items:
            return self.items[len(self.items)-1]
        else:
            return ""
    def apilar(self, x):
        self.items.append(x)

    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila esta vacia")
    def es_vacia(self):
        return self.items == []

def main():
    parentesis = input("Entrada: ")
    #Caso cadena de string empieza con parentesis de cerradura )
    if parentesis[0] == ')':
        print(False)
        return
    #Caso continua si el primer parentesis es de apertura (
    pila = Pila()
    for i in parentesis:
        if i == "(":
            pila.apilar("(")
        else:
            pila.desapilar()
    print(pila.es_vacia())

if __name__ == '__main__':
    main()