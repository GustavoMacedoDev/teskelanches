# Generated by Django 2.2.6 on 2019-11-02 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0029_auto_20191102_0245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Caixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_abertura', models.DateField()),
                ('data_fechamento', models.DateField()),
                ('observacao', models.CharField(max_length=50)),
            ],
        ),
    ]