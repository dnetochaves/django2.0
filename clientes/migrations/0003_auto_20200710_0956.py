# Generated by Django 3.0.7 on 2020-07-10 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_auto_20200629_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='doc',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clientes.Document'),
        ),
    ]