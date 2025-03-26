class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} (${self.precio:.2f})"
class Venta:
    def __init__(self):
        self.items = []  

    def agregar_item(self, producto, cantidad):
        self.items.append((producto, cantidad))

    def calcular_subtotal(self):
        subtotal = sum(producto.precio * cantidad for producto, cantidad in self.items)
        return subtotal
class Factura:
    def __init__(self, nro_factura, cliente, venta, impuesto=16):
        self.nro_factura = nro_factura
        self.cliente = cliente
        self.venta = venta  
        self.impuesto = impuesto

    def calcular_total(self):
        subtotal = self.venta.calcular_subtotal()
        total = subtotal * (1 + self.impuesto / 100)
        return total

    def mostrar_factura(self):
        print(f"Factura N°: {self.nro_factura}")
        print(f"Cliente: {self.cliente}")
        print("---------------------------------")
        print("Productos:")
        for idx, (producto, cantidad) in enumerate(self.venta.items, start=1):
            print(f"{idx}. {producto.nombre} x{cantidad}: ${producto.precio * cantidad:.2f}")
        print("---------------------------------")
        print(f"Subtotal: ${self.venta.calcular_subtotal():.2f}")
        print(f"Impuesto ({self.impuesto}%): ${self.venta.calcular_subtotal() * self.impuesto / 100:.2f}")
        print(f"Total: ${self.calcular_total():.2f}")

cafe = Producto("Café Premium", 5.50)
te = Producto("Té Verde", 3.20)
leche = Producto("Leche de Almendra", 4.00)


venta1 = Venta()
venta1.agregar_item(cafe, 2)
venta1.agregar_item(te, 3)
venta1.agregar_item(leche, 1)


factura1 = Factura(
    nro_factura="F-001",
    cliente="Ana Pérez",
    venta=venta1,
    impuesto=16  
)

factura1.mostrar_factura()