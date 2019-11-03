# Generated by Django 2.2.6 on 2019-11-02 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0031_auto_20191102_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lancamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacao', models.CharField(max_length=50, verbose_name='Observação')),
                ('caixa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Caixa')),
            ],
        ),
    ]