from producto import Producto
from productoServices import ProductoService


class App:
    def menu_producto(self):
        print("\n\n\tMENU - Producto")
        print("\n1.\tListar productos")
        print("2.\tAgregar producto")
        print("3.\tModificar producto")
        print("4.\tEliminar producto")
        print("  \tSalir (otra tecla)")
        return int(input("\n\tElija una opción: "))


if __name__ == '__main__':
    productoService = ProductoService()

    app = App()
    while True:
        opcion_producto = app.menu_producto()
        if opcion_producto == 1:
            print("\n---->\tLista de productos:\n")
            print(productoService.get_productosList())
        if opcion_producto == 2:
            _descripcion = input("\n----> \tIngrese la descripcion: ")
            _precio = int(input("\n----> \tIngrese el precio: "))
            _tipo = input("\n----> \tIngrese el tipo: ")
            pro1 = Producto(_descripcion, _precio, _tipo)
            productoService.add_producto(pro1)

        if opcion_producto == 3:
            key = int(
                input("\n----> \tIngrese la key del producto a modificar: ")
                     )
            _descripcion = input("\n----> \tIngrese la nueva descripcion: ")
            _precio = int(input("\n----> \tIngrese el nuevo precio: "))
            _tipo = input("\n----> \tIngrese el nuevo tipo: ")
            pro1 = Producto(_descripcion, _precio, _tipo)
            productoService.update_producto(key, pro1)
        if opcion_producto == 4:
            key = int(
                input("\n----> \tIngrese la key del producto a eliminar: ")
                     )
            productoService.delete_producto(key)
        if opcion_producto < 1 or opcion_producto > 4:
            break
