from modulos.tienda import Tienda
from modulos.productos import Producto
# _________________________________________________________________
# =================================================================
# ========================CREAR===TIENDAS==========================
la_verduleria = Tienda("LA_VERDULERIA_DEL_BARRIO")
##     aLmacen_tito = Tienda("Almacen Don Tito")
##     ph_tires = Tienda("Padre_Hurtado Tires")
print(la_verduleria)
##     print(aLmacen_tito)
##     print(ph_tires)
# _________________________________________________________________
# =================================================================
# ========================CREAR===PRODUCTOS========================
print("vamos a CREAR algunos productos.\n")
zanahoria = Producto("ZANAHORIA", 600, "HORTALIZAS")
kiwi = Producto("KIWI", 500, "FRUTAS")
papa = Producto("PAPA", 550,"HORTALIZAS")
espinaca = Producto("ESPINACA", 1150,"HORTALIZAS")
banana = Producto("PLATANO", 1190, "FRUTAS")
# _________________________________________________________________
# =================================================================
# ========================ANHADIR===PRODUCTOS======================
print("\nVamos a ANHadir los productos Creados:")
la_verduleria.anhadir_producto(zanahoria)
la_verduleria.anhadir_producto(kiwi)
la_verduleria.anhadir_producto(papa)
la_verduleria.anhadir_producto(espinaca)
la_verduleria.anhadir_producto(banana)
print("Terminamos de ANHadir productos.\n")
# _________________________________________________________________
# =================================================================
# ========================VENDER===PRODUCTO========================
la_verduleria.vender_producto(3)
la_verduleria.vender_producto(1)
# print(la_verduleria)
# _________________________________________________________________
# =================================================================
# ===================PROBAR===INFLATION===METHOD===================
print("\nRealizando AUMENTO por inflaciOn\n")
la_verduleria.inflacion(10)
# _________________________________________________________________
# =================================================================
# ===================PROBAR===CLEARANCE===METHOD===================
print("\nRealizando SALE a productos de la CategorIa indicada\n")
la_verduleria.descuentazo("HORTALIZAS", 95)