# Generated by Django 4.0.6 on 2022-10-11 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day_by_day', '0012_alter_message_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]