# Generated by Django 3.1.5 on 2021-02-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_pathway_pathdescript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pathway',
            name='pathDescript',
            field=models.TextField(null=True),
        ),
    ]