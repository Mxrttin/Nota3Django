# Generated by Django 5.0.6 on 2024-06-30 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_serie_remove_libros_serie_libros_id_serie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='descripcion',
            field=models.CharField(max_length=700),
        ),
    ]
