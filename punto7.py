def crearlista(e):
    """
    Crea una lista de cadenas de caracteres de longitud e.

    Args:
        e (int): La cantidad de elementos que tendrá la lista.

    Returns:
        list: La lista de cadenas de caracteres.
    """
    lista = []  # inicializa una lista vacía
    for i in range(e):  # itera sobre un rango de e veces
        n = str(input("Ingrese elemento para la lista"))  # solicita una cadena de caracteres al usuario
        lista.append(n)  # agrega la cadena a la lista
    return lista  # retorna la lista creada


def vocales(lista):
    """
    Verifica si en la lista existe una cadena de caracteres que contiene dos o más vocales.
    Si se encuentra una cadena de este tipo, imprime la cadena y retorna True.
    Si no existe ninguna cadena con dos o más vocales, imprime un mensaje y retorna False.

    Args:
        lista (list): La lista de cadenas de caracteres.

    Returns:
        bool: True si existe una cadena con dos o más vocales, False en caso contrario.
    """
    encontrado = False  # inicializa una variable booleana en False
    for i in lista:  # itera sobre cada cadena de caracteres en la lista
        contador_vocales = 0  # inicializa un contador de vocales en 0
        for letra in i:  # itera sobre cada letra en la cadena de caracteres
            if letra in ['a', 'A', 'á', 'Á', 'é', 'É', 'e', 'E', 'i', 'I', 'í', 'Í', 'o', 'O', 'ó', 'Ó', 'u', 'U', 'ú', 'Ú']:  # verifica si la letra es una vocal
                contador_vocales += 1  # incrementa el contador de vocales
                if contador_vocales >= 2:  # si el contador de vocales es mayor o igual a 2, significa que la cadena tiene 2 o más vocales
                    print("La palabra '" + str(i) + "' de la lista contiene dos o mas vocales")  # imprime la cadena que contiene 2 o más vocales
                    encontrado = True  # cambia la variable booleana a True
                    break  # detiene la iteración
    if encontrado == False:  # si la variable booleana sigue siendo False, significa que no se encontró ninguna cadena con 2 o más vocales
        print("No existe una palabra en la lista con dos o mas vocales.")  # imprime el mensaje correspondiente
    return encontrado  # retorna la variable booleana


if __name__ == "__main__":
    e = int(input("Ingrese el tamaño de la lista: "))  # solicita al usuario el tamaño de la lista
    lista = crearlista(e)  # crea una lista de cadenas de caracteres de longitud e
    print("La lista ingresada: ", lista)  # imprime la lista ingresada por el usuario
    vocal = vocales(lista)  # verifica si hay una cadena con dos o más vocales en la lista y retorna True o False