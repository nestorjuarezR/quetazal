# Generated by Django 4.1.13 on 2024-02-06 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_articulo_tags_imagenproducto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproducto',
            name='articulo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='store.articulo'),
        ),
    ]