# Generated by Django 4.1.5 on 2023-01-23 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_alter_pelicula_imagen'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autor',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Genero',
        ),
    ]