# Generated by Django 2.2.6 on 2019-10-29 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0015_auto_20191029_0210'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='numero_pedido',
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
    ]
