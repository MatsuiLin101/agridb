# Generated by Django 2.1.2 on 2018-11-15 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0006_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='name',
            field=models.CharField(max_length=10, null=True, unique=True),
        ),
    ]
