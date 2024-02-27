# Generated by Django 4.2.7 on 2024-01-24 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_date_posted_alter_recipebook_date_created_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 12, 13, 27, 652333, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recipebook',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 12, 13, 27, 653896, tzinfo=datetime.timezone.utc)),
        ),
    ]
