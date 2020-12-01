from base_de_datos import bd

class ClienteModel(bd.Model):
    __tablename__="t_cliente"
    id_cliente = bd.Column("cli_id", bd.Integer, primary_key = True, autoincrement = True, nullable = False)
    dni_cliente = bd.Column("cli_dni", bd.String(8), nullable = False)
    nombre_cliente = bd.Column("cli_nomb", bd.String(45), nullable = False)
    apellido_cliente = bd.Column("cli_ape", bd.String(45), nullable = False)
    # Sirve para hacer la relacion inversa
    prestamosCliente = bd.relationship('PrestamoModel', backref='clientePrestamo')
    
    def __init__(self, dni, nombre, apellido):
        self.dni_cliente = dni
        self.nombre_cliente = nombre
        self.apellido_cliente = apellido