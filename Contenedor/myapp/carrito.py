class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        pk = str(producto.id_producto)
        if pk not in self.carrito.keys():
            self.carrito[pk]={
                "producto_id": producto.id_producto,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[pk]["cantidad"] += 1
            self.carrito[pk]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        pk = str(producto.id_producto)
        if pk in self.carrito:
            del self.carrito[pk]
            self.guardar_carrito()

    def restar(self, producto):
        pk = str(producto.id_producto)
        if pk in self.carrito.keys():
            self.carrito[pk]["cantidad"] -= 1
            self.carrito[pk]["acumulado"] -= producto.precio
            if self.carrito[pk]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True