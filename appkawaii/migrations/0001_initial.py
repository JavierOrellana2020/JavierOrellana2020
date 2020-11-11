# Generated by Django 3.1.2 on 2020-10-31 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.DecimalField(decimal_places=0, max_digits=13)),
                ('descripcion', models.TextField(max_length=100)),
                ('stock', models.IntegerField()),
                ('precioCosto', models.IntegerField()),
                ('precioVenta', models.IntegerField()),
            ],
        ),
    ]
