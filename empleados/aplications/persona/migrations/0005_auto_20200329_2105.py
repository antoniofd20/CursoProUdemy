# Generated by Django 3.0.4 on 2020-03-30 03:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre completo'),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]
