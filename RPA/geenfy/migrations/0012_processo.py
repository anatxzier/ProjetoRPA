# Generated by Django 5.0.8 on 2024-08-29 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geenfy', '0011_lixeira'),
    ]

    operations = [
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=55)),
            ],
        ),
    ]
