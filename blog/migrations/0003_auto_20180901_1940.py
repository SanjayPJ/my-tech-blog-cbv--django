# Generated by Django 2.1 on 2018-09-01 14:10

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180901_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 14, 10, 42, 611715, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 1, 14, 10, 42, 611715, tzinfo=utc)),
        ),
    ]
