# Generated by Django 4.1.5 on 2023-01-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_pelicula_options_alter_pelicula_imagen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pelicula',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='media/avatar'),
        ),
    ]