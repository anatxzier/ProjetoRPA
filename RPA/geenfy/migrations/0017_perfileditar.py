# Generated by Django 5.0.8 on 2024-09-19 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geenfy', '0016_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerfilEditar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=55)),
                ('imgPerfil', models.ImageField(upload_to='imgPerfilEditar/')),
            ],
        ),
    ]
