class Cliente:

    def __init__(self, nombre, producto, pais, intereses):

        self.nombre = nombre
        self.producto = producto
        self.pais = pais
        self.i = intereses

    def __str__(self):

        return f"Hemos creado el registro en nuestra base de datos del cliente: {self.nombre}"


    def busqueda(self, pagina_web):

        print(f"El cliente {self.nombre} ha buscado desde la pagina web de {pagina_web} a cerca de instereses de {self.i} en el pais {self.pais}")


    def pagar(self, monto, hora):

        print(f"El joven {self.nombre} ha realizado una compra de unas {self.producto} con un precio de {monto} pesos a las {hora} de la noche.")      


  
           
        