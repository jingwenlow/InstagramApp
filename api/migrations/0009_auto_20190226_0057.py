# Generated by Django 2.1.5 on 2019-02-26 00:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190226_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_received',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='time_sent',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
