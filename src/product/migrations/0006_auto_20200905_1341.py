# Generated by Django 3.1.1 on 2020-09-05 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20200905_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='crop',
            name='summary',
        ),
        migrations.RemoveField(
            model_name='machinerie',
            name='summary',
        ),
        migrations.AddField(
            model_name='machinerie',
            name='condition',
            field=models.TextField(default='ye'),
        ),
        migrations.AddField(
            model_name='machinerie',
            name='image',
            field=models.TextField(default='image'),
        ),
        migrations.AddField(
            model_name='machinerie',
            name='location',
            field=models.TextField(default='ye'),
        ),
        migrations.AlterField(
            model_name='crop',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
