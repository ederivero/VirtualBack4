# Generated by Django 3.1.6 on 2021-02-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0002_auto_20210203_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariomodel',
            name='usuarioCorreo',
            field=models.EmailField(db_column='usu_mail', max_length=50, unique=True, verbose_name='Correo del usuario'),
        ),
    ]
