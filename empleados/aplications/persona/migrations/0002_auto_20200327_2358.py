# Generated by Django 3.0.4 on 2020-03-28 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades empleado',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['last_name', 'first_name'], 'verbose_name': 'Mi empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
    ]
