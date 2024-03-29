# Generated by Django 2.2.6 on 2019-10-30 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0021_auto_20191030_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bebida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='bebida',
            field=models.ManyToManyField(to='sistema.Bebida'),
        ),
    ]
