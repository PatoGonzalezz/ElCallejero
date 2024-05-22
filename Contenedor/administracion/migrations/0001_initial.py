# Generated by Django 5.0.4 on 2024-05-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('foto_producto', models.ImageField(blank=True, null=True, upload_to='')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.CharField(max_length=100)),
            ],
        ),
    ]
