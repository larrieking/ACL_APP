# Generated by Django 4.0.6 on 2022-08-02 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 2, 14, 55, 3, 749368, tzinfo=utc)),
        ),
    ]