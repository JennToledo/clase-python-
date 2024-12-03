class CuentaArticulo: 
    # Aributos  
    __TotalDeCompra : 0.0 
    __descuento1 : 0.10 
    __descuento2 : 0.20
    __TotalApagar : 0.0 

    def CalcularTotalAPagar(self, TotalDeCompra, descuento1, descuento2):
        self.__TotalDeCompra = TotalDeCompra 
        self.__descuento1 = descuento1 
        self.__descuento2 = descuento2

        if self.__TotalDeCompra >= 100 <= 200:
            self.__TotalApagar = (self.__TotalDeCompra * self.__descuento1)
        elif self.__TotalDeCompra >= 200: 
            self.__TotalApagar = (self.__TotalDeCompra * self.__descuento2)
        return self.__TotalApagar
