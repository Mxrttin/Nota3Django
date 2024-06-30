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
                "nombre": libro.titulo,
                "portada_url": libro.imagen.url if libro.imagen else None,                
                "acumulado": float(libro.precio),  # Convertir a float para asegurar cálculos numéricos
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += float(libro.precio)

        self.guardarCarrito()

    def guardarCarrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, libro):
        id = str(libro.id)

        if id in self.carrito:
            del self.carrito[id]
            self.guardarCarrito()

    def restar(self, libro):
        id = str(libro.id)

        if id in self.carrito.keys():
            if self.carrito[id]["cantidad"] > 1:
                self.carrito[id]["cantidad"] -= 1
                self.carrito[id]["acumulado"] -= float(libro.precio)
            else:
                self.eliminar(libro)
            
            self.guardarCarrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True