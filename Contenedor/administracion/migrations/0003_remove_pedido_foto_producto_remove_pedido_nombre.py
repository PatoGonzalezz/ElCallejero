# Generated by Django 5.0.4 on 2024-05-23 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0002_estado_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='foto_producto',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='nombre',
        ),
    ]