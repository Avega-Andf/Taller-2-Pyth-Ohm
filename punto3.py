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