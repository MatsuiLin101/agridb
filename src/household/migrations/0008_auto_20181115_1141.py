# Generated by Django 2.1.2 on 2018-11-15 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('household', '0007_auto_20181115_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='year',
            name='name',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]