class Producto:
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

def mostrar_menu():
    print("Sistema de Inventario")
    print("1.  Agregar producto")
    print("2.  Mostrar producto")
    print("3.  Buscar producto")
    print("4.  Actualizar producto")
    print("5.  Eliminar producto")
    print("6.  Salir")

inventario = []


while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")

    if opcion == "6":
        print("Saliendo del programa.")
        break

    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")
        try:
            cantidad = int(input("Ingrese la cantidad: "))
            precio = float(input("Ingrese el precio"))
            producto = Producto(nombre,cantidad,precio)
            inventario.append(producto)
            print("producto agregado. ")
        except ValueError:
            print("error: Entrada no valida.")
    elif opcion == "2":
        for i in inventario:
            print(f'Nombre: {i.nombre}, Cantidad: {i.cantidad}, Precio: {i.precio}')  # Mostramos los productos
    elif opcion == "3":
        nombre = input("Ingrese el nombre del producto a buscar. ")
        encontrado = False
        for i in inventario:
            if i.nombre == nombre:
                print(f'Nombre:  {i.nombre}, Cantidad: {i.cantidad}, Precio: {i.precio}')
                encontrato = True
                break
            if not encontrado:
                print("Producto no encontrato")
    elif opcion == "4":
        nombre = input("Ingrese el nombre del producto a actualizar: ")
        encontrado = False
        for i in inventario:
            if i.nombre == nombre:
                try:
                    cantidad = int(input("Ingrese la nueva cantidad: "))
                    precio = float(input("Ingrese el nuevo precio: "))
                    i.cantidad = cantidad
                    i.precio = precio
                    print("Producto actualizado.")
                    encontrado = True
                    break
                except ValueError:
                    print("Error: Entrada no válida.")
        if not encontrado:
            print("Producto no encontrado.")

    elif opcion == "5":
        nombre = input("Ingrese el producto a eliminar: ")
        for i in inventario:
            if i.nombre == nombre:
                inventario.remove(i)
                print("Producto eliminado.")
                break

    else:
        print("opcion no valida.  Seguir intentando")
