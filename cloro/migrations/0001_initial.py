# Generated by Django 4.2.3 on 2024-02-20 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CloroModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('UNSAAC_TESIS_ELECTRONICA', models.CharField(max_length=255, verbose_name='Nombre del Sistema')),
                ('data_cloro', models.CharField(max_length=10, verbose_name='Dato de Cloro')),
                ('data_turbidez', models.CharField(max_length=10, verbose_name='Dato de Turbidez')),
            ],
            options={
                'db_table': 'cloro',
                'ordering': ['-created_at'],
            },
        ),
    ]
