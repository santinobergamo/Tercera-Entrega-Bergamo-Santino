# Generated by Django 4.2.5 on 2023-09-12 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppProject', '0008_remove_pedidocompra_detalles_pedidocompra_cantidad_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidocompra',
            name='producto',
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='codigo_producto',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='nombre_producto',
            field=models.CharField(default=0, max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pedidocompra',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
