# Generated by Django 3.1.5 on 2021-02-24 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathway',
            name='pathName',
            field=models.CharField(max_length=150),
        ),
    ]