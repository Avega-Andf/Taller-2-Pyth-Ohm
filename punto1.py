# Desarrollar un programa que ingrese un número entero"n" y separe todos los digitos que componen el número.
def digitos(num):
    """
    Función que recibe un número entero y devuelve una lista con cada uno de sus dígitos separados.

    Args:
    num (int): El número entero a separar en dígitos.

    Returns:
    list: Una lista con los dígitos del número.
    """
    numstr = str(num) #Volvemos el numero ingresado en una cadena de caracteres por medio del str()
    digitos = [] #Se crea una lista vacia en donde se ingresaran los digitos del numero ingresado
    for i in numstr:
        digitos.append(int(i)) #Por un ciclo for por cada caracter "i" del numero, se agregara a la lista
    return digitos 

if __name__ == "__main__":
    num= int(input("Ingrese un numero entero: ")) 
    dig = digitos(num) #Se llama a la funcion digitos
    print("Los digitos separados del numero " +str(num) + " son: " +str(dig)) #Se imprime el numero que se ingreso, junto a una lista con sus digitos separados





