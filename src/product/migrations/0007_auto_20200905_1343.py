# Generated by Django 3.1.1 on 2020-09-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20200905_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
