# Generated by Django 4.1.2 on 2022-10-10 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_by_day', '0004_article_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=100),
        ),
    ]
