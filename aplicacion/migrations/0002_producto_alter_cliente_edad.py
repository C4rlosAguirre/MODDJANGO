# Generated by Django 4.0.4 on 2022-05-05 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('cliente_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='aplicacion.cliente')),
            ],
            bases=('aplicacion.cliente',),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
