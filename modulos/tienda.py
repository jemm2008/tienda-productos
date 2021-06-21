class Tienda:
    def __init__(self, nombre_tienda, lista_productos = []):
        self.nombre_tienda = nombre_tienda
        self.lista_productos = lista_productos

    def __str__(self):
        return f"Nombre de la Tienda: {self.nombre_tienda}\nLista de Productos: {self.lista_productos}\n"
    
    def anhadir_producto(self, producto_nuevo):
        self.lista_productos.append(producto_nuevo)
        print("# # # # # # # PRODUCTO ANHADIDO # # # # # # #")
        producto_nuevo.producto_info()
        return self

    def vender_producto(self, id):
        print("\n# # # # # # # PRODUCTO VENDIDO # # # # # # #")
        self.lista_productos.pop(id).producto_info()
        return self

    def inflacion(self, porcentaje_incremento):
        a = 0
        for pro in self.lista_productos:
            a += 1
            print(f"=================Producto 0{a}:=================")
            pro.producto_info()
            print("AUMENTA su precio a: ")
            pro.actualizar_precio(porcentaje_incremento, True).producto_info()
        return self

    def descuentazo(self, categoria, descuentazo_porcentaje):
        a = 0
        for product in self.lista_productos:
            a += 1
            if product.cat_producto == categoria:
                print(f"=================Producto 0{a}:=================")
                product.producto_info()
                print("Se REMATA, y su nuevo precio de remate es: ")
                product.actualizar_precio(descuentazo_porcentaje, False).producto_info()
        print(f"Descuento de precios a toda la categoria {categoria}, realizado")
        return self

#########################################################
#####     coso = Tienda("VERDULERIA")
#####     print(coso)
#####     print("anhadir_P")
#####     pera = ("PERA", 1000, "FRUTAS")
#####     coco = ("COCO", 1511, "FRUTAS")
#####     coso.anhadir_producto(pera)
#####     coso.anhadir_producto(coco)
#####     print(coso)
#####     print("#############################")
#####     coso.vender_producto(1)