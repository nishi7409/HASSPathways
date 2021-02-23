# Generated by Django 3.1.5 on 2021-02-22 14:07

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=10)),
                ('ID', models.IntegerField()),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('HI', models.IntegerField(default=0)),
                ('CI', models.IntegerField(default=0)),
                ('DI', models.IntegerField(default=0)),
                ('fall', models.IntegerField(default=0)),
                ('spring', models.IntegerField(default=0)),
                ('summer', models.IntegerField(default=0)),
                ('pathways', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=150), blank=True, default=list, null=True, size=10)),
            ],
        ),
    ]