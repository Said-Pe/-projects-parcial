import json

class Presupuesto:
    def __init__(self, archivo):
        self.archivo = archivo

    def cargar_presupuesto(self):
        try:
            with open(self.archivo, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def guardar_presupuesto(self, presupuesto):
        with open(self.archivo, 'w') as f:
            json.dump(presupuesto, f, indent=4)

    def agregar_articulo(self, nombre, precio):
        if not isinstance(precio, float) and not isinstance(precio, int):
            print("El precio debe ser un número válido.")
            return

        if precio <= 0:
            print("El precio debe ser mayor que cero.")
            return

        articulo = {'nombre': nombre, 'precio': precio}
        presupuesto = self.cargar_presupuesto()
        presupuesto.append(articulo)
        self.guardar_presupuesto(presupuesto)
        print("Artículo agregado correctamente.")

    def buscar_articulo(self, nombre):
        nombre = nombre.lower()
        presupuesto = self.cargar_presupuesto()
        for articulo in presupuesto:
            if articulo['nombre'].lower() == nombre:
                return articulo
        print("Artículo no encontrado.")

    def editar_articulo(self, nombre, nuevo_precio):
        if not isinstance(nuevo_precio, float) and not isinstance(nuevo_precio, int):
            print("El nuevo precio debe ser un número válido.")
            return

        if nuevo_precio <= 0:
            print("El nuevo precio debe ser mayor que cero.")
            return

        presupuesto = self.cargar_presupuesto()
        for articulo in presupuesto:
            if articulo['nombre'].lower() == nombre.lower():
                articulo['precio'] = nuevo_precio
                self.guardar_presupuesto(presupuesto)
                print("Artículo editado correctamente.")
                return
        print("Artículo no encontrado.")

    def eliminar_articulo(self, nombre):
        nombre = nombre.lower()
        presupuesto = self.cargar_presupuesto()
        presupuesto = [articulo for articulo in presupuesto if articulo['nombre'].lower() != nombre]
        self.guardar_presupuesto(presupuesto)
        print("Artículo eliminado correctamente.")

def menu():
    print("1. Agregar artículo")
    print("2. Buscar artículo")
    print("3. Editar artículo")
    print("4. Eliminar artículo")
    print("5. Salir")

def main():
    presupuesto = Presupuesto("presupuesto.json")
    while True:
        menu()
        opcion = input("Seleccione una opción: ").lower()

        if opcion == "1":
            nombre = input("Nombre del artículo: ").lower()
            while True:
                try:
                    precio = float(input("Precio del artículo: "))
                    break
                except ValueError:
                    print("El precio debe ser un número válido.")
            presupuesto.agregar_articulo(nombre, precio)
        elif opcion == "2":
            nombre = input("Nombre del artículo a buscar: ").lower()
            articulo = presupuesto.buscar_articulo(nombre)
            if articulo:
                print(articulo)
        elif opcion == "3":
            nombre = input("Nombre del artículo a editar: ").lower()
            while True:
                try:
                    nuevo_precio = float(input("Nuevo precio del artículo: "))
                    break
                except ValueError:
                    print("El nuevo precio debe ser un número válido.")
            presupuesto.editar_articulo(nombre, nuevo_precio)
        elif opcion == "4":
            nombre = input("Nombre del artículo a eliminar: ").lower()
            presupuesto.eliminar_articulo(nombre)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
