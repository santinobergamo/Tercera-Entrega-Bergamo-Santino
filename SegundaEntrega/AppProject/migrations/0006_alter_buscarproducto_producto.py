# Generated by Django 4.2.5 on 2023-09-09 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AppProject', '0005_alter_buscarproducto_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buscarproducto',
            name='producto',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppProject.producto'),
        ),
    ]