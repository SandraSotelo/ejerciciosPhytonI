class Tarea:
    def __init__(self,titulo,descripcion,estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado

def mostrar_menu():
    print("Sistema de Gestión de Tareas")
    print("1.  Agregar nueva tarea")
    print("2.  Mostrar todas las tareas")
    print("3.  Buscar una tarea por titulo")
    print("4.  Actualizar el estado de una tarea")
    print("5.  Eliminar una tarea por titulo")
    print("6.  Salir")

agenda = []

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    if opcion == "6":
        print("Saliendo del programa.")
        break

    if opcion == "1":
        try:
            titulo = input("Ingrese el título de la tarea: ")
            if not titulo:
                raise ValueError("El título no puede estar vacío")

            descripcion = input("Ingrese la descripción de la tarea: ")
            if not descripcion:
                raise ValueError("La descripción no puede estar vacía")

            estado = input("Ingrese el estado de la tarea (pendiente o completada): ")
            if estado.lower() not in ["pendiente", "completada"]:
                raise ValueError("El estado debe ser 'Pendiente' o 'Completada'")
            tareas = Tarea(titulo, descripcion, estado)
            agenda.append(tareas)
            print("Tarea agregada correctamente.")
        except ValueError as e:
            print(f"Error: {str(e)}")
    elif opcion == "2":
        for a in agenda:
            print(f'Titulo: {a.titulo}, Descripcion: {a.descripcion}, Estado: {a.estado}')
    elif opcion == "3":
        titulo = input("Ingrese el título de la tarea a buscar. ")
        encontrado = False
        for a in agenda:
            if a.titulo == titulo:
                print(f'Titulo:  {a.titulo}, Descripcion: {a.descripcion}, Estado: {a.estado}')
                encontrato = True
                break
            if not encontrado:
                print("La tarea indicada no fue encontrada")
    elif opcion == "4":
        titulo = input("Ingrese el titulo de la tareas a actualizar: ")
        encontrado = False
        for a in agenda:
            if a.titulo == titulo:
                try:
                    descripcion = input("Ingrese la nueva descripción de la tarea: ")
                    if not descripcion:
                        raise ValueError("La descripción no puede estar vacía")
                    estado = input("Ingrese el nuevo estado de la tarea (pendiente o completada): ")
                    if estado.lower() not in ["pendiente", "completada"]:
                        raise ValueError("El estado nuevo estado debe ser 'Pendiente' o 'Completada'")
                    a.descripcion = descripcion
                    a.estado = estado
                    print("Tarea actualizada correctamente.")
                except ValueError as e:
                    print(f"Error: {str(e)}")
    elif opcion == "5":
        titulo = input("Ingrese el titulo de la tarea a eliminar: ")
        for a in agenda:
            if a.titulo == titulo:
                agenda.remove(a)
                print("Tarea eliminada.")
                break

    else:
        print("opcion no valida.  Seguir intentando")

