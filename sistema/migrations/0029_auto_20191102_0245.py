# Generated by Django 2.2.6 on 2019-11-02 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0028_auto_20191102_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='status',
            field=models.CharField(choices=[('ATIVO', 'ativo'), ('CANCELADO', 'cancelado'), ('BAIXADO', 'baixado')], default='ATIVO', max_length=50),
        ),
    ]