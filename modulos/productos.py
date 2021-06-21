class Producto:
    def __init__(self, nombre_producto, precio_producto, cat_producto):
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto
        self.cat_producto = cat_producto

    def producto_info(self):
        print(f"Producto:  {self.nombre_producto} -- CategorIa: {self.cat_producto} --  PRECIO:  ${self.precio_producto}\n")
        return self

    def actualizar_precio(self, cambio_porcentaje, si_aumenta):
        if si_aumenta == True:
            self.precio_producto += (self.precio_producto * (cambio_porcentaje / 100))
        elif si_aumenta == False:
            self.precio_producto -= (self.precio_producto * (cambio_porcentaje / 100))
        return self

# _________________________________________________________________
# =================================================================
# zapallo = Producto("Zapallo", 100, "Hortalizas y Verduras")
# print(zapallo)
# zapallo.producto_info()
# _________________________________________________________________
# =================================================================