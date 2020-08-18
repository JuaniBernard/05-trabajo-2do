from repositorios import Repositorios


class ProductoService:
    def add_producto(self, producto):
        key = len(Repositorios.productosList)
        while key in Repositorios.productosList:
            key = key + 1
        Repositorios.productosList[key] = producto.__dict__
        return key

    def update_producto(self, key, producto):
        if key in Repositorios.productosList:
            Repositorios.productosList[key]['_descripcion'] = producto._descripcion
            Repositorios.productosList[key]['_precio'] = producto._precio
            Repositorios.productosList[key]['_tipo'] = producto._tipo
        else:
            raise ValueError("ID de producto incorrecta.")

    def delete_producto(self, key):
        if key in Repositorios.productosList:
            del Repositorios.productosList[key]
        else:
            raise ValueError("ID de producto incorrecta.")

    def get_productosList(self):
        return Repositorios.productosList
