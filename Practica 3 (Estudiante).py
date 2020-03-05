class Estudiante:
  # Indicamos atributos para la clase
  edad = 0
  carrera = "Deconocida"
  universidad = "Desconocida"
  genero = "Femenino"
  
  # definimos funciones
  def festejar(self) :
    print("Festejando")
  
  def estudiar(self, materia) :
    print("Estudiando" + materia)
    
  def lloras(self) :
    print("Llorando")
  
  def dormir(self) :
    print("Durmiendo")
    
  # Ajustamos la edad
  def cambiarEdad(self, edadAlumno) :
    self.edad = edadAlumno
    print("Nueva edad", edadAlumno)
    
# Generamos un nuevo Estudiante
jonathan = Estudiante()
jonathan.estudiar("Logica para programacion")
# imprimimos atributo del objeto
jonathan.cambiarEdad(23)
print(jonathan.edad)
    