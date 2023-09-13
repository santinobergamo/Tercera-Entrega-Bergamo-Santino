# Generated by Django 4.2.5 on 2023-09-12 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProject', '0007_detallepedidocompra_pedidocompra_proveedor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidocompra',
            name='detalles',
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidocompra',
            name='producto',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='AppProject.producto'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DetallePedidoCompra',
        ),
    ]
