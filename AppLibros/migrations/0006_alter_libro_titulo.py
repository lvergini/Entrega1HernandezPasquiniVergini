# Generated by Django 4.0.6 on 2022-08-30 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppLibros', '0005_rename_publication_date_libro_fecha_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]
