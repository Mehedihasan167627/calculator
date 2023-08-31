# Generated by Django 4.2.4 on 2023-08-31 07:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_member_is_bazar_done'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bazarlist',
            name='date',
        ),
        migrations.RemoveField(
            model_name='fine',
            name='date',
        ),
        migrations.RemoveField(
            model_name='member',
            name='date',
        ),
        migrations.AlterField(
            model_name='bazarcost',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2023, 8, 31)),
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(default=datetime.date(2023, 9, 1)),
        ),
        migrations.AlterField(
            model_name='moneydeposit',
            name='date',
            field=models.DateField(verbose_name=datetime.date(2023, 8, 31)),
        ),
    ]