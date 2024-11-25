# Generated by Django 5.0.8 on 2024-08-13 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geenfy', '0005_alter_homepage_texto_alter_homepage_titulo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=55)),
                ('imgLog', models.ImageField(upload_to='imgLogin/')),
            ],
        ),
        migrations.AlterField(
            model_name='homepage',
            name='texto',
            field=models.CharField(max_length=100),
        ),
    ]
