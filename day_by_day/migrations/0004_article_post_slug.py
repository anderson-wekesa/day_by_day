# Generated by Django 4.1.2 on 2022-10-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_by_day', '0003_alter_article_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='post_slug',
            field=models.SlugField(max_length=200, null=True),
        ),
    ]