# Generated by Django 3.1.3 on 2023-03-24 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manhwas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(default=' ')),
                ('genero', models.TextField(default=' ')),
                ('descripcion', models.TextField(default=' ')),
                ('autor', models.TextField(default=' ')),
                ('estado', models.TextField(default=' ')),
                ('capitulos', models.IntegerField(blank=True, default=1)),
                ('artista', models.TextField(default=' ')),
                ('pais', models.TextField(blank=True, default=' ')),
                ('clasificacion', models.TextField(blank=True, default=1)),
                ('adaptacion', models.TextField(default='No')),
            ],
        ),
    ]
