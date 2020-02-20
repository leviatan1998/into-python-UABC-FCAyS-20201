import types

# creamos una funcion que nos da 
# el numero de decadas
def obtenerNumeroDeDecadas(dato):
  print("Numero de decadas" + dato[0])
  # print("Numero de decadas" + dato[0)
  # Funcion mejorada
  print(type(dato))
  # if isinstance(, int)
  
# Declaramos una variable para el nombre de
nombre = "Miguel"

# En python podemos identificar tipos
# en la siguiente linea se identifica
# y muestra el tipo
print(type(nombre))

anios = 21
# Se comprueba el tipo de dato de anios
print(type(anios))

# Pedimos que el usuario nos indique datos
nuevoNombre = input("Dame tu nombre!!")
print(type(nuevoNombre))
nuevaEdad = input("Dame tu edad!!")
print(type(nuevaEdad))

# Mostrando inicial y transformando cadenas
print("Hola" + nuevoNombre +
", tu inicial es" + nuevoNombre [1])
print("Tu nombre en mayusculas es:" + 
nuevoNombre.upper())
## Utilizamos la funcion para decadas pasando
## la nuevaEdad como parametro
obtenerNumeroDeDecadas(nuevaEdad)


  