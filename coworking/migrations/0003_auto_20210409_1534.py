# Generated by Django 3.1.6 on 2021-04-09 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0002_auto_20210409_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reservation',
            options={'verbose_name': 'Бронь', 'verbose_name_plural': 'Заказы на бронь'},
        ),
    ]