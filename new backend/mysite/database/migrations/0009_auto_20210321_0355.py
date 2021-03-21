# Generated by Django 3.1.5 on 2021-03-21 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20210225_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='pathway',
            name='priority1',
            field=models.ManyToManyField(related_name='priority1', to='database.Course'),
        ),
        migrations.AddField(
            model_name='pathway',
            name='priority2',
            field=models.ManyToManyField(related_name='priority2', to='database.Course'),
        ),
        migrations.AddField(
            model_name='pathway',
            name='priority3',
            field=models.ManyToManyField(related_name='priority3', to='database.Course'),
        ),
    ]
