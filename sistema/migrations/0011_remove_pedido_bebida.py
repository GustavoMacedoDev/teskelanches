# Generated by Django 2.2.6 on 2019-10-28 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0010_auto_20191028_1613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='bebida',
        ),
    ]
