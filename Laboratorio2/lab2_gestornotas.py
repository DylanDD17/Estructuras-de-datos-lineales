class Calificacion:
    def __init__(self, actividad, nota):
        self.actividad = actividad
        self.nota = nota
    def __str__(self):
        return f"\tActividad: {self.actividad}, Nota: {self.nota}"
    
class Estudiante:
    def __init__(self, name):
        self.name = name
        self.calificaciones = [] #Cada estudiante tiene una lista de calificaciones
    def __str__(self):
        return f"Estudiante: {self.name}"

    def agregar_calificacion(self, actividad, nota):
        self.calificaciones.append(Calificacion(actividad, nota))

    def eliminar_calificacion(self, actividad):
        for calificacion in self.calificaciones:
            if calificacion.actividad == actividad:
                self.calificaciones.remove(calificacion)
                return ("\tEliminado")
        return ("\tNo encontrado")
    
    def modificar_calificacion(self, actividad, nota):
        for calificacion in self.calificaciones:
            if calificacion.actividad == actividad:
                calificacion.nota = nota
                return ("\tModificado")
        return ("\tNo encontrado")
    
    def calcular_promedio(self):
        total = sum(calificacion.nota for calificacion in self.calificaciones)
        return total / len(self.calificaciones) 
    
    def mostrar_calificaciones(self):
        for calificacion in self.calificaciones:
            print(calificacion)

class Curso:
    def __init__(self, name):
        self.name = name
        self.estudiantes = []
    def __str__(self):
        return f"Curso: {self.name}"
    
    def mostrar_estudiantes(self):
        print(f"\nEstudiantes en el curso {self.name}:")
        for estudiante in self.estudiantes:
            print(estudiante)

# Ejemplo de uso
print("~ GESTOR DE NOTAS ~\n")
if __name__ == "__main__":

    curso = Curso("EDL")

    print(curso)
    estudiantes = []
    curso.estudiantes.append(Estudiante("Laura"))
    curso.estudiantes.append(Estudiante("Ana"))
    curso.estudiantes.append(Estudiante("Luis"))
    curso.mostrar_estudiantes()

    print(f"\n-----CALIFICACIONES {curso.estudiantes[0].name}-----")
    estudiante0 = curso.estudiantes[0] #Laura
    estudiante0.agregar_calificacion("Parcial Final", 90)
    estudiante0.agregar_calificacion("Proyecto Final", 85)
    print(f"~Calificaciones de {estudiante0.name}:")
    estudiante0.mostrar_calificaciones() #Mostrar calificaciones Laura
    print("Eliminar 'Proyecto Final'")
    eliminado = estudiante0.eliminar_calificacion("Proyecto Final") 
    print(f"{eliminado}")
    print(f"~Calificaciones de {estudiante0.name} después de eliminar Proyecto Final:")
    estudiante0.mostrar_calificaciones() #Mostrar calificaciones después de eliminar
    print("Modificar 'Parcial Final' a 95")
    modificado = estudiante0.modificar_calificacion("Parcial Final", 95)
    print(f"{modificado}")
    print(f"~Calificaciones de {estudiante0.name} después de modificar Parcial Final:")
    estudiante0.mostrar_calificaciones() #Mostrar calificaciones después de modificar
    promedio = estudiante0.calcular_promedio()
    print(f"~Promedio de {estudiante0.name}: {promedio}")

    print(f"\n-----CALIFICACIONES {curso.estudiantes[1].name}-----")
    estudiante1 = curso.estudiantes[1] #Ana
    estudiante1.agregar_calificacion("Parcial Final", 75)
    estudiante1.agregar_calificacion("Proyecto Final", 85)
    print(f"~Calificaciones de {estudiante1.name}:")
    estudiante1.mostrar_calificaciones() #Mostrar calificaciones Ana
    print("Eliminar 'Parcial Final'")
    eliminado = estudiante1.eliminar_calificacion("Parcial Final")
    print(f"{eliminado}")
    print(f"~Calificaciones de {estudiante1.name} después de eliminar Paracial Final:")
    estudiante1.mostrar_calificaciones() #Mostrar calificaciones después de eliminar
    print("Modificar 'Proyecto Final' a 93")
    modificado = estudiante1.modificar_calificacion("Proyecto Final", 93)
    print(f"{modificado}") #Modificar Proyecto Final
    print(f"~Calificaciones de {estudiante1.name} después de modificar Proyecto Final:")
    estudiante1.mostrar_calificaciones() #Mostrar calificaciones después de modificar
    promedio = estudiante1.calcular_promedio()
    print(f"~Promedio de {estudiante1.name}: {promedio}")

    print(f"\n-----CALIFICACIONES {curso.estudiantes[2].name}-----")
    estudiante2 = curso.estudiantes[2] #Luis
    estudiante2.agregar_calificacion("Parcial Final", 60)
    estudiante2.agregar_calificacion("Proyecto Final", 93)
    print(f"~Calificaciones de {estudiante2.name}:")
    estudiante2.mostrar_calificaciones() #Mostrar calificaciones Luis
    print("Eliminar 'Actividad 1'")
    eliminado = estudiante2.eliminar_calificacion("Actividad 1") #No existe
    print(f"{eliminado}")
    print(f"~Calificaciones de {estudiante2.name} después de intentar eliminar 'Actividad 1':")
    estudiante2.mostrar_calificaciones() #Mostrar calificaciones después de eliminar
    print("Modificar 'Parcial Final' a 70 y 'Proyecto Final' a 96")
    modificado = estudiante2.modificar_calificacion("Parcial Final", 70)
    modificado2 = estudiante2.modificar_calificacion("Proyecto Final", 96)
    print(f"{modificado}") #Modificar Parcial Final
    print(f"{modificado2}") #Modificar Proyecto Final
    print(f"~Calificaciones de {estudiante2.name} después de modificar Parcial Final y Proyecto Final:")
    estudiante2.mostrar_calificaciones() #Mostrar calificaciones después de modificar
    promedio = estudiante2.calcular_promedio()
    print(f"~Promedio de {estudiante2.name}: {promedio}")

print("\n~ Fin ~")