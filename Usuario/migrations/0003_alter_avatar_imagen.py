# Generated by Django 4.1.5 on 2023-01-17 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuario', '0002_rename_user_usuario_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='imagen',
            field=models.ImageField(upload_to='avatar'),
        ),
    ]
