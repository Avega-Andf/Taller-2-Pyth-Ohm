# Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:
    #El promedio
    #La mediana
    #El promedio multiplicativo 
    #Ordenar los números de forma ascendente
    #Ordenar los números de forma descendente
    #La potencia del mayor número elevado al menor número
    #La raíz cúbica del menor número
def crearlista():
    """
    Crea una lista de cadenas de caracteres de longitud 5.

    Returns:
        list: La lista con 5 numeros flotantes.
    """
    lista = []  # inicializa una lista vacía
    for i in range(5):  # itera sobre un rango de 5 veces, ya que se pide una lista de 5
        n = float(input("Ingrese elemento para la lista"))  # solicita una cadena de caracteres al usuario
        lista.append(n)  # agrega la cadena a la lista
    return (lista)  # retorna la lista creada

def promedio(lista):
    """
    Calcula el promedio de una lista de números.

    Args:
    - lista (list): Lista de números.

    Returns:
    - promed (float): Promedio de la lista.
    """
    prom = 0   # inicializar la variable prom en cero, para no afectar la suma
    for i in range(len(lista)): # iterar por la cantidad de elementos de la lista, por cada elemento de las lista
        prom += lista[i] # agregar el valor del elemento actual a la variable prom
    promed = prom / len(lista) # calcular el promedio dividiendo la suma de los valores de la lista por la cantidad de elementos en la lista
    print("El promedio es: " + str(promed))  # Se imprime el resultado
    return promed # devolver el resultado del promedio

def mediana(lista):
    """
    Calcula la mediana de una lista de números.

    Args:
    - lista (list): Lista de números.

    Returns:
    - med (float): Mediana de la lista.
    """
    lista.sort() # ordenar la lista de menor a mayor
    n = len(lista) # obtener la cantidad de elementos en la lista
    med = lista[n//2] # obtener el elemento central de la lista (Se toma exactamente el de la mitad, porque el tamaño de la lista siempre es impar)
    print("La mediana es: " +str(med)) # Se imprime el resultado
    return med # devolver la mediana
    
def promediomultiplicativo(lista):
    """
    Calcula el promedio multiplicativo de una lista de números.

    Args:
    - lista (list): Lista de números.

    Returns:
    - promedi (float): Promedio multiplicativo de la lista.
    """
    prom = 1  # inicializar la variable prom en 1, para no afectar la multiplicacion
    for i in range(len(lista)):  # iterar sobre los elementos de la lista
        prom *= lista[i]   # multiplicar el valor del elemento actual a la variable prom
    if prom < 0: # si el producto es negativo
        z = -prom  # volvemos el valor positivo (Debido a que python arroja numeros complejos, al elevar un numero negativo a una fraccion)
        promedi = -(z** (1/len(lista))) #Se halla la raiz, y luego se vuelve negativa: ejemplo: (raiz quinta de - 32) = - (raiz quinta de 32) 
    else:  # si el producto es positivo, se halla la raiz de forma normal
        promedi = prom ** (1/len(lista))   # elevar el producto a la 1/n
    print("El promedio multiplicacitvo es: " + str(promedi)) #Imprime el resultado
    return promedi # Devuelve el valor del promedio multiplicativo
    
def ordenarmenormayor(lista):
    """
    Ordena una lista de números de menor a mayor.

    Args:
    - lista (list): Lista de números.

    Returns:
    - lista (list): Lista de números ordenada de menor a mayor.
    """
    lista.sort() # Ordena de menor a mayor
    print("Los numeros ordenados de menor a mayor: " + str(lista)) # Se imprime
    return lista
    
def ordenarmayormenor(lista):
    """
    Ordena los números en la lista de mayor a menor y los devuelve.

    Args:
    lista (list): lista de números a ordenar.

    Returns:
    list: la lista de números ordenados de mayor a menor.
    """
    lista.sort(reverse = True) # Ordena de mayor a menor
    print("Los numeros ordenados de mayor a menor: " + str(lista)) # Se imprime
    return lista
    
def potenciadelmayorelevadoalmenor(lista):
    """
    Calcula la potencia del mayor número elevado al menor número en la lista.

    Args:
    lista (list): lista de números.

    Returns:
    float: la potencia del mayor número elevado al menor número.
    """    
    potencia = max(lista) ** min(lista) #Se eleva el mayor a la potencia del menor usa max() y min()
    print("La potencia del mayor número elevado al menor número: " + str(potencia)) #Se imprime el resultado
    return potencia

def raizcubicadelmenornumero(lista):
    """
    Calcula la raíz cúbica del menor número en la lista.

    Args:
    lista (list): lista de números.

    Returns:
    float: la raíz cúbica del menor número.
    """
    if min(lista) < 0: #Si el resultado es negativo
        z = -min(lista) #se vuelve positivo
        raiz =  str(-((z) ** (1/3))) # Se halla la raiz y se pasa a negativo ejemplo: (raiz de -27) = - (raiz de 27) = (-3) = -(3)
        print("La raíz cúbica del menor número es: " + str(raiz))
    else: #Si es positivo
        raiz = min(lista) ** (1/3) #Se halla la raiz cubica del numero mas pequeño usando min()
        print("La raíz cúbica del menor número es: " + str(raiz)) #Se imprime el valor
    return raiz

if __name__ == "__main__":
    lista = crearlista() #Se llama la funcion crearlista para usar la lista
    #Se llaman todas las funciones y se imprime la lista creada
    print("La lista de numeros ingresados es: " +str(lista))
    prom = promedio(lista)
    med = mediana(lista)
    prommulti = promediomultiplicativo(lista)
    menormayor = ordenarmenormayor(lista)
    mayormenor = ordenarmayormenor(lista)
    potencia = potenciadelmayorelevadoalmenor(lista)
    raiz = raizcubicadelmenornumero(lista)