# Generated by Django 4.0.5 on 2022-06-17 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.CharField(max_length=100),
        ),
    ]
