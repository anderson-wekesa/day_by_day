# Generated by Django 4.1.2 on 2022-10-11 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_by_day', '0008_alter_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
