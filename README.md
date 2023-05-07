# TALLER 2, Hecho por.. PYTH-OHM :D
#### Integrantes:
##### Tomas Santiago Forero Duarte
##### Andrés David Ortiz Rivas
##### Andrés Felipe Vega Bermeo
# 
#### Logo de pyth - Ohm:
[![c67e2c4b-33f7-417f-94a8-1adc607ac09f.jpg](https://i.postimg.cc/bvbvZzwZ/c67e2c4b-33f7-417f-94a8-1adc607ac09f.jpg)](https://postimg.cc/GBLRNnYR)
#
### 1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.
<details><summary>codigo</summary><p>

``` python
def digitos(num):
    #Función que recibe un número entero y devuelve una lista con cada uno de sus dígitos separados.
    """
    #Args:
    #num (int): El número entero a separar en dígitos.

    #Returns:
    #list: Una lista con los dígitos del número.
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
```
</p></details></br>


  + Para este codigo, el numero ingresado se vuelven una cadena de caracteres, y por cada caracter del numero, se ingresa a una lista, teniendo asi una la lista de los digitos separados por comas del numero 

### 2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.

<details><summary>codigo</summary><p>

``` python
def listaentera(numero):
    """
    Función que recibe un número y devuelve una lista con cada uno de sus dígitos enteros.

    Args:
    numero (float): El número real a separar en dígitos enteros.

    Returns:
    list: Una lista con los dígitos enteros del número.
    """
    numerostr = str(int(numero))  # Se convierte el número en un entero y luego en una cadena de caracteres
    parteentera = []  # Se crea una lista vacía para almacenar los dígitos enteros del número
    for i in numerostr:  # Se recorre la cadena de caracteres
        parteentera.append(int(i))  # Se convierte cada carácter en un entero y se agrega a la lista
    return parteentera  # Se retorna la lista de dígitos enteros del número


def listadecimal(x):
    """
    Función que recibe un número real y devuelve una lista con cada uno de sus dígitos decimales.

    Args:
    x (float): El número real a separar en dígitos decimales.

    Returns:
    list: Una lista con los dígitos decimales del número.
    """
    entero = int(x)  # Se obtiene la parte entera del número
    decimal = x - entero  # Se obtiene la parte decimal del número
    partedecimal = []  # Se crea una lista vacía para almacenar los dígitos decimales del número
    for i in range(10):  # Se itera 10 veces para obtener hasta 10 dígitos decimales
        decimal *= 10  # Se multiplica la parte decimal por 10
        digito = int(decimal)  # Se obtiene el primer dígito decimal
        partedecimal.append(digito)  # Se agrega el dígito decimal a la lista
        decimal -= digito  # Se resta el dígito decimal obtenido a la parte decimal y se repite el proceso
    return partedecimal  # Se retorna la lista de dígitos decimales del número


if __name__ == "__main__":
    numero = float(input("Ingrese el número decimal: "))  # Se solicita al usuario que ingrese un número real
    digitosenteros = listaentera(numero)  # Se llama a la función listaentera para obtener la lista de dígitos enteros del número
    digitosdecimales = listadecimal(numero)  # Se llama a la función listadecimal para obtener la lista de dígitos decimales del número
    print("Numero ingresado: " + str(numero))
    print("Parte entera: " + str(digitosenteros))  # Se imprime la lista de dígitos enteros del número
    print("Parte decimal: " + str(digitosdecimales))  # Se imprime la lista de dígitos decimales del número
```
</p></details></br>
+ En este codigo se establece un limete de 10 decimales despues del punto:
+ La función listaentera recibe un número y devuelve una lista con cada uno de sus dígitos enteros. Primero convierte el número en un entero y luego en una cadena de caracteres. Luego crea una lista vacía para almacenar los dígitos enteros y recorre la cadena de caracteres, convirtiendo cada carácter en un entero y agregándolo a la lista. Finalmente, retorna la lista de dígitos enteros del número.
+ La función listadecimal recibe un número real y devuelve una lista con cada uno de sus dígitos decimales. Primero obtiene la parte entera del número y luego la parte decimal. Luego, crea una lista vacía para almacenar los dígitos decimales y itera 10 veces para obtener hasta 10 dígitos decimales. En cada iteración, multiplica la parte decimal por 10, obtiene el primer dígito decimal, lo agrega a la lista, resta el dígito decimal obtenido a la parte decimal y repite el proceso. Finalmente, retorna la lista de dígitos decimales del número.
+ En el bloque if __name__ == "__main__":, se solicita al usuario que ingrese un número real, se llama a la función listaentera para obtener la lista de dígitos enteros del número, se llama a la función listadecimal para obtener la lista de dígitos decimales del número, se imprimer el numero original y se imprime cada lista.

### 3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos.
<details><summary>codigo</summary><p>

``` python
def iguales(num1:int,num2:int) -> str:
  """
  Comprueba si dos números enteros 'num1' y 'num2' son espejos.

  Args:
    num1 (int): El primer número entero.
    num2 (int): El segundo número entero.

  Returns:
    str: Un mensaje indicando si los números son espejos o no.
  """
  snum1 = str(num1) #convierte el primer número ingresado en una cadena de caracteres.
  snum2 = str(num2) #convierte el segundo número ingresado en una cadena de caracteres.
  if snum1 == snum2[::-1]: #La instrucción snum2[::-1] invierte la cadena de caracteres snum2
    mensaje = "Los numeros " + str(num1) + " y " + str(num2) + " son numeros espejos"
  else:
    mensaje = "Los numeros " + str(num1) + " y " + str(num2) + " NO son numeros espejos"
  return mensaje

def cuadradosespejos(num1:int,num2:int) -> bool:
  """
  Comprueba si los cuadrados de dos números enteros son espejos.

  Args:
    num1 (int): El primer número entero.
    num2 (int): El segundo número entero.

  Returns:
    bool: True si los cuadrados de los números son espejos, False en caso contrario.
  """
  acuadrado = num1 ** 2 
  bcuadrado = num2 ** 2
  stra = str(acuadrado) #convierte el cuadrado del primer número ingresado en una cadena de caracteres.
  strb = str(bcuadrado) #convierte el cuadrado del segundo número ingresado en una cadena de caracteres.
  espejo = iguales(num1,num2)
  if stra == strb[::-1]: #Verifica si los cuadrados son espejos.
    print(espejo)
    return True
    #Si los cuadrados son espejos, la función imprime el mensaje de que los números son espejos, llamando a la función iguales().
  else:
    print("Los numeros " + str(num1) + " y " + str(num2) + " NO son numeros espejos")
    return False
    #Si los cuadrados no son espejos, la función imprime un mensaje de que los números no son espejos y devuelve False.
  
if __name__ == "__main__": # se pide al usuario que ingrese dos números enteros y se llama a la función cuadradosespejos().
    num1 = int(input("Ingrese un numero entero: "))
    num2 = int(input("Ingrese un segundo numero entero: "))
    cuadradosespejos(num1, num2)

```
</p></details></br>

+ Para este codigo se uso la siguiente definicion de numeros espejos:
+ Un número y su cuadrado que al ser invertido en su representación decimal, es decir, leerlo de derecha a izquierda en lugar de izquierda a derecha, resulta en un número y su cuadrado iguales a los originales. 
+ Ejemplos de numeros espejos para el codigo:
$$12^2 = 144$$ 
$$21^2 = 441$$
$$13^2 = 169$$ 
$$31^2 = 961$$
$$1012^2 = 1024144$$
$$2101^2 = 4414201$$
+ Ejemplos de NO numeros espejos segun el codigo:
$$14^2 = 196$$ 
$$41^2 = 1681$$

El codigo primero verifica que el numero 1 y el numero 2 sean espejos, y luego que sus cuadrados sean espejos, despues de que esas dos afirmaciones sean verdaderas, se imprimira que numero 1 y numero 2 son numeros espejos.

### 4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.
<details><summary>codigo</summary><p>

``` python
import math
def factorial(x:int):
    """
    Calcula el factorial de un número entero.

    Args:
        x: Un número entero positivo.

    Returns:
        El factorial de x.
    """
    fact = 1 #Comienza en 1 para no afectar el valor del producto
    for i in range(1, x+1): # Factorial: Se multiplican los valores desde 0 hasta la cantidad x, elegida
        fact *= i
    return fact #Regresa el valor del factorial

def cosaprox(x:int, n:int):
    """
    Calcula una aproximación del coseno de x mediante la serie de Taylor.

    Args:
        x: Un número real.
        n: La cantidad de términos de la serie de Taylor a utilizar.

    Returns:
        Una aproximación del coseno de x mediante la serie de Taylor truncada en el término n.
    """
    cosap = 0 #Comienza en cero para no afectar el valor de la suma
    for i in range(0, n+1): #Se efectua la suma de taylor desde 0 hasta una cantidad n veces elegida por el usaurio
        cosap += (-1)**i * ((x)**(2*i))/factorial(2*i) # Formula para hallar la aproximacion de coseno
    return cosap #Regresa el valor aproximado de coseno de x

def cosreal(x):
    """
    Calcula el valor real del coseno de x.

    Args:
        x: Un número real.

    Returns:
        El valor real del coseno de x.
    """
    cosre = math.cos(x) #Se halla el valor del coseno real de "x" mediante import math
    return cosre #Regresa el valor de coseno

def calcularn(x):
    """
    Calcula la cantidad de términos de la serie de Taylor necesarios para que la aproximación del coseno de x tenga un error menor a 0.001%.

    Args:
        x: Un número real.

    Returns:
        La cantidad de términos de la serie de Taylor necesarios para que la aproximación del coseno de x tenga un error menor a 0.001%.
    """
    n = 0
    aprox  = cosaprox(x,n)
    real = cosreal(x)
    error = abs(real - aprox)
    while error > 0.00001: #Se actualizan los valores hasta hallar el valor "n" que cumpla la condicion
        n += 1
        aprox = cosaprox(x,n)
        real = cosreal(x)
        error = abs(real - aprox)
    return n #Regresa el valor "n" obtenido

def calcularn2(x):
    """
    Calcula la cantidad de términos de la serie de Taylor necesarios para que la aproximación del coseno de x tenga un error menor a 0.1%.

    Args:
        x: Un número real.

    Returns:
        La cantidad de términos de la serie de Taylor necesarios para que la aproximación del coseno de x tenga un error menor a 0.1%.
    """
    n = 0
    aprox  = cosaprox(x,n)
    real = cosreal(x)
    error = abs(real - aprox)
    while error > 0.001: #Se actualizan los valores hasta hallar el valor "n" que cumpla la condicion
        n += 1
        aprox = cosaprox(x,n)
        real = cosreal(x)
        error = abs(real - aprox)
    return n #Regresa el valor "n" obtenido

def calcularn3(x):
    """
    Calcula la cantidad de términos de la serie de Taylor necesarios para que la aproximación del coseno de x tenga un error menor a 1%.

    Args:
        x: Un número real.

    Returns:
        La cantidad de términos de la serie de Taylor necesarios para que la aproximación del coseno de x tenga un error menor a 1%.
    """
    n = 0
    aprox  = cosaprox(x,n)
    real = cosreal(x)
    error = abs(real - aprox)
    while error > 0.01: #Se actualizan los valores hasta hallar el valor "n" que cumpla la condicion
        n += 1
        aprox = cosaprox(x,n)
        real = cosreal(x)
        error = abs(real - aprox)
    return n #Regresa el valor "n" obtenido

def calcularn4(x):
    """
    Calcula la cantidad de términos de la serie de Taylor necesarios para que la aproximación del coseno de x tenga un error menor al 10%.

    Args:
        x: Un número real.

    Returns:
        La cantidad de términos de la serie de Taylor necesarios para que la aproximación del coseno de x tenga un error menor al 10%.
    """
    n = 0
    aprox  = cosaprox(x,n)
    real = cosreal(x)
    error = abs(real - aprox)
    while error > 0.1: #Se actualizan los valores hasta hallar el valor "n" que cumpla la condicion
        n += 1
        aprox = cosaprox(x,n)
        real = cosreal(x)
        error = abs(real - aprox)
    return n #Regresa el valor "n" obtenido

if __name__ == "__main__":
    x = float(input("ingrese un numero x para calcular el coseno")) #Numero al cual se le sacara el coseno
    n = int(input("Ingrese la cantidad de sumatorias de taylord a evaluar")) #Cantidad de veces que se hara la suma de taylor
    #Se llaman las funciones
    aprox = cosaprox(x,n) 
    real = cosreal(x)
    nerror = calcularn(x)
    nerror2 = calcularn2(x)
    nerror3 = calcularn3(x)
    nerror4 = calcularn4(x)
    error = abs(real - aprox)
    #Se imprimen los resultados obtenidos
    print("el valor arpoximado del coseno de " + str(x) + " es: " + str(aprox) + " y El valor real es: " + str(real))
    print("El error con " +str(n)+" sumas es: " + str(error)) 
    print("Para un error menor al 10% la cantidad de 'n' que se necesitan son: " + str(nerror4))  
    print("Para un error menor al 1% la cantidad de 'n' que se necesitan son: " + str(nerror3))
    print("Para un error menor al 0.1% la cantidad de 'n' que se necesitan son: " + str(nerror2))  
    print("Para un error menor al 0.001% la cantidad de 'n' que se necesitan son: " + str(nerror))  
```
</p></details></br>

##### Para este codigo se realiza lo siguiente:
+ Se define una funcion factorial, para usarla al momento de la aproximación del coseno
+ Para la aproximación de coseno se usa el ciclo for para sumar la cantidad actual con la anterior, una cantidad "n" de veces.
+ Para el coseno real se usa import math y math.cos(x)
+ Para hallar los distintos valores de "n", con su respectivo error, se usan funciones con cilo while por cada error diferente que se quiera hallar (0.001, 0.1, 1, 10) , hasta que se cumpla la condicion, al final regresa el valor de "n" que se necesita para cada error deseado.
+ Al final en la funcion "main", se ingresan los valores "x" y "n" a evaluar, se llaman las funciones usadas, y imprimen todos los valores que se obtuvieron.

### 5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.
<details><summary>codigo de manera iterativa</summary><p>

``` python
def mcd(num1, num2):
    """
    Calcula el máximo común divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides.

    Args:
        num1 (int): El primer número entero.
        num2 (int): El segundo número entero.

    Returns:
        int: El MCD de los dos números enteros.
    """
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
```
</p></details></br>

<details><summary>codigo de manera recursiva</summary><p>

``` python
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
```
</p></details></br>

##### En este programa se calculo el mcd y el mcm de esta manera:
+ Para el mcd, se usa el teorema de Euclideas el cual dice: 
+ El máximo común divisor (MCD) de dos números enteros se puede calcular mediante la división sucesiva de estos números hasta que el residuo sea cero. El MCD será el último divisor diferente de cero que se haya utilizado en la sucesión de divisiones.
+ Ejemplo mcd(120,84):
$$120 ÷ 84 = 1$$
+ con residuo 36
$$84 ÷ 36 = 2$$
+ con residuo 12
$$36 ÷ 12 = 3$$
+ con residuo 0 
+ Como el último divisor diferente de cero es 12, entonces el MCD de 120 y 84 es 12.
+ Para el mcm, se uso la siguiente operacion para calcularlo:
+ + mcm(a,b) = (a*b) / mcd(a,b)
+ Ejemplo mmc(120/84):
$$(120 * 84)/12$$
$$10*84$$
+ mcm(120, 84) = 840

##### Respecto al codigo:
+ Se puede hacer tanto de manera iterativa como recursiva, pero solo cambia la parte de hallar el mcd, ya que es la unica parte en donde se usa ciclos whiles
+ Se llama la funcion del mcd, dentro de la del mcm para hallar el valor del mcm de los 2 numeros ingresados.
+ Al final solo se llama la funcion del mcm, ya que es la que regresa el valor que necesitamos


### 6. Desarrollar un programa que determine si en una lista no existen elementos repetidos.
<details><summary>codigo</summary><p>

``` python
def crearlista(e):
    """
    Crea una lista de tamaño especificado por el usuario, pidiendo al usuario que ingrese cada elemento.

    Args:
        e(int): El tamaño de la lista a crear.

    Returns:
        list: Una lista con los elementos ingresados por el usuario.
    """
    lista = []  
    for i in range(e):
        n = str(input("Ingrese elemento para la lista"))
        lista.append(n)
    return lista
    
def sin_repetidos(lista):
    """
    Determina si una lista tiene elementos repetidos.

    Args:
        lista (list): La lista a verificar.

    Returns:
        bool: True si la lista tiene elementos repetidos, False si no.
    """
    for i in range(len(lista)): 
        if lista[i] in lista[i+1:]:  # Se usa [i+1:] para crear una nueva lista que contiene los elementos de la lista original a partir del índice "i+1" hasta el final de la lista. 
            return False # Si hay repetidos regresa False
    return True #Si no hay repetidos regresa True

def repetidos(lista):
    """
    Verifica si una lista tiene elementos repetidos y devuelve un mensaje.

    Args:
        lista (list): La lista a verificar.

    Returns:
        str: Un mensaje indicando si la lista tiene elementos repetidos o no.
    """
    if sin_repetidos(lista): #Se aplica la funcion sin repetidos en la lista, para verifiacr si tiene o no elementos repetidos
        mensaje = "La lista ingresada no tiene elementos repetidos"
    else:
        mensaje = "La lista ingresada tiene elementos repetidos"
    return mensaje #Dependiendo si tieno o no, se regresara alguno de los dos mensajes

if __name__ == "__main__":
    e = int(input("ingrese el tamaño de la lista 1: ")) #Cantidad de elementos de la lista
    #Se llama las funciones
    lista = crearlista(e)
    repetir = repetidos(lista)
    #Se imprime
    print("La lista ingresada: ", lista)
    print(repet
```
</p></details></br>

+ La función crearlista recibe un número entero e y crea una lista lista con e elementos, ingresados por el usuario.
+ La función "sin_repetidos" recibe una lista lista y verifica si existen elementos repetidos en ella. Para ello, itera sobre cada elemento de la lista usando "[i+1:]" y compara si está presente en el resto de la lista. Si encuentra un elemento repetido, retorna False. Si no hay elementos repetidos, retorna True.
+ La función "repetidos" recibe una lista y verifica si existen elementos repetidos en ella utilizando la función "sin_repetidos". Si "sin_repetidos" retorna "True", significa que la lista no tiene elementos repetidos, y regresa un mensaje indicando que la lista no tiene elementos repetidos. Si "sin_repetidos" retorna False, significa que la lista tiene elementos repetidos, y regresa un mensaje indicando que la lista tiene elementos repetidos. 
+ En el bloque "if __name__ == "__main__":"", se solicita al usuario que ingrese el tamaño de la lista, se llaman las funciones, y se imprimen los valores que arrojan las funciones.

### 7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'.
<details><summary>codigo</summary><p>

``` python
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
            if letra in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:  # verifica si la letra es una vocal
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
```
</p></details></br>

+ La "función crearlista(e)" recibe un entero e y devuelve una lista de longitud "e" que se llena con cadenas de caracteres ingresadas por el usuario.
+ La función vocales(lista) recibe una lista de cadenas de caracteres y busca si existe una cadena con dos o más vocales. Si encuentra alguna cadena con dos o más vocales, imprime un mensaje diciendo qué cadena es la que tiene dos o más vocales. Si no encuentra ninguna cadena con dos o más vocales, imprime un mensaje diciendo que no existe tal cadena en la lista.
+ La variable encontrado se utiliza para saber si se encontró alguna cadena con dos o más vocales en la lista o no.
+ Se crea una lista con las vocales, de todas las formas en la que se pueden ingresar y asi revisar si cada letra de la palabra tiene 2 o mas vocales:  ['a', 'A', 'á', 'Á', 'é', 'É', 'e', 'E', 'i', 'I', 'í', 'Í', 'o', 'O', 'ó', 'Ó', 'u', 'U', 'ú', 'Ú'].
+ El código principal pregunta por el tamaño de la lista a crear, llama a la función crearlista(e), llama a la función vocales(lista) con la lista creada, y imprime los valores obtenidos.

### 8. Desarrollar un programa que dadas dos listas determine que elementos tiene la primer lista que no tenga la segunda lista.
<details><summary>codigo</summary><p>

``` python
def crearlista1(e):
    """
    Crea una lista de cadenas de caracteres de longitud e.

    Returns:
        list: La lista con e elementos.
    """
    lista1 = []  # inicializa una lista vacía
    for i in range(e):  # itera sobre un rango de e veces
        n = str(input("Ingrese elemento para la lista 1"))  # solicita una cadena de caracteres al usuario
        lista1.append(n)  # agrega la cadena a la lista
    return (lista1)  # retorna la lista creada

def crearlista2(f):
    """
    Crea una lista de cadenas de caracteres de longitud f.

    Returns:
        list: La lista con f elementos.
    """
    lista2 = []  # inicializa una lista vacía
    for i in range(f):  # itera sobre un rango de f veces
        n = str(input("Ingrese elemento para la lista 2"))  # solicita una cadena de caracteres al usuario
        lista2.append(n)  # agrega la cadena a la lista
    return (lista2)  # retorna la lista creada

def funcionbuscar(lista1, lista2):
    """
    Busca los elementos de lista1 que no están en lista2 y los devuelve como una lista.

    Args:
    lista1 (list): la lista de la que se extraerán los elementos.
    lista2 (list): la lista que se utilizará para comprobar qué elementos están en lista1.

    Returns:
    list: una lista de los elementos de lista1 que no están en lista2.
    """
    numeros = []
    for i in lista1: # Este bucle itera a través de los elementos de la primera lista, uno por uno.
        if i not in lista2: # Si el elemento actual de la lista1 no está en la segunda lista (lista2), el siguiente bloque de código se ejecuta.
            numeros.append(i) # Agrega el elemento actual (i) a la lista "numeros".
    return numeros # Devuelve la lista "numeros" que contiene los elementos que estaban en la primera lista pero no en la segunda lista.

if __name__ == "__main__":
    # Tamaño de la listas
    e = int(input("Ingrese el tamaño de la lista 1: "))
    f = int(input("Ingrese el tamaño de la lista 2: "))
    # Se llaman las funciones
    lista1 = crearlista1(e)
    lista2 = crearlista2(f)
    buscar = funcionbuscar(lista1, lista2)
    # Se imprimen los valores
    print("Lista 1: " ,lista1)
    print("Lista 2; " ,lista2)
    print("Elementos que tiene la primer lista y la segunda no: " ,buscar)
```

</p></details></br>
+ La función "crearlista1(e)" crea una lista de cadenas de caracteres de longitud "e". Toma un argumento "e" que indica cuántos elementos debe tener la lista. Retorna la lista creada.

+ La función "crearlista2(f)" crea una lista de cadenas de caracteres de longitud "f". Toma un argumento "f" que indica cuántos elementos debe tener la lista. Retorna la lista creada.

##### La función funcionbuscar(lista1, lista2):
+ Crea una lista vacía llamada "numeros".
+ Itera sobre los elementos de la lista1, verificando si el elemento actual no está en la lista2.
+ Si el elemento no está en lista2, lo agrega a la lista "numeros".
+ Retorna la lista "numeros" que contiene los elementos que estaban en la primera lista pero no en la segunda lista.

### 9. Resolver el punto 7 del taller 1 usando operaciones con vectores.
<details><summary>codigo</summary><p>

``` python
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

```
</p></details></br>

#### Las funciones que se usan:
+ crearlista(): Esta función solicita cinco números al usuario y los almacena en una lista. Se utiliza un bucle for para iterar cinco veces y se utiliza la función append() para agregar cada número a la lista. Devuelve la lista creada.
+ promedio(lista): Esta función calcula el promedio de los números en la lista. Utiliza un bucle for para iterar sobre la lista y acumular la suma de los valores. Luego, divide la suma total por la cantidad de números en la lista para obtener el promedio. Imprime el resultado y devuelve el valor del promedio.
+ mediana(lista): Esta función calcula la mediana de los números en la lista. Primero, ordena la lista de menor a mayor utilizando el método sort(). Luego, encuentra el elemento central de la lista y lo devuelve.
+ promediomultiplicativo(lista): Esta función calcula el promedio multiplicativo de los números en la lista. Utiliza un bucle for para iterar sobre la lista y acumular el producto de los valores. Luego, eleva el producto total a la potencia de 1/n, donde n es la cantidad de números en la lista. Si el producto es negativo, toma su valor absoluto y calcula su raíz n-ésima antes de volver a hacerlo negativo. Imprime el resultado y devuelve el valor del promedio multiplicativo.
+ ordenarmenormayor(lista): Esta función ordena los números de la lista de menor a mayor utilizando el método sort(). Imprime la lista ordenada y devuelve la lista.
+ ordenarmayormenor(lista): Esta función ordena los números de la lista de mayor a menor utilizando el método sort() con el parámetro reverse=True. Imprime la lista ordenada y devuelve la lista.
+ potenciadelmayorelevadoalmenor(lista): Esta función calcula la potencia del mayor número de la lista elevado al menor número de la lista utilizando las funciones max() y min(). Imprime el resultado y devuelve el valor de la potencia.
+ raizcubicadelmenornumero(lista): Esta función calcula la raíz cúbica del número más pequeño de la lista utilizando la función min(). Si el número es negativo, toma su valor absoluto, calcula su raíz cúbica y lo hace negativo de nuevo. Imprime el resultado y devuelve el valor de la raíz cúbica.
+ Por último, el programa utiliza la función crearlista() para solicitar al usuario que ingrese los números y luego llama a cada una de las funciones definidas para calcular y mostrar los resultados.

### 10. Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus columnas y de cada diagonal es igual.
<details><summary>codigo</summary><p>

``` python
# Desarrollar un algoritmo que determine si una matriz es mágica. Se dice que una 
# matriz cuadrada es mágica si la suma de cada una de sus filas, de cada una de sus 
# columnas y de cada diagonal es igual.

def matriz_magic(matriz):
    """
    Verifica si una matriz es mágica.

    Args:
    matriz (list): Una lista de listas que representa la matriz a verificar.

    Returns:
    bool: True si la matriz es mágica, False en caso contrario.
    """
    n = len(matriz)
    # sumdiade = suma diagonal derecha
    sumdiade = sum(matriz[i][i] for i in range(n))
    # sumdiaiz = suma diagonal izquierda
    sumdiaiz = sum(matriz[i][n-i-1] for i in range(n))
    if sumdiade != sumdiaiz:
        return False
    # para comprobar las sumas de filas, columnas y diagonales
    for i in range(n):
        if sum(matriz[i]) != sumdiade:
            return False
        if sum(matriz[j][i] for j in range(n)) != sumdiade:
            return False
    return True

# Para "cuadrar" la matriz cuadrada.
n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        entrada = int(input("Ingrese el elemento"+ str(i) + "," +str(j)+ ":" ))
        fila.append(entrada)
    matriz.append(fila)

# Para mostrar la matriz.
print("La matriz...")
for i in range(len(matriz)):
    print(matriz[i])

# Da el veredicto.
if matriz_magic(matriz):
    print("... es mágica")
else:
    print("... NO es mágica")

```
</p></details></br>
+ Este código verifica si una matriz cuadrada es mágica, es decir, si la suma de cada una de sus filas, columnas y diagonales es igual.
+ Primero se define la función matriz_magic()
+ Para verificar si la matriz es mágica, se calcula la suma de las diagonales y se compara. Si no son iguales, la matriz no es mágica y se devuelve False. 
+ Luego, para cada fila, columna y diagonal se calcula su suma y se compara con la suma de las diagonales. Si alguna suma es diferente, la matriz no es mágica y se devuelve False. Si todas las sumas son iguales, la matriz es mágica y se devuelve True.
+ En la funcion main, se solicita al usuario que ingrese los valores de la matriz y los almacena. Luego, muestra la matriz ingresada y llama a la función matriz_magic() para verificar si es mágica o no. Finalmente, muestra el resultado.

