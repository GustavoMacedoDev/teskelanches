# Generated by Django 2.2.6 on 2019-11-02 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0027_pedido_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('ATIVO', 'ativo'), ('CANCELADO', 'cancelado'), ('BAIXADO', 'baixado')], max_length=50),
        ),
    ]
