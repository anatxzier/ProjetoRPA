# Generated by Django 5.1 on 2024-09-24 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geenfy', '0018_rename_arquino_fineshed_finished_file_arquivo_fineshed_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=55)),
                ('imgInfo', models.ImageField(upload_to='imgInfo/')),
            ],
        ),
    ]