# Generated by Django 3.1.6 on 2021-02-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Facturacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuariomodel',
            name='usuarioCorreo',
            field=models.EmailField(db_column='usu_mail', help_text='Correo del usuario', max_length=50, unique=True),
        ),
    ]
