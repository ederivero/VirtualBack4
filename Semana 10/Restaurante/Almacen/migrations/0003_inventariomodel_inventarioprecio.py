# Generated by Django 3.1.6 on 2021-02-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Almacen', '0002_auto_20210204_1911'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventariomodel',
            name='inventarioPrecio',
            field=models.DecimalField(db_column='inventario_precio', decimal_places=2, default=10.2, max_digits=5, verbose_name='Precio del plato'),
            preserve_default=False,
        ),
    ]
