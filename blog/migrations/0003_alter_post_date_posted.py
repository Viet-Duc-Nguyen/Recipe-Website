# Generated by Django 4.2.7 on 2024-01-03 13:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 3, 13, 30, 22, 887981, tzinfo=datetime.timezone.utc)),
        ),
    ]
