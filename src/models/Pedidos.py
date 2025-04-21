class Pedido():

    def __init__(self, id, fecha, cedula, cliente_name, direccion, telefono, correo, costo, metodo_pago, estado_pedido, lote) -> None:
        self.id = id
        self.fecha = fecha
        self.cedula = cedula
        self.cliente_name = cliente_name
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.costo = costo
        self.metodo_pago = metodo_pago
        self.estado_pedido = estado_pedido
        self.lote = lote
