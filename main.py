# Definimos una funcion para indicar
# si la edad es par o impar
def edadParOImpar(edad) :
  if edad % 2 == 0 :
   print("Tu edad es par")
  else :
   print("Tu edad es impar")


# En este codigo repasamos algunos detalles
variableValida = "Ensenada"
otra_variable = "Tj"
# 3variable = "Mexicali" # No valida
variable3 = "Mexicali"
print("Ciudades en BC: " + variableValida + ", " + otra_variable + ", " + variable3)

x = 0.6
x = 3.9 * x *  (1 - x) 
print(x)

# elevamos un numero al cuadrado
tres = 3
tresAlCuadrado = 3 * 3 # Utiliza multiplicacion
print(tresAlCuadrado)
tresAlCuadrado = 3 ** 2 # Utiliza multiplicacion
print(tresAlCuadrado)

edad = 21 #Edad
edadParOImpar(edad)

operacion1 = 13 - 4 * (5 - 2) + 3 * (2 + 8)
print(operacion1)

operacion2 = 16 + 3 * (6 - 4) - 3 * 5
print(operacion2)

operacion3 = 23 - 8 + 6 *2 - 3 * 4
print(operacion3)

operacion4 = (6 * (7 * 5 - 4 * 6) + 81/ 9 - 6)
print(operacion4)