def mcd(num1, num2):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides.

    Args:
        num1 (int): El primer número entero.
        num2 (int): El segundo número entero.

    Returns:
        int: El MCD de los dos números enteros.
    """
    if num2 == 0:
        return num1
    else:
        while num2 != 0:
            x = num2
            num2 = num1 % num2
            num1 = x
        return num1

def mcm(num1, num2):
    """
    Calcula el minimo común multiplo (MCM) de dos números enteros utilizando la ecuacion: MCM(a,b) = (a * b) / MCD(a,b) .

    Args:
        num1 (int): El primer número entero.
        num2 (int): El segundo número entero.

    Returns:
        int: El MCM de los dos números enteros.
    """
    mdivisor = mcd(num1,num2) #Se llama a la funcion mcd para poder calcular el mcm
    mmultiplo = (num1 * num2)/mdivisor #Se realiza la siguiente operacion: MCM(a,b) = (a * b) / MCD(a,b) 
    return mmultiplo #Regresa el mcm de los dos numeros enteros ingresados


if __name__ == "__main__":
    num1=int(input("Ingrese el primer numero para hallar el mcm"))
    num2=int(input("Ingrese el segundo numero para hallar el mcm"))
    multiplo = mcm(num1,num2) #Se llama solo a la funcion mcm, que es la que se va a utilizar
    print("El mcm de: " + str(num1) + " y " +str(num2)+ " es: "  +str(multiplo))