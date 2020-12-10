from django.db import models
# Para ver todos los tipos de los modelos:
# https://docs.djangoproject.com/en/3.1/ref/models/fields/
# Create your models here.
class ProductoModel(models.Model):
    # si yo no defino la primary key se va a crear automaticamente en mi bd con el nombre Id
    # solamente puede haber un AutoField por modelo
    # si no indico el nombre de la columna en la bd se va a crear con el nombre del atributo
    productoId = models.AutoField(auto_created=True, primary_key=True, unique=True, null=False, db_column='prod_id')
    productoNombre = models.CharField(max_length=45, db_column='prod_nom')
    productoPrecio = models.DecimalField(max_digits=5, decimal_places=2, db_column='prod_prec')
    productoMinimo = models.IntegerField(db_column='prod_minimo')
    # para definir algunas opciones extras como el nombre de la tabla, ordenamiento y modificar opciones de visualizacion en el panel administrativo se crea una clase Meta
    class Meta:
        # esta clase sirve para pasar metadatos al padre , es decir como estamos heredando de la clase Model, le vamos a pasar configuracion a ese padre
        db_table = 't_producto'
        # para cambiar algunas opciones del panel administrativo
        verbose_name_plural = "Productos"
        verbose_name = "Producto"

class AlmacenModel(models.Model):
    almacenId = models.AutoField(primary_key=True, unique=True, null=False, db_column='alma_id')
    almacenDescripcion = models.CharField(max_length=45, db_column='alma_desc')
    class Meta:
        db_table='t_almacen'
        verbose_name_plural = "Almacenes"
        verbose_name = "Almacen"

class ProductoAlmacenModel(models.Model):
    productoAlmacenId = models.AutoField(primary_key=True, unique=True, null=False, db_column='prod_alma_id')
    productoAlmacenCantidad = models.IntegerField(db_column='prod_alma_cant')
    # CASCADE => esta opcion va a permitir eliminar el padre y que cuando se elimine, automaticamente todos los hijos se eliminen tambien
    # PROTECT => esta opcion no va a permitir eliminar el padre, y solmanente se va a poder eliminar el padre cuando no tenga ningun hijo relacionado
    # SET_NULL => permite eliminar al padre pero cuando este es eliminado, todos sus hijos quedan sin padre, es decir su campo de fk cambia de valor a null
    # DO_NOTHING => deja eliminar al padre y no elimina su valor del hijo, es decir se queda con esa llave aunque ya no exista, esto genera una mala integridad de los datos y crea errores al momento de devolver segun su padre
    productoId = models.ForeignKey(ProductoModel, on_delete=models.PROTECT, db_column='producto_id', related_name='productosAlmacenes')
    almacenId= models.ForeignKey(AlmacenModel, on_delete=models.PROTECT, db_column='alma_id', related_name='almacenesProductos')
    class Meta:
        db_table='t_prod_alma'

# registrar los otros modelos faltantes (CabeceraVentaMdel y DetalleVentaModel)