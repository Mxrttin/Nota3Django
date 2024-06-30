# Generated by Django 5.0.6 on 2024-06-30 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('serie', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=100)),
                ('publicacion', models.DateField()),
                ('escritor', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=300)),
                ('imagen', models.ImageField(null=True, upload_to='libros')),
                ('precio', models.CharField(max_length=20)),
            ],
        ),
    ]