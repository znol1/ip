# Generated by Django 3.2 on 2021-05-18 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0008_auto_20210518_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedtime',
            name='end',
            field=models.DateTimeField(null=True, verbose_name='Конец'),
        ),
        migrations.AlterField(
            model_name='bookedtime',
            name='start',
            field=models.DateTimeField(null=True, verbose_name='Начало'),
        ),
    ]
