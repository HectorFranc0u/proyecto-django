# Generated by Django 4.1.2 on 2022-10-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbCombos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CombName', models.CharField(max_length=200)),
                ('CombTipo', models.CharField(max_length=200)),
                ('ComPrecio', models.CharField(max_length=10)),
                ('CombDescripcion', models.CharField(max_length=200)),
                ('CombDisp', models.BooleanField()),
                ('idProducto', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tbProductos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProdTipo', models.CharField(max_length=200)),
                ('ProdUnidaddeMed', models.CharField(max_length=10)),
                ('ProdName', models.CharField(max_length=5)),
                ('idProveedor', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='tbProveedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProvEmpresa', models.CharField(max_length=200)),
                ('ProvName', models.CharField(max_length=200)),
                ('ProvLastname', models.CharField(max_length=200)),
                ('ProvPais', models.CharField(max_length=200)),
                ('ProvTipoProd', models.CharField(max_length=200)),
                ('idSucursal', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='tbSucursales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SucName', models.CharField(max_length=200)),
                ('SucAddress', models.TextField()),
                ('SucGerente', models.CharField(max_length=200)),
                ('SucHorarios', models.CharField(max_length=200)),
                ('SucCombos', models.CharField(max_length=200)),
                ('idCombos', models.CharField(max_length=10)),
            ],
        ),
    ]
