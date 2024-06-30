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

    def agregar(self, libro):
        id = str(libro.id)

        if id not in self.carrito.keys():
            self.carrito[id] = {
                "producto_id": libro.id,
                "nombre": libro.nombre,
                "acumulado": libro.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += libro.precio

        self.guardarCarrito()

    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(libro.id)

        if id in self.carrito:
            del self.carrito[id]
            self.guardarCarrito()

    def restar(self, producto):
        id = str(libro.id)

        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= libro.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardarCarrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True