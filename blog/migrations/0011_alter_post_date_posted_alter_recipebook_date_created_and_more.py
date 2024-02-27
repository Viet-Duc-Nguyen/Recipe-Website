# Generated by Django 4.2.7 on 2024-01-24 09:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_recipebook_color_alter_post_date_posted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 9, 32, 31, 693559, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recipebook',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 24, 9, 32, 31, 694295, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='recipebook',
            name='recipes',
            field=models.ManyToManyField(related_name='recipe_books', to='blog.post'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.post')),
            ],
        ),
    ]